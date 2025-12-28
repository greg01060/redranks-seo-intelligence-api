#!/bin/bash

# RedRanks SEO Intelligence API - cURL Examples
#
# Automate SEO with simple API calls. Keyword research, SERP analysis, and discussion discovery.
#
# Get your API key:
#     https://rapidapi.com/greg01060/api/redranks-seo-intelligence-api
#
# Tutorials:
#     https://www.redranks.com/tutorials/


# ============================================================
# Configuration
# ============================================================

# Replace with your API key
RAPIDAPI_KEY="YOUR_RAPIDAPI_KEY"

BASE_URL="https://redranks-seo-intelligence-api.p.rapidapi.com/api/v2"


# ============================================================
# 1. KEYWORD METRICS
# Tutorial: https://www.redranks.com/tutorials/keyword-research-python.html
# ============================================================

# Basic keyword lookup
curl -X POST "$BASE_URL/keyword-metrics" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keywords": ["crm software", "project management"]
  }'

# With related keywords
curl -X POST "$BASE_URL/keyword-metrics" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keywords": ["crm software"],
    "include_related": true,
    "max_related": 10
  }'


# ============================================================
# 2. SERP ANALYSIS
# Tutorial: https://www.redranks.com/tutorials/serp-analysis-python.html
# ============================================================

# Basic SERP analysis
curl -X POST "$BASE_URL/serp-analysis" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "best crm software"
  }'

# With more results
curl -X POST "$BASE_URL/serp-analysis" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "best crm software",
    "include_features": true,
    "max_results": 20
  }'


# ============================================================
# 3. DISCOVER THREADS
# Tutorial: https://www.redranks.com/tutorials/reddit-discussion-discovery.html
# ============================================================

# Basic search
curl -X POST "$BASE_URL/discover-threads" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "CRM software",
    "max_threads": 5
  }'

# With brand tracking
curl -X POST "$BASE_URL/discover-threads" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "CRM software",
    "your_brand": "Acme CRM",
    "competitors": ["HubSpot", "Salesforce", "Pipedrive"],
    "max_threads": 10,
    "max_comments_per_thread": 10
  }'

# Force fresh data (no cache)
curl -X POST "$BASE_URL/discover-threads" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "project management",
    "data_freshness": "realtime",
    "max_threads": 5
  }'


# ============================================================
# 4. ANALYZE THREAD
# Analyze any Reddit thread by URL
# ============================================================

# Basic thread analysis
curl -X POST "$BASE_URL/analyze-threads" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.reddit.com/r/smallbusiness/comments/abc123/best_crm/"
  }'

# With brand tracking
curl -X POST "$BASE_URL/analyze-threads" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.reddit.com/r/smallbusiness/comments/abc123/best_crm/",
    "your_brand": "Acme CRM",
    "competitors": ["HubSpot", "Salesforce"],
    "max_comments": 30
  }'


# ============================================================
# 5. HEALTH CHECK
# ============================================================

curl -X GET "$BASE_URL/health" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: redranks-seo-intelligence-api.p.rapidapi.com"
