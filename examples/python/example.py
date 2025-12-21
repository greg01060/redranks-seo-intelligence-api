"""
Reddit Traffic and Intelligence API - Python Example

Find Reddit threads ranking on Google with traffic estimates and brand sentiment.

Get your API key:
    Zyla:     https://zylalabs.com/api-marketplace/other/reddit+traffic+plus+intelligence+api/11553
    RapidAPI: https://rapidapi.com/greg01060/api/reddit-traffic-and-intelligence-api

Requirements:
    pip install requests
"""

import requests
from typing import Optional
from collections import defaultdict

# ============================================================
# Configuration - Choose your provider
# ============================================================

# Option 1: Zyla API Hub (recommended)
PROVIDER = "zyla"
ZYLA_API_KEY = "YOUR_ZYLA_API_KEY"  # Replace with your key

# Option 2: RapidAPI
# PROVIDER = "rapidapi"
# RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"  # Replace with your key

# ============================================================


def get_headers():
	"""Get headers based on provider"""
	if PROVIDER == "zyla":
		return {
			"Authorization": f"Bearer {ZYLA_API_KEY}",
			"Content-Type": "application/json"
		}
	else:
		return {
			"X-RapidAPI-Key": RAPIDAPI_KEY,
			"X-RapidAPI-Host": "reddit-traffic-and-intelligence-api.p.rapidapi.com",
			"Content-Type": "application/json"
		}


def get_base_url():
	"""Get base URL based on provider"""
	if PROVIDER == "zyla":
		return "https://zylalabs.com/api/5765/reddit+traffic+plus+intelligence+api/11553"
	else:
		return "https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2"


