# Zomato Scraper: Restaurant Ratings, Cuisine & Pricing

Scrape Zomato restaurant listings by city and cuisine: name, locality, address, cuisines, dining and delivery ratings, cost for two, and photo. India restaurant data and lead generation at scale. No login required.

**Run it on Apify:** [apify.com/themineworks/zomato-scraper](https://apify.com/themineworks/zomato-scraper)
**Docs, FAQ and pricing:** [themineworks.com/actors/zomato-scraper](https://themineworks.com/actors/zomato-scraper/)

**Price:** From $1.80 per 1,000 restaurants on Apify's higher plans ($3.00 on the free plan), plus a $0.005 start fee per run. Failed and empty results are never charged.

## What it returns

* Search by city and cuisine type
* Name, locality, full address, and cuisine tags
* Separate dining and delivery ratings
* Cost-for-two and representative photo
* No login, no API key required

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/zomato-scraper").call(run_input={
    "city": "Mumbai",
    "searchQuery": "Biryani",
    "maxResults": 5
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/zomato-scraper').call({
    "city": "Mumbai",
    "searchQuery": "Biryani",
    "maxResults": 5
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~zomato-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"city": "Mumbai", "searchQuery": "Biryani", "maxResults": 5}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 zomato_restaurant_scraper.py --token YOUR_APIFY_TOKEN --city "Mumbai" --search-query "Biryani" --max-results "5"
node zomato_restaurant_scraper.mjs --token YOUR_APIFY_TOKEN --city "Mumbai" --search-query "Biryani" --max-results "5"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `city` | string |  | Indian city to search restaurants in (for example Mumbai, Delhi, Bangalore, Hyderabad, Pune, Chennai) |
| `searchQuery` | string |  | Optional cuisine or dish to filter by (for example Korean, Pizza, Biryani, Chinese, Desserts) |
| `maxResults` | integer | `30` | Maximum number of restaurants to return |
| `allowResidentialFallback` | boolean | `true` | If the cheap datacenter attempt on page 1 is blocked, retry once on residential proxy before giving up |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `name` | string | Restaurant name |
| `city` | string | City searched |
| `locality` | string | Locality / neighbourhood within the city |
| `address` | string | Full address string |
| `cuisines` | array | List of cuisine tags |
| `rating_dining` | number | Zomato dining rating (out of 5) |
| `rating_delivery` | number | Zomato delivery rating (out of 5) |
| `cost_for_two` | number | Approximate cost for two people, in INR |
| `restaurant_url` | string | Zomato restaurant page URL |
| `image_url` | string | Featured photo URL |
| `scraped_at` | string | ISO-8601 timestamp when this record was scraped |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/zomato-scraper
```

## FAQ

### Does it cover both dine-in and delivery-only restaurants?

Yes. The actor returns both, with separate rating fields for dining and delivery where Zomato reports them separately.

### What is the price?

Pay per result: from $1.80 per 1,000 restaurants on Apify's higher plans, $3.00 on the free plan, plus a $0.005 start fee per run. Failed results are never charged.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [B2B Leads Finder](https://themineworks.com/actors/b2b-leads-finder/): Business emails and LinkedIn profiles for target companies
* [LinkedIn Company Scraper](https://themineworks.com/actors/linkedin-company-details/): Company size, industry, website, and followers without login
* [Zillow Rental Listings Scraper](https://themineworks.com/actors/zillow-rental-listings/): Scrape Zillow for-rent listings by city or zip. $1 per 1,000 results

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works
