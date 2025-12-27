/**
 * RedRanks SEO Intelligence API - JavaScript Examples
 * 
 * Automate SEO with JavaScript. Keyword research, SERP analysis, and discussion discovery.
 * 
 * Get your API key:
 *     https://rapidapi.com/greg01060/api/redranks-seo-intelligence-api
 * 
 * Tutorials:
 *     https://www.redranks.com/tutorials/
 */

// ============================================================
// Configuration
// ============================================================

const RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'; // Replace with your key

const HEADERS = {
	'X-RapidAPI-Key': RAPIDAPI_KEY,
	'X-RapidAPI-Host': 'reddit-traffic-and-intelligence-api.p.rapidapi.com',
	'Content-Type': 'application/json'
};

const BASE_URL = 'https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2';

// ============================================================
// API Functions
// ============================================================

/**
 * Get keyword metrics: volume, CPC, difficulty, and related keywords.
 * Tutorial: https://www.redranks.com/tutorials/keyword-research-python.html
 */
async function keywordMetrics(keywords, options = {}) {
	const response = await fetch(`${BASE_URL}/keyword-metrics`, {
		method: 'POST',
		headers: HEADERS,
		body: JSON.stringify({
			keywords,
			include_related: options.includeRelated || false,
			max_related: options.maxRelated || 5
		})
	});

	if (!response.ok) {
		throw new Error(`API error: ${response.status}`);
	}

	return response.json();
}

/**
 * Analyze SERP for a keyword. Detect features and find discussion positions.
 * Tutorial: https://www.redranks.com/tutorials/serp-analysis-python.html
 */
async function serpAnalysis(keyword, options = {}) {
	const response = await fetch(`${BASE_URL}/serp-analysis`, {
		method: 'POST',
		headers: HEADERS,
		body: JSON.stringify({
			keyword,
			include_features: options.includeFeatures !== false,
			max_results: options.maxResults || 10
		})
	});

	if (!response.ok) {
		throw new Error(`API error: ${response.status}`);
	}

	return response.json();
}

/**
 * Discover Reddit threads ranking on Google with traffic and sentiment.
 * Tutorial: https://www.redranks.com/tutorials/reddit-discussion-discovery.html
 */
async function discoverThreads(keyword, options = {}) {
	const response = await fetch(`${BASE_URL}/discover-threads`, {
		method: 'POST',
		headers: HEADERS,
		body: JSON.stringify({
			keyword,
			your_brand: options.yourBrand || null,
			competitors: options.competitors || null,
			max_threads: options.maxThreads || 10,
			max_comments_per_thread: options.maxComments || 5,
			data_freshness: options.freshness || 'balanced'
		})
	});

	if (!response.ok) {
		throw new Error(`API error: ${response.status}`);
	}

	return response.json();
}

// ============================================================
// Example 1: Keyword Research
// ============================================================

async function exampleKeywordResearch() {
	console.log('='.repeat(60));
	console.log('EXAMPLE 1: Keyword Research');
	console.log('='.repeat(60));

	const keywords = ['crm software', 'project management', 'help desk software'];

	const data = await keywordMetrics(keywords, {
		includeRelated: true,
		maxRelated: 5
	});

	for (const kw of data.keywords || []) {
		console.log(`\n${kw.keyword.toUpperCase()}`);
		console.log(`  Volume: ${kw.volume?.toLocaleString()}/month`);
		console.log(`  CPC: $${kw.cpc?.toFixed(2)}`);
		console.log(`  Difficulty: ${kw.keyword_difficulty}/100`);
		console.log(`  Intent: ${kw.search_intent}`);

		if (kw.related_keywords?.length > 0) {
			console.log('  Related keywords:');
			for (const r of kw.related_keywords.slice(0, 3)) {
				console.log(`    - ${r.keyword} (${r.volume?.toLocaleString()}/mo)`);
			}
		}
	}
}

// ============================================================
// Example 2: SERP Analysis
// ============================================================

async function exampleSerpAnalysis() {
	console.log('\n' + '='.repeat(60));
	console.log('EXAMPLE 2: SERP Analysis');
	console.log('='.repeat(60));

	const keyword = 'best crm software';

	const data = await serpAnalysis(keyword, { maxResults: 10 });

	console.log(`\nKeyword: ${data.keyword}`);

	// SERP Features
	const features = data.serp_features || {};
	console.log('\nSERP Features Detected:');
	console.log(`  AI Overview: ${features.has_ai_overview ? 'Yes' : 'No'}`);
	console.log(`  Discussion Box: ${features.has_discussion_box ? 'Yes' : 'No'}`);
	console.log(`  Featured Snippet: ${features.has_featured_snippet ? 'Yes' : 'No'}`);
	console.log(`  People Also Ask: ${features.has_people_also_ask ? 'Yes' : 'No'}`);

	// Discussion positions
	console.log(`\nDiscussions at positions: ${data.discussion_positions || []}`);

	// Top results
	console.log('\nTop 5 Organic Results:');
	for (const result of (data.organic_results || []).slice(0, 5)) {
		const discMarker = result.is_discussion ? ' [DISCUSSION]' : '';
		console.log(`  ${result.position}. ${result.domain}${discMarker}`);
	}
}

// ============================================================
// Example 3: Discussion Discovery
// ============================================================

