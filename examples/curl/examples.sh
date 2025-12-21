# Reddit Traffic and Intelligence API - cURL Examples

# Get your API key:
#   Zyla:     https://zylalabs.com/api-marketplace/other/reddit+traffic+plus+intelligence+api/11553
#   RapidAPI: https://rapidapi.com/greg01060/api/reddit-traffic-and-intelligence-api


# ============================================================
# ZYLA API HUB EXAMPLES
# ============================================================

# Basic Search (Zyla)
curl -X POST "https://zylalabs.com/api/5765/reddit+traffic+plus+intelligence+api/11553/discover+threads" \
  -H "Authorization: Bearer YOUR_ZYLA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "CRM software",
    "max_threads": 5
  }'

# With Brand Tracking (Zyla)
curl -X POST "https://zylalabs.com/api/5765/reddit+traffic+plus+intelligence+api/11553/discover+threads" \
  -H "Authorization: Bearer YOUR_ZYLA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "CRM software",
    "your_brand": "Acme CRM",
    "competitors": ["HubSpot", "Salesforce", "Pipedrive"],
    "max_threads": 10,
    "max_comments_per_thread": 10
  }'


# ============================================================
# RAPIDAPI EXAMPLES
# ============================================================

# Basic Search (RapidAPI)
curl -X POST "https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2/discover-threads" \
  -H "X-RapidAPI-Key: YOUR_RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: reddit-traffic-and-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "CRM software",
    "max_threads": 5
  }'

# With Brand Tracking (RapidAPI)
curl -X POST "https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2/discover-threads" \
  -H "X-RapidAPI-Key: YOUR_RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: reddit-traffic-and-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "CRM software",
    "your_brand": "Acme CRM",
    "competitors": ["HubSpot", "Salesforce", "Pipedrive"],
    "max_threads": 10,
    "max_comments_per_thread": 10
  }'

# Force Fresh Data - No Cache (RapidAPI)
curl -X POST "https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2/discover-threads" \
  -H "X-RapidAPI-Key: YOUR_RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: reddit-traffic-and-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "project management",
    "data_freshness": "realtime",
    "max_threads": 5
  }'

# Health Check (RapidAPI)
curl -X GET "https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2/health" \
  -H "X-RapidAPI-Key: YOUR_RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: reddit-traffic-and-intelligence-api.p.rapidapi.com"
