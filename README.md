# Reddit Traffic and Intelligence API

Find Reddit threads that rank on Google. Traffic estimates, SERP positions, multi-dimensional brand sentiment. One API call.

**[Get API Key (Zyla)](https://zylalabs.com/api-marketplace/other/reddit+traffic+plus+intelligence+api/11553)** | **[Get API Key (RapidAPI)](https://rapidapi.com/greg01060/api/reddit-traffic-and-intelligence-api)** | **[Documentation](https://www.redranks.com/api-docs.html)** | **[Sample Report](https://www.redranks.com/demo-report.html)**

---

## What It Does

Enter a keyword. Get back the top Reddit threads ranking on Google for that term - with traffic estimates, SERP positions, and detailed brand sentiment breakdowns.

- **Traffic Intelligence** - Reddit threads ranking on Google with monthly traffic estimates
- **Brand Sentiment** - Multi-dimensional sentiment (positive/negative/neutral) with specific praise and complaints
- **Keyword Metrics** - Search volume, CPC, keyword difficulty
- **Thread Analysis** - Pain points, buyer intent, feature requests

## Quick Start

### Using Zyla API Hub

```javascript
const response = await fetch('https://zylalabs.com/api/5765/reddit+traffic+plus+intelligence+api/11553/discover+threads', {
	method: 'POST',
	headers: {
		'Authorization': 'Bearer YOUR_ZYLA_API_KEY',
		'Content-Type': 'application/json'
	},
	body: JSON.stringify({
		keyword: 'CRM software',
		your_brand: 'Acme CRM',
		competitors: ['HubSpot', 'Salesforce', 'Pipedrive'],
		max_threads: 10
	})
});

const data = await response.json();
console.log(data);
```

### Using RapidAPI

```javascript
const response = await fetch('https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2/discover-threads', {
	method: 'POST',
	headers: {
		'X-RapidAPI-Key': 'YOUR_RAPIDAPI_KEY',
		'X-RapidAPI-Host': 'reddit-traffic-and-intelligence-api.p.rapidapi.com',
		'Content-Type': 'application/json'
	},
	body: JSON.stringify({
		keyword: 'CRM software',
		your_brand: 'Acme CRM',
		competitors: ['HubSpot', 'Salesforce', 'Pipedrive'],
		max_threads: 10
	})
});

const data = await response.json();
console.log(data);
```

## Example Response

```json
{
	"status": "success",
	"keyword": "CRM software",
	"keyword_metrics": {
		"volume": 84192,
		"cpc": 14.61,
		"keyword_difficulty": 71.9,
		"search_intent": "commercial"
	},
	"threads_discovered": 8,
	"threads": [
		{
			"post_id": "1e5141p",
			"url": "https://www.reddit.com/r/smallbusiness/comments/1e5141p/",
			"title": "Best CRM for small business?",
			"subreddit": "smallbusiness",
			"source": "discussion_box",
			"position": 0,
			"estimated_traffic": 33677,
			"ctr": 0.4,
			"priority": "HIGH",
			"analysis": {
				"sentiment": "mixed",
				"buyer_intent": "high",
				"pain_points": ["pricing complexity", "learning curve"],
				"brand_sentiments": {
					"HubSpot": {
						"sentiment": "mixed",
						"positive": 15,
						"negative": 8,
						"neutral": 3,
						"confidence": 0.87,
						"praise": ["easy to use", "good free tier", "great integrations"],
						"complaints": ["expensive at scale", "pushy sales team"]
					},
					"Salesforce": {
						"sentiment": "negative",
						"positive": 4,
						"negative": 12,
						"neutral": 2,
						"confidence": 0.82,
						"praise": ["powerful features", "industry standard"],
						"complaints": ["too complex", "expensive", "overkill for SMB"]
					}
				}
			}
		}
	],
	"summary": {
		"total_threads": 8,
		"by_priority": {"HIGH": 3, "MEDIUM": 4, "LOW": 1},
		"estimated_monthly_traffic": 134705
	}
}
```

## Use Cases

- **Competitive Intelligence Platforms** - Add Reddit sentiment as a data source
- **SEO Tools** - Track Reddit threads ranking for target keywords
- **Brand Monitoring** - Monitor brand mentions in high-visibility threads
- **Sales Enablement** - Auto-generate battle cards from competitor sentiment
- **Market Research** - Understand what real users say about products
- **Content Strategy** - Find content gaps where Reddit ranks

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `keyword` | string | Yes | - | The keyword to search (2-100 characters) |
| `your_brand` | string | No | null | Your brand name for mention analysis |
| `competitors` | array | No | null | Competitor brands to track (max 20) |
| `max_threads` | integer | No | 5 | Number of threads to return (0-20) |
| `max_comments_per_thread` | integer | No | 5 | Comments per thread (0-20) |
| `data_freshness` | string | No | "balanced" | "realtime", "balanced", or "custom" |

## Pricing

Available on both Zyla API Hub and RapidAPI with free tiers:

| Tier | Zyla | RapidAPI |
|------|------|----------|
| Free | 25 searches | 15 searches |
| Paid | From $24.99/mo | From $49/mo |

**[Start Free on Zyla](https://zylalabs.com/api-marketplace/other/reddit+traffic+plus+intelligence+api/11553)** | **[Start Free on RapidAPI](https://rapidapi.com/greg01060/api/reddit-traffic-and-intelligence-api)**

## Response Time

- **Fresh requests:** 20-30 seconds (hits all data sources)
- **Cached requests:** Under 1 second

## FAQ

**What about rate limits?**

None. Your plan determines your monthly quota, not how fast you can use it.

**How do you calculate traffic estimates?**

`traffic = search_volume x position_ctr`. We include the CTR rate in every response so you can verify.

**What's the difference between fresh and cached?**

Fresh requests query all data sources (20-30s). Cached responses return instantly. Use `data_freshness: "realtime"` for guaranteed fresh data.

## Examples

See the `/examples` directory for complete working examples:

- **Python** - `examples/python/example.py`
- **JavaScript** - `examples/javascript/example.js`
- **cURL** - `examples/curl/examples.sh`

## Links

- [Website](https://www.redranks.com)
- [API Documentation](https://www.redranks.com/api-docs.html)
- [Sample Report](https://www.redranks.com/demo-report.html)
- [Zyla API Hub](https://zylalabs.com/api-marketplace/other/reddit+traffic+plus+intelligence+api/11553)
- [RapidAPI](https://rapidapi.com/greg01060/api/reddit-traffic-and-intelligence-api)

## License

This repository contains documentation and examples for the Reddit Traffic and Intelligence API. See [LICENSE](LICENSE) for details.
