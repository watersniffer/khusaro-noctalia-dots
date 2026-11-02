#!/usr/bin/env python3
import sys, re, urllib.request
url = sys.argv[1]
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "ignore")
m = re.search(r'<video[^>]*>.*?<source[^>]*src="([^"]+)"', html, re.S | re.I)
if not m:
    m = re.search(r'<source[^>]*src="([^"]+\.webm[^"]*)"', html, re.I)
v = m.group(1) if m else ""
if v and not v.startswith("http"):
    v = "https://moewalls.com" + (v if v.startswith("/") else "/" + v)
print(v)
