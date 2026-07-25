# Zomato Restaurant Scraper (Python)

Scrape restaurant listings from Zomato by city and cuisine — names, localities, cuisines, dining & delivery ratings, cost for two and photos. No login, runs on cheap datacenter proxy.

A tiny, real Python client for the **[themineworks/zomato-scraper](https://apify.com/themineworks/zomato-scraper)** actor on Apify — run it, get structured data, export CSV. No scraping infrastructure to maintain, no proxies to buy, no login.

[![Apify Actor](https://img.shields.io/badge/Apify-zomato-restaurant-scraper-97d700)](https://apify.com/themineworks/zomato-scraper)

## Quickstart

```bash
pip install -r requirements.txt
export APIFY_TOKEN=apify_api_xxx        # free token: https://console.apify.com/account/integrations
python zomato_scraper.py --city "Mumbai" --max 25 --out results.csv
```

That runs the hosted actor and writes a clean CSV. New Apify accounts include free platform credits, so you can try it at no cost.

## Output fields

| field |
|---|
| `name` |
| `city` |
| `locality` |
| `address` |
| `cuisines` |
| `rating_dining` |
| `rating_delivery` |
| `cost_for_two` |
| `restaurant_url` |
| `image_url` |
| `scraped_at` |

## Why the hosted actor?

The scraping itself — anti-bot handling, proxy rotation, phone/field resolution — runs on Apify, so this client stays a few lines. You only pay for delivered results; empty or failed runs are never billed.

## Links

- **Actor:** https://apify.com/themineworks/zomato-scraper
- **All themineworks scrapers:** https://apify.com/themineworks
- **Apify Python client docs:** https://docs.apify.com/api/client/python/

## License

MIT © The Mine Works
