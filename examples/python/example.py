"""
RedRanks SEO Intelligence API - Python Examples

Automate SEO with Python. Keyword research, SERP analysis, and discussion discovery.

Get your API key:
    https://rapidapi.com/greg01060/api/redranks-seo-intelligence-api

Tutorials:
    https://www.redranks.com/tutorials/

Requirements:
    pip install requests
"""

import requests
from typing import Optional, List
from collections import defaultdict

# ============================================================
# Configuration
# ============================================================

RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"  # Replace with your key

HEADERS = {
	"X-RapidAPI-Key": RAPIDAPI_KEY,
	"X-RapidAPI-Host": "reddit-traffic-and-intelligence-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

BASE_URL = "https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2"

# ============================================================
# API Functions
# ============================================================


def keyword_metrics(
	keywords: List[str],
	include_related: bool = False,
	max_related: int = 5
) -> dict:
	"""
	Get keyword metrics: volume, CPC, difficulty, and related keywords.
	
	Tutorial: https://www.redranks.com/tutorials/keyword-research-python.html
	
	Args:
		keywords: List of keywords to analyze (max 10)
		include_related: Include related keyword suggestions
		max_related: Related keywords per keyword (1-20)
	
	Returns:
		API response with keyword data
	"""
	response = requests.post(
		f"{BASE_URL}/keyword-metrics",
		headers=HEADERS,
		json={
			"keywords": keywords,
			"include_related": include_related,
			"max_related": max_related
		}
	)
	response.raise_for_status()
	return response.json()


def serp_analysis(
	keyword: str,
	include_features: bool = True,
	max_results: int = 10
) -> dict:
	"""
	Analyze SERP for a keyword. Detect features and find discussion positions.
	
	Tutorial: https://www.redranks.com/tutorials/serp-analysis-python.html
	
	Args:
		keyword: Keyword to analyze
		include_features: Include SERP feature detection
		max_results: Organic results to return (1-20)
	
	Returns:
		API response with SERP data
	"""
	response = requests.post(
		f"{BASE_URL}/serp-analysis",
		headers=HEADERS,
		json={
			"keyword": keyword,
			"include_features": include_features,
			"max_results": max_results
		}
	)
	response.raise_for_status()
	return response.json()


def discover_threads(
	keyword: str,
	your_brand: Optional[str] = None,
	competitors: Optional[List[str]] = None,
	max_threads: int = 10,
	max_comments: int = 5,
	data_freshness: str = "balanced"
) -> dict:
	"""
	Discover Reddit threads ranking on Google with traffic and sentiment.
	
	Tutorial: https://www.redranks.com/tutorials/reddit-discussion-discovery.html
	
	Args:
		keyword: The search keyword (2-100 characters)
		your_brand: Your brand name for mention analysis
		competitors: List of competitor brand names (max 20)
		max_threads: Number of threads to return (0-20)
		max_comments: Comments per thread (0-20)
		data_freshness: "realtime", "balanced", or "custom"
	
	Returns:
		API response with thread data
	"""
	response = requests.post(
		f"{BASE_URL}/discover-threads",
		headers=HEADERS,
		json={
			"keyword": keyword,
			"your_brand": your_brand,
			"competitors": competitors,
			"max_threads": max_threads,
			"max_comments_per_thread": max_comments,
			"data_freshness": data_freshness
		}
	)
	response.raise_for_status()
	return response.json()


# ============================================================
# Example 1: Keyword Research
# ============================================================

def example_keyword_research():
	"""
	Batch analyze keywords with related suggestions.
	
	Learn more: https://www.redranks.com/tutorials/keyword-research-python.html
	"""
	print("=" * 60)
	print("EXAMPLE 1: Keyword Research")
	print("=" * 60)
	
	keywords = ["crm software", "project management", "help desk software"]
	
	data = keyword_metrics(keywords, include_related=True, max_related=5)
	
	for kw in data.get("keywords", []):
		print(f"\n{kw['keyword'].upper()}")
		print(f"  Volume: {kw.get('volume', 0):,}/month")
		print(f"  CPC: ${kw.get('cpc', 0):.2f}")
		print(f"  Difficulty: {kw.get('keyword_difficulty', 0)}/100")
		print(f"  Intent: {kw.get('search_intent', 'unknown')}")
		
		related = kw.get("related_keywords", [])
		if related:
			print(f"  Related keywords:")
			for r in related[:3]:
				print(f"    - {r['keyword']} ({r.get('volume', 0):,}/mo)")


# ============================================================
# Example 2: SERP Analysis
# ============================================================

def example_serp_analysis():
	"""
	Analyze SERP features and find discussion opportunities.
	
	Learn more: https://www.redranks.com/tutorials/serp-analysis-python.html
	"""
	print("\n" + "=" * 60)
	print("EXAMPLE 2: SERP Analysis")
	print("=" * 60)
	
	keyword = "best crm software"
	
	data = serp_analysis(keyword, max_results=10)
	
	print(f"\nKeyword: {data.get('keyword')}")
	
	# SERP Features
	features = data.get("serp_features", {})
	print("\nSERP Features Detected:")
	print(f"  AI Overview: {'Yes' if features.get('has_ai_overview') else 'No'}")
	print(f"  Discussion Box: {'Yes' if features.get('has_discussion_box') else 'No'}")
	print(f"  Featured Snippet: {'Yes' if features.get('has_featured_snippet') else 'No'}")
	print(f"  People Also Ask: {'Yes' if features.get('has_people_also_ask') else 'No'}")
	
	# Discussion positions
	disc_positions = data.get("discussion_positions", [])
	print(f"\nDiscussions found at positions: {disc_positions}")
	
	# Top results
	print("\nTop 5 Organic Results:")
	for result in data.get("organic_results", [])[:5]:
		disc_marker = " [DISCUSSION]" if result.get("is_discussion") else ""
		print(f"  {result['position']}. {result['domain']}{disc_marker}")


# ============================================================
# Example 3: Discussion Discovery
# ============================================================

def example_discussion_discovery():
	"""
	Find Reddit threads with traffic estimates and brand sentiment.
	
	Learn more: https://www.redranks.com/tutorials/reddit-discussion-discovery.html
	"""
	print("\n" + "=" * 60)
	print("EXAMPLE 3: Discussion Discovery")
	print("=" * 60)
	
	data = discover_threads(
		keyword="CRM software",
		your_brand="Acme CRM",
		competitors=["HubSpot", "Salesforce", "Pipedrive"],
		max_threads=5
	)
	
	print(f"\nKeyword: {data.get('keyword')}")
	
	# Keyword metrics
	metrics = data.get("keyword_metrics", {})
	print(f"Search Volume: {metrics.get('volume', 0):,}/month")
	
	# Summary
	summary = data.get("summary", {})
	print(f"Threads Found: {summary.get('total_threads', 0)}")
	print(f"Total Traffic: {summary.get('estimated_monthly_traffic', 0):,}/month")
	
	# Top threads
	print("\nTop Threads:")
	for thread in data.get("threads", [])[:3]:
		print(f"\n  {thread.get('title')}")
		print(f"    URL: {thread.get('url')}")
		print(f"    Traffic: {thread.get('estimated_traffic', 0):,}/month")
		print(f"    Priority: {thread.get('priority')}")
		print(f"    Source: {thread.get('source')}")


# ============================================================
# Example 4: Competitive Intelligence
# ============================================================

def example_competitive_intel():
	"""
	Aggregate brand sentiment across multiple threads.
	"""
	print("\n" + "=" * 60)
	print("EXAMPLE 4: Competitive Intelligence")
	print("=" * 60)
	
	data = discover_threads(
		keyword="email marketing software",
		your_brand="MailPro",
		competitors=["Mailchimp", "ConvertKit", "Klaviyo"],
		max_threads=10
	)
	
	# Aggregate sentiment
	brand_stats = defaultdict(lambda: {
		"positive": 0,
		"negative": 0,
		"neutral": 0,
		"praise": [],
		"complaints": []
	})
	
	for thread in data.get("threads", []):
		sentiments = thread.get("analysis", {}).get("brand_sentiments", {})
		
		for brand, sentiment in sentiments.items():
			brand_stats[brand]["positive"] += sentiment.get("positive", 0)
			brand_stats[brand]["negative"] += sentiment.get("negative", 0)
			brand_stats[brand]["neutral"] += sentiment.get("neutral", 0)
			brand_stats[brand]["praise"].extend(sentiment.get("praise", []))
			brand_stats[brand]["complaints"].extend(sentiment.get("complaints", []))
	
	print("\nBrand Sentiment Summary:")
	
	for brand, stats in brand_stats.items():
		total = stats["positive"] + stats["negative"] + stats["neutral"]
		if total == 0:
			continue
		
		positive_rate = round((stats["positive"] / total) * 100)
		
		print(f"\n  {brand}:")
		print(f"    Mentions: {total} ({positive_rate}% positive)")
		print(f"    +{stats['positive']} / -{stats['negative']} / ~{stats['neutral']}")
		
		if stats["praise"]:
			unique_praise = list(set(stats["praise"]))[:3]
			print(f"    Praise: {', '.join(unique_praise)}")
		
		if stats["complaints"]:
			unique_complaints = list(set(stats["complaints"]))[:3]
			print(f"    Complaints: {', '.join(unique_complaints)}")


# ============================================================
# Example 5: Find Opportunities
# ============================================================

def example_find_opportunities():
	"""
	Find high-traffic threads where your brand is missing.
	"""
	print("\n" + "=" * 60)
	print("EXAMPLE 5: Find Opportunities")
	print("=" * 60)
	
	your_brand = "Acme CRM"
	competitors = ["HubSpot", "Salesforce", "Pipedrive"]
	
	data = discover_threads(
		keyword="best crm for startups",
		your_brand=your_brand,
		competitors=competitors,
		max_threads=10
	)
	
	# Find threads where competitors appear but you don't
	opportunities = []
	
	for thread in data.get("threads", []):
		brands = thread.get("analysis", {}).get("brand_sentiments", {})
		has_competitors = any(c in brands for c in competitors)
		has_your_brand = your_brand in brands
		high_traffic = thread.get("estimated_traffic", 0) > 500
		
		if has_competitors and not has_your_brand and high_traffic:
			opportunities.append(thread)
	
	print(f"\nFound {len(opportunities)} opportunity threads:")
	
	for i, thread in enumerate(opportunities, 1):
		brands_mentioned = list(thread.get("analysis", {}).get("brand_sentiments", {}).keys())
		
		print(f"\n  {i}. {thread.get('title')}")
		print(f"     Traffic: {thread.get('estimated_traffic', 0):,}/month")
		print(f"     Competitors: {', '.join(brands_mentioned)}")
		print(f"     URL: {thread.get('url')}")


# ============================================================
# Run All Examples
# ============================================================

if __name__ == "__main__":
	print("\nRedRanks SEO Intelligence API - Python Examples")
	print("Tutorials: https://www.redranks.com/tutorials/\n")
	
	try:
		example_keyword_research()
		example_serp_analysis()
		example_discussion_discovery()
		example_competitive_intel()
		example_find_opportunities()
		
		print("\n" + "=" * 60)
		print("All examples completed!")
		print("=" * 60)
		
	except requests.exceptions.HTTPError as e:
		print(f"\nAPI Error: {e}")
		print("Check your API key and try again.")
	except Exception as e:
		print(f"\nError: {e}")
