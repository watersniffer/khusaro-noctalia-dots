#!/usr/bin/env python3
import sys, re, urllib.request, urllib.parse, json
BASE = "https://motionbgs.com"
UA = "Mozilla/5.0 (X11; Linux x86_64) Quickshell"

# One card = one <a href=/slug> ... </a> block containing the thumbnail <img>.
CARD = re.compile(r'<a\b([^>]*)>(.*?)</a>', re.S)
HREF = re.compile(r'href=/([a-z0-9-]+)')
TITLE = re.compile(r'title="([^"]+)"')
IMG = re.compile(r'<img[^>]*src=(/i/c/[^ >]+media/(\d+)/[^ >]+)')
SKIP = ("", "4k", "mobile", "gifs", "tag")


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.8",
    })
    return urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "ignore")


def parse(html):
    items = []
    seen = set()
    for card in CARD.finditer(html):
        href = HREF.search(card.group(1))
        img = IMG.search(card.group(2))
        if not href or not img:
            continue
        slug = href.group(1)
        if slug in SKIP or slug in seen:
            continue
        seen.add(slug)
        mid = img.group(2)
        title = TITLE.search(card.group(0))
        label = title.group(1) if title else slug.replace("-", " ").title()
        label = re.sub(r'\s+live wallpaper$', '', label, flags=re.I)
        items.append({
            "title": label,
            "url": BASE + "/" + slug,
            "thumb": BASE + img.group(1),
            "video": BASE + "/media/" + mid + "/" + slug + ".960x540.mp4",
        })
    return items


def main():
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        page = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    except ValueError:
        page = 1
    if page < 1:
        page = 1
    # Page 1 lives at "/", every later page at "/<n>/". Search is served from
    # "/search?q=..." and is not paginated.
    url = BASE + "/" if page <= 1 else BASE + "/" + str(page) + "/"
    if q.strip():
        if page > 1:
            print("[]")
            return
        url = BASE + "/search?q=" + urllib.parse.quote(q)
    try:
        html = fetch(url)
    except Exception as e:
        # Empty list is what the shell reads as "nothing more to show".
        print("[]")
        print("motionbgs-fetch: %s" % e, file=sys.stderr)
        return
    print(json.dumps(parse(html)))


if __name__ == "__main__":
    main()
