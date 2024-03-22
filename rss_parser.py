#!/usr/bin/env python3

# Jonas Stolt, jontas@gmx.com
# RSS-parser för Conky
# Installera feedparser med t ex. pip install feedparser
# Idéer från:
# https://mr-destructive.github.io/techstructive-blog/python-feedparser/

import feedparser
import sys

def get_feed(uri, lines=5): # URL och antal rubriker, default 5
    try:
        feed = feedparser.parse(uri)
        for item in feed.entries[:lines]:
            print(item.title)
    except Exception as e:
        print(f"Fel: {e}")

def main():
    fallback_uri = "https://api.sr.se/api/rss/program/104"
    uri = sys.argv[1] if len(sys.argv) >= 1 else fallback_uri
    lines = int(sys.argv[2]) if len(sys.argv) > 1 else 5
    get_feed(uri, lines)

if __name__ == "__main__":
    main()