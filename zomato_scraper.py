#!/usr/bin/env python3
"""Zomato Restaurant Scraper (Python) — run the hosted Apify actor and export results to CSV.

Powered by the themineworks/zomato-scraper actor on Apify. Get a free API token at
https://console.apify.com/account/integrations (new accounts include free credits).

    pip install -r requirements.txt
    export APIFY_TOKEN=apify_api_xxx
    python zomato_scraper.py --city "Mumbai" --max 25
"""
import argparse, csv, os, sys
from apify_client import ApifyClient

FIELDS = ['name', 'city', 'locality', 'address', 'cuisines', 'rating_dining', 'rating_delivery', 'cost_for_two', 'restaurant_url', 'image_url', 'scraped_at']

def main():
    ap = argparse.ArgumentParser(description="Zomato Restaurant Scraper (Python)")
    ap.add_argument("--city", default='Mumbai', help="Indian city")
    ap.add_argument("--query", default='', help="Cuisine / dish (optional)")
    ap.add_argument("--max", type=int, default=30, help="Max results")
    ap.add_argument("--out", default="results.csv", help="Output CSV path")
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    args = ap.parse_args()
    if not args.token:
        sys.exit("Missing Apify token. Pass --token or set APIFY_TOKEN. Get one free at "
                 "https://console.apify.com/account/integrations")

    client = ApifyClient(args.token)
    run_input = {
        "city": args.city,
        "searchQuery": args.query,
        "maxResults": args.max,
        "proxyConfiguration": {"useApifyProxy": True}
    }
    print(f"Running themineworks/zomato-scraper ...", file=sys.stderr)
    run = client.actor("themineworks/zomato-scraper").call(run_input=run_input)

    rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: (", ".join(v) if isinstance(v, list) else v) for k, v in r.items()})

    for r in rows[:10]:
        print(" | ".join(str(r.get(c, "")) for c in ['name', 'locality', 'rating_dining', 'cost_for_two']))
    print(f"\n{len(rows)} rows written to {args.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
