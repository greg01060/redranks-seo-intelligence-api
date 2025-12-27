# RedRanks SEO Intelligence API

Automate SEO with Python. Keyword research, SERP analysis, and Reddit discussion discovery - all via simple API calls.

**[Tutorials](https://www.redranks.com/tutorials/)** | **[API Documentation](https://www.redranks.com/api-docs.html)** | **[Demo Report](https://www.redranks.com/demo-report.html)** | **[Get API Key](https://rapidapi.com/greg01060/api/redranks-seo-intelligence-api)**

---

## Endpoints

| Endpoint | What It Does | Response Time |
|----------|--------------|---------------|
| `/keyword-metrics` | Search volume, CPC, difficulty, related keywords | 1-3 seconds |
| `/serp-analysis` | SERP features, organic results, discussion positions | 1-3 seconds |
| `/discover-threads` | Reddit threads on Google + traffic + brand sentiment | 20-30s fresh, <1s cached |

---

## Quick Start

```python
import requests

API_KEY = "your_rapidapi_key"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "reddit-traffic-and-intelligence-api.p.rapidapi.com",
    "Content-Type": "application/json"
}
BASE_URL = "https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2"

# 1. Keyword Research
response = requests.post(f"{BASE_URL}/keyword-metrics", headers=HEADERS, json={
    "keywords": ["crm software", "project management"],
    "include_related": True
})
print(response.json())

# 2. SERP Analysis
response = requests.post(f"{BASE_URL}/serp-analysis", headers=HEADERS, json={
    "keyword": "best crm software"
})
print(response.json())

# 3. Discussion Discovery
response = requests.post(f"{BASE_URL}/discover-threads", headers=HEADERS, json={
    "keyword": "crm software",
    "your_brand": "Acme CRM",
    "competitors": ["HubSpot", "Salesforce"]
})
print(response.json())
```

---

## Tutorials

Learn to use this API with our free Python tutorials:

1. **[Keyword Research](https://www.redranks.com/tutorials/keyword-research-python.html)** - Batch analyze keywords with volume, CPC, and difficulty
2. **[SERP Analysis](https://www.redranks.com/tutorials/serp-analysis-python.html)** - Detect AI Overviews, Discussion Boxes, and track positions
3. **[Discussion Discovery](https://www.redranks.com/tutorials/reddit-discussion-discovery.html)** - Find high-traffic Reddit threads with sentiment analysis
4. **[Automated Reports](https://www.redranks.com/tutorials/automated-seo-reports-python.html)** - Combine all endpoints into scheduled HTML reports

---

## Endpoint Details

### 1. Keyword Metrics

Get search volume, CPC, difficulty, and related keywords.

```bash
POST /api/v2/keyword-metrics
```

**Request:**
```json
{
    "keywords": ["crm software", "project management"],
    "include_related": true,
    "max_related": 10
}
```

**Response:**
```json
{
    "status": "success",
    "keywords": [
        {
            "keyword": "crm software",
            "volume": 83473,
            "cpc": 12.87,
            "keyword_difficulty": 68.9,
            "search_intent": "commercial",
            "related_keywords": [
                {
                    "keyword": "best crm software",
                    "volume": 1152,
                    "cpc": 10.9,
                    "keyword_difficulty": 74.9
                }
            ]
        }
    ]
}
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `keywords` | array | Yes | - | Keywords to analyze (max 10) |
| `include_related` | boolean | No | false | Include related keyword suggestions |
| `max_related` | integer | No | 5 | Related keywords per keyword (1-20) |

---

### 2. SERP Analysis

Analyze search results page with feature detection.

```bash
POST /api/v2/serp-analysis
```

**Request:**
```json
{
    "keyword": "best crm software",
    "include_features": true,
    "max_results": 10
}
```

**Response:**
```json
{
    "status": "success",
    "keyword": "best crm software",
    "serp_features": {
        "has_ai_overview": true,
        "has_discussion_box": true,
        "has_featured_snippet": false,
        "has_people_also_ask": true
    },
    "organic_results": [
        {
            "position": 1,
            "url": "https://www.reddit.com/r/CRM/...",
            "domain": "reddit.com",
            "title": "What's the best CRM?",
            "is_discussion": true
        }
    ],
    "discussion_positions": [1, 4, 7],
    "discussion_count": 3
}
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `keyword` | string | Yes | - | Keyword to analyze |
| `include_features` | boolean | No | true | Include SERP feature detection |
| `max_results` | integer | No | 10 | Organic results to return (1-20) |

---

### 3. Discover Threads

Find Reddit threads ranking on Google with traffic and sentiment.

```bash
POST /api/v2/discover-threads
```

**Request:**
```json
{
    "keyword": "CRM software",
    "your_brand": "Acme CRM",
    "competitors": ["HubSpot", "Salesforce", "Pipedrive"],
    "max_threads": 10
}
```

**Response:**
```json
{
    "status": "success",
    "keyword": "CRM software",
    "keyword_metrics": {
        "volume": 84192,
        "cpc": 14.61,
        "keyword_difficulty": 71.9
    },
    "threads_discovered": 8,
    "threads": [
        {
            "title": "Best CRM for small business?",
            "url": "https://www.reddit.com/r/smallbusiness/...",
            "subreddit": "smallbusiness",
            "source": "discussion_box",
            "position": 0,
            "estimated_traffic": 33677,
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
                        "praise": ["easy to use", "good free tier"],
                        "complaints": ["expensive at scale"]
                    }
                }
            }
        }
    ],
    "summary": {
        "total_threads": 8,
        "estimated_monthly_traffic": 134705
    }
}
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `keyword` | string | Yes | - | Keyword to search (2-100 chars) |
| `your_brand` | string | No | null | Your brand for mention analysis |
| `competitors` | array | No | null | Competitor brands (max 20) |
| `max_threads` | integer | No | 5 | Threads to return (0-20) |
| `max_comments_per_thread` | integer | No | 5 | Comments per thread (0-20) |
| `data_freshness` | string | No | "balanced" | "realtime", "balanced", or "custom" |

---

## Use Cases

- **SEO Tools** - Add keyword research and SERP tracking
- **Competitive Intelligence** - Track brand sentiment across Reddit discussions
- **Content Strategy** - Find content gaps where Reddit ranks
- **Brand Monitoring** - Monitor high-visibility discussions
- **Sales Enablement** - Auto-generate battle cards from sentiment data

---

## Examples

Complete working examples in multiple languages:

- **Python** - `examples/python/example.py`
- **JavaScript** - `examples/javascript/example.js`
- **cURL** - `examples/curl/examples.sh`

---

## Response Times

| Endpoint | Fresh | Cached |
|----------|-------|--------|
| `/keyword-metrics` | 1-3 seconds | N/A |
| `/serp-analysis` | 1-3 seconds | N/A |
| `/discover-threads` | 20-30 seconds | Under 1 second |

---

## Links

- [Website](https://www.redranks.com)
- [Tutorials](https://www.redranks.com/tutorials/)
- [API Documentation](https://www.redranks.com/api-docs.html)
- [Demo Report](https://www.redranks.com/demo-report.html)
- [RapidAPI](https://rapidapi.com/greg01060/api/redranks-seo-intelligence-api)

---

## License

This repository contains documentation and examples for the RedRanks SEO Intelligence API. See [LICENSE](LICENSE) for details.
