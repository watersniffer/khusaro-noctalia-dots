#!/usr/bin/env python3
import sys, json, re, urllib.parse, urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) Quickshell"
BASE = "https://moewalls.com"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode("utf-8", "ignore")

def main():
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    page = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    if q.strip() == "":
        if page <= 1:
            url = BASE + "/"
        else:
            url = BASE + "/page/" + str(page) + "/"
    else:
        qs = urllib.parse.quote(q)
        if page <= 1:
            url = BASE + "/?s=" + qs
        else:
            url = BASE + "/page/" + str(page) + "/?s=" + qs
    html = fetch(url)
    items = []
    for block in re.findall(r'<li class="g1-collection-item g1-collection-item-1of3".*?</li>', html, re.S):
        m = re.search(r'<h3[^>]*entry-title[^>]*>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
        if not m:
            continue
        page_url = m.group(1)
        title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        tm = re.search(r'<img[^>]*src="([^"]+)"', block)
        thumb = tm.group(1) if tm else ""
        items.append({"title": title, "url": page_url, "thumb": thumb})
    print(json.dumps(items))

if __name__ == "__main__":
    main()
