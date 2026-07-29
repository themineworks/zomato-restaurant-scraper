#!/usr/bin/env node
// zomato-scraper — Apify actor client.
// Node.js client for the themineworks/zomato-scraper Apify actor: runs it, waits, saves results.json.
// Free Apify account + API token: https://console.apify.com/sign-up
import { ApifyClient } from 'apify-client';
import { writeFileSync } from 'node:fs';

const ACTOR = 'themineworks/zomato-scraper';

// Flags map 1:1 to the actor's input schema. Run: node zomato_restaurant_scraper.mjs --token YOUR_TOKEN --city "Mumbai"
function parseArgs(argv) {
    const out = {};
    for (let i = 0; i < argv.length; i++) {
        if (!argv[i].startsWith('--')) continue;
        const key = argv[i].slice(2);
        const val = (argv[i + 1] && !argv[i + 1].startsWith('--')) ? argv[++i] : true;
        out[key] = val;
    }
    return out;
}

const args = parseArgs(process.argv.slice(2));
const token = args.token || process.env.APIFY_TOKEN;
if (!token) {
    console.error('Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up');
    process.exit(1);
}

const runInput = {};
if (args['city'] !== undefined) runInput.city = args['city'];
if (args['search-query'] !== undefined) runInput.searchQuery = args['search-query'];
if (args['max-results'] !== undefined) runInput.maxResults = parseInt(args['max-results'], 10);

const client = new ApifyClient({ token });
console.log(`Running ${ACTOR} ...`);
const run = await client.actor(ACTOR).call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
writeFileSync('results.json', JSON.stringify(items, null, 2));
console.log(`Saved ${items.length} results to results.json`);