def discover_threads(
	keyword: str,
	your_brand: Optional[str] = None,
	competitors: Optional[list] = None,
	max_threads: int = 10,
	max_comments: int = 5,
	data_freshness: str = "balanced"
) -> dict:
	"""
	Discover Reddit threads ranking on Google for a keyword.
	
	Args:
		keyword: The search keyword (2-100 characters)
		your_brand: Your brand name for mention analysis
		competitors: List of competitor brand names (max 20)
		max_threads: Number of threads to return (0-20)
		max_comments: Comments per thread (0-20)
		data_freshness: "realtime", "balanced", or "custom"
	
	Returns:
		API response as dictionary
	"""
	endpoint = "discover+threads" if PROVIDER == "zyla" else "discover-threads"
	
	response = requests.post(
		f"{get_base_url()}/{endpoint}",
		headers=get_headers(),
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


def example_basic_search():
	"""Example: Basic keyword search"""
	print("--- Basic Search ---\n")
	
	data = discover_threads("project management software")
	
	print(f"Keyword: {data['keyword']}")
	print(f"Search Volume: {data.get('keyword_metrics', {}).get('volume', 0):,}/month")
	print(f"Threads Found: {data.get('threads_discovered', 0)}")
	print(f"Total Traffic: {data.get('summary', {}).get('estimated_monthly_traffic', 0):,}/month\n")
	
	# Show top threads
	for i, thread in enumerate(data.get("threads", [])[:3], 1):
		print(f"{i}. {thread['title']}")
		print(f"   URL: {thread.get('url', 'N/A')}")
		print(f"   Traffic: {thread.get('estimated_traffic', 0):,}/month")
		print(f"   Priority: {thread.get('priority', 'N/A')}\n")


def example_competitive_intel():
	"""Example: Competitive intelligence with brand tracking"""
	print("--- Competitive Intelligence ---\n")
	
	data = discover_threads(
		keyword="CRM software",
		your_brand="Acme CRM",
		competitors=["HubSpot", "Salesforce", "Pipedrive"],
		max_threads=5
	)
	
	# Aggregate brand sentiment across all threads
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
	
	# Display results
	print("Brand Sentiment Summary:\n")
	
	for brand, stats in brand_stats.items():
		total = stats["positive"] + stats["negative"] + stats["neutral"]
		positive_rate = round((stats["positive"] / total) * 100) if total > 0 else 0
		
		print(f"{brand}:")
		print(f"  Mentions: {total} ({positive_rate}% positive)")
		print(f"  +{stats['positive']} / -{stats['negative']} / ~{stats['neutral']}")
		
		if stats["praise"]:
			unique_praise = list(set(stats["praise"]))[:3]
			print(f"  Praise: {', '.join(unique_praise)}")
		
		if stats["complaints"]:
			unique_complaints = list(set(stats["complaints"]))[:3]
			print(f"  Complaints: {', '.join(unique_complaints)}")
		
		print()


def example_find_opportunities():
	"""Example: Find high-traffic opportunities where your brand is missing"""
	print("--- High-Traffic Opportunities ---\n")
	
	competitors = ["Mailchimp", "ConvertKit", "Klaviyo"]
	your_brand = "MailPro"
	
	data = discover_threads(
		keyword="email marketing",
		your_brand=your_brand,
		competitors=competitors,
		max_threads=10
	)
	
	# Find threads where competitors are mentioned but your brand isn't
	opportunities = []
	
	for thread in data.get("threads", []):
		brands = thread.get("analysis", {}).get("brand_sentiments", {})
		has_competitors = any(b in brands for b in competitors)
		has_your_brand = your_brand in brands
		high_traffic = thread.get("estimated_traffic", 0) > 1000
		
		if has_competitors and not has_your_brand and high_traffic:
			opportunities.append(thread)
	
	print(f"Found {len(opportunities)} opportunity threads:\n")
	
	for i, thread in enumerate(opportunities, 1):
		brands_mentioned = list(thread.get("analysis", {}).get("brand_sentiments", {}).keys())
		
		print(f"{i}. {thread['title']}")
		print(f"   URL: {thread.get('url', 'N/A')}")
		print(f"   Traffic: {thread.get('estimated_traffic', 0):,}/month")
		print(f"   Competitors mentioned: {', '.join(brands_mentioned)}")
		print()


def example_generate_battle_card():
	"""Example: Generate a sales battle card from sentiment data"""
	print("--- Auto-Generated Battle Card ---\n")
	
	data = discover_threads(
		keyword="help desk software",
		your_brand="SupportHub",
		competitors=["Zendesk", "Freshdesk", "Intercom"],
		max_threads=10
	)
	
	# Aggregate competitor data
	competitor_data = defaultdict(lambda: {
		"praise": [],
		"complaints": [],
		"positive": 0,
		"negative": 0
	})
	
	for thread in data.get("threads", []):
		sentiments = thread.get("analysis", {}).get("brand_sentiments", {})
		
		for brand, sentiment in sentiments.items():
			if brand in ["Zendesk", "Freshdesk", "Intercom"]:
				competitor_data[brand]["positive"] += sentiment.get("positive", 0)
				competitor_data[brand]["negative"] += sentiment.get("negative", 0)
				competitor_data[brand]["praise"].extend(sentiment.get("praise", []))
				competitor_data[brand]["complaints"].extend(sentiment.get("complaints", []))
	
	# Generate battle card
	print("=" * 50)
	print("SALES BATTLE CARD - Help Desk Software")
	print("=" * 50)
	
	for competitor, stats in competitor_data.items():
		unique_complaints = list(set(stats["complaints"]))[:5]
		unique_praise = list(set(stats["praise"]))[:3]
		
		if not unique_complaints and not unique_praise:
			continue
		
		print(f"\n## vs {competitor}")
		print("-" * 30)
		
		if unique_praise:
			print(f"Their strengths (prepare defense):")
			for item in unique_praise:
				print(f"  - {item}")
		
		if unique_complaints:
			print(f"\nTheir weaknesses (attack here):")
			for item in unique_complaints:
				print(f"  - {item}")
		
		# Generate positioning suggestion
		if unique_complaints:
			print(f"\nSuggested positioning:")
			print(f'  "Unlike {competitor}, SupportHub {_invert_complaint(unique_complaints[0])}"')


def _invert_complaint(complaint: str) -> str:
	"""Helper to invert a complaint into positive positioning"""
	inversions = {
		"expensive": "offers transparent, predictable pricing",
		"complex": "is simple to set up and use",
		"slow": "delivers fast performance",
		"poor support": "provides responsive customer support",
		"difficult": "is intuitive and easy to learn",
	}
	
	complaint_lower = complaint.lower()
	for key, value in inversions.items():
		if key in complaint_lower:
			return value
	
	return f"addresses the '{complaint}' issue"


if __name__ == "__main__":
	print(f"\nUsing provider: {PROVIDER.upper()}\n")
	print("=" * 50)
	
	example_basic_search()
	
	print("\n" + "=" * 50)
	example_competitive_intel()
	
	print("\n" + "=" * 50)
	example_find_opportunities()
	
	print("\n" + "=" * 50)
	example_generate_battle_card()