async function exampleDiscussionDiscovery() {
	console.log('\n' + '='.repeat(60));
	console.log('EXAMPLE 3: Discussion Discovery');
	console.log('='.repeat(60));

	const data = await discoverThreads('CRM software', {
		yourBrand: 'Acme CRM',
		competitors: ['HubSpot', 'Salesforce', 'Pipedrive'],
		maxThreads: 5
	});

	console.log(`\nKeyword: ${data.keyword}`);

	// Keyword metrics
	const metrics = data.keyword_metrics || {};
	console.log(`Search Volume: ${metrics.volume?.toLocaleString()}/month`);

	// Summary
	const summary = data.summary || {};
	console.log(`Threads Found: ${summary.total_threads}`);
	console.log(`Total Traffic: ${summary.estimated_monthly_traffic?.toLocaleString()}/month`);

	// Top threads
	console.log('\nTop Threads:');
	for (const thread of (data.threads || []).slice(0, 3)) {
		console.log(`\n  ${thread.title}`);
		console.log(`    URL: ${thread.url}`);
		console.log(`    Traffic: ${thread.estimated_traffic?.toLocaleString()}/month`);
		console.log(`    Priority: ${thread.priority}`);
		console.log(`    Source: ${thread.source}`);
	}
}

// ============================================================
// Example 4: Competitive Intelligence
// ============================================================

async function exampleCompetitiveIntel() {
	console.log('\n' + '='.repeat(60));
	console.log('EXAMPLE 4: Competitive Intelligence');
	console.log('='.repeat(60));

	const data = await discoverThreads('email marketing software', {
		yourBrand: 'MailPro',
		competitors: ['Mailchimp', 'ConvertKit', 'Klaviyo'],
		maxThreads: 10
	});

	// Aggregate sentiment
	const brandStats = {};

	for (const thread of data.threads || []) {
		const sentiments = thread.analysis?.brand_sentiments || {};

		for (const [brand, sentiment] of Object.entries(sentiments)) {
			if (!brandStats[brand]) {
				brandStats[brand] = {
					positive: 0,
					negative: 0,
					neutral: 0,
					praise: [],
					complaints: []
				};
			}

			brandStats[brand].positive += sentiment.positive || 0;
			brandStats[brand].negative += sentiment.negative || 0;
			brandStats[brand].neutral += sentiment.neutral || 0;

			if (sentiment.praise) {
				brandStats[brand].praise.push(...sentiment.praise);
			}
			if (sentiment.complaints) {
				brandStats[brand].complaints.push(...sentiment.complaints);
			}
		}
	}

	console.log('\nBrand Sentiment Summary:');

	for (const [brand, stats] of Object.entries(brandStats)) {
		const total = stats.positive + stats.negative + stats.neutral;
		if (total === 0) continue;

		const positiveRate = Math.round((stats.positive / total) * 100);

		console.log(`\n  ${brand}:`);
		console.log(`    Mentions: ${total} (${positiveRate}% positive)`);
		console.log(`    +${stats.positive} / -${stats.negative} / ~${stats.neutral}`);

		if (stats.praise.length > 0) {
			const uniquePraise = [...new Set(stats.praise)].slice(0, 3);
			console.log(`    Praise: ${uniquePraise.join(', ')}`);
		}

		if (stats.complaints.length > 0) {
			const uniqueComplaints = [...new Set(stats.complaints)].slice(0, 3);
			console.log(`    Complaints: ${uniqueComplaints.join(', ')}`);
		}
	}
}

// ============================================================
// Example 5: Find Opportunities
// ============================================================

async function exampleFindOpportunities() {
	console.log('\n' + '='.repeat(60));
	console.log('EXAMPLE 5: Find Opportunities');
	console.log('='.repeat(60));

	const yourBrand = 'Acme CRM';
	const competitors = ['HubSpot', 'Salesforce', 'Pipedrive'];

	const data = await discoverThreads('best crm for startups', {
		yourBrand,
		competitors,
		maxThreads: 10
	});

	// Find threads where competitors appear but you don't
	const opportunities = (data.threads || []).filter(thread => {
		const brands = thread.analysis?.brand_sentiments || {};
		const hasCompetitors = competitors.some(c => c in brands);
		const hasYourBrand = yourBrand in brands;
		const highTraffic = thread.estimated_traffic > 500;

		return hasCompetitors && !hasYourBrand && highTraffic;
	});

	console.log(`\nFound ${opportunities.length} opportunity threads:`);

	opportunities.forEach((thread, i) => {
		const brandsMentioned = Object.keys(thread.analysis?.brand_sentiments || {});

		console.log(`\n  ${i + 1}. ${thread.title}`);
		console.log(`     Traffic: ${thread.estimated_traffic?.toLocaleString()}/month`);
		console.log(`     Competitors: ${brandsMentioned.join(', ')}`);
		console.log(`     URL: ${thread.url}`);
	});
}

// ============================================================
// Run All Examples
// ============================================================

(async () => {
	console.log('\nRedRanks SEO Intelligence API - JavaScript Examples');
	console.log('Tutorials: https://www.redranks.com/tutorials/\n');

	try {
		await exampleKeywordResearch();
		await exampleSerpAnalysis();
		await exampleDiscussionDiscovery();
		await exampleCompetitiveIntel();
		await exampleFindOpportunities();

		console.log('\n' + '='.repeat(60));
		console.log('All examples completed!');
		console.log('='.repeat(60));

	} catch (error) {
		console.error('\nError:', error.message);
		console.log('Check your API key and try again.');
	}
})();
