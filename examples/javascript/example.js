/**
 * Reddit Traffic and Intelligence API - JavaScript Example
 * 
 * Find Reddit threads ranking on Google with traffic estimates and brand sentiment.
 * 
 * Get your API key:
 *     Zyla:     https://zylalabs.com/api-marketplace/other/reddit+traffic+plus+intelligence+api/11553
 *     RapidAPI: https://rapidapi.com/greg01060/api/reddit-traffic-and-intelligence-api
 */

// ============================================================
// Configuration - Choose your provider
// ============================================================

// Option 1: Zyla API Hub (recommended)
const PROVIDER = 'zyla';
const ZYLA_API_KEY = 'YOUR_ZYLA_API_KEY'; // Replace with your key

// Option 2: RapidAPI
// const PROVIDER = 'rapidapi';
// const RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'; // Replace with your key

// ============================================================

function getHeaders() {
	if (PROVIDER === 'zyla') {
		return {
			'Authorization': `Bearer ${ZYLA_API_KEY}`,
			'Content-Type': 'application/json'
		};
	} else {
		return {
			'X-RapidAPI-Key': RAPIDAPI_KEY,
			'X-RapidAPI-Host': 'reddit-traffic-and-intelligence-api.p.rapidapi.com',
			'Content-Type': 'application/json'
		};
	}
}

function getBaseUrl() {
	if (PROVIDER === 'zyla') {
		return 'https://zylalabs.com/api/5765/reddit+traffic+plus+intelligence+api/11553';
	} else {
		return 'https://reddit-traffic-and-intelligence-api.p.rapidapi.com/api/v2';
	}
}

/**
 * Discover Reddit threads ranking on Google for a keyword
 */
async function discoverThreads(keyword, options = {}) {
	const endpoint = PROVIDER === 'zyla' ? 'discover+threads' : 'discover-threads';
	
	const response = await fetch(
		`${getBaseUrl()}/${endpoint}`,
		{
			method: 'POST',
			headers: getHeaders(),
			body: JSON.stringify({
				keyword,
				your_brand: options.yourBrand || null,
				competitors: options.competitors || null,
				max_threads: options.maxThreads || 10,
				max_comments_per_thread: options.maxComments || 5,
				data_freshness: options.freshness || 'balanced'
			})
		}
	);

	if (!response.ok) {
		throw new Error(`API error: ${response.status}`);
	}

	return response.json();
}

/**
 * Example: Basic keyword search
 */
async function exampleBasicSearch() {
	console.log('--- Basic Search ---\n');
	
	const data = await discoverThreads('project management software');
	
	console.log(`Keyword: ${data.keyword}`);
	console.log(`Search Volume: ${data.keyword_metrics?.volume?.toLocaleString()}/month`);
	console.log(`Threads Found: ${data.threads_discovered}`);
	console.log(`Total Traffic: ${data.summary?.estimated_monthly_traffic?.toLocaleString()}/month\n`);
	
	// Show top threads
	data.threads?.slice(0, 3).forEach((thread, i) => {
		console.log(`${i + 1}. ${thread.title}`);
		console.log(`   URL: ${thread.url}`);
		console.log(`   Traffic: ${thread.estimated_traffic?.toLocaleString()}/month`);
		console.log(`   Priority: ${thread.priority}\n`);
	});
}

/**
 * Example: Competitive intelligence with brand tracking
 */
async function exampleCompetitiveIntel() {
	console.log('--- Competitive Intelligence ---\n');
	
	const data = await discoverThreads('CRM software', {
		yourBrand: 'Acme CRM',
		competitors: ['HubSpot', 'Salesforce', 'Pipedrive'],
		maxThreads: 5
	});
	
	// Aggregate brand sentiment across all threads
	const brandStats = {};
	
	data.threads?.forEach(thread => {
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
	});
	
	// Display results
	console.log('Brand Sentiment Summary:\n');
	
	for (const [brand, stats] of Object.entries(brandStats)) {
		const total = stats.positive + stats.negative + stats.neutral;
		const positiveRate = total > 0 ? Math.round((stats.positive / total) * 100) : 0;
		
		console.log(`${brand}:`);
		console.log(`  Mentions: ${total} (${positiveRate}% positive)`);
		console.log(`  +${stats.positive} / -${stats.negative} / ~${stats.neutral}`);
		
		if (stats.praise.length > 0) {
			const uniquePraise = [...new Set(stats.praise)].slice(0, 3);
			console.log(`  Praise: ${uniquePraise.join(', ')}`);
		}
		
		if (stats.complaints.length > 0) {
			const uniqueComplaints = [...new Set(stats.complaints)].slice(0, 3);
			console.log(`  Complaints: ${uniqueComplaints.join(', ')}`);
		}
		
		console.log('');
	}
}

/**
 * Example: Find high-traffic opportunities
 */
async function exampleFindOpportunities() {
	console.log('--- High-Traffic Opportunities ---\n');
	
	const data = await discoverThreads('email marketing', {
		yourBrand: 'MailPro',
		competitors: ['Mailchimp', 'ConvertKit', 'Klaviyo'],
		maxThreads: 10
	});
	
	// Find threads where competitors are mentioned but your brand isn't
	const opportunities = data.threads?.filter(thread => {
		const brands = thread.analysis?.brand_sentiments || {};
		const hasCompetitors = Object.keys(brands).some(b => 
			['Mailchimp', 'ConvertKit', 'Klaviyo'].includes(b)
		);
		const hasYourBrand = 'MailPro' in brands;
		
		return hasCompetitors && !hasYourBrand && thread.estimated_traffic > 1000;
	});
	
	console.log(`Found ${opportunities?.length || 0} opportunity threads:\n`);
	
	opportunities?.forEach((thread, i) => {
		console.log(`${i + 1}. ${thread.title}`);
		console.log(`   URL: ${thread.url}`);
		console.log(`   Traffic: ${thread.estimated_traffic?.toLocaleString()}/month`);
		console.log(`   Competitors mentioned: ${Object.keys(thread.analysis?.brand_sentiments || {}).join(', ')}`);
		console.log('');
	});
}

// Run examples
(async () => {
	console.log(`\nUsing provider: ${PROVIDER.toUpperCase()}\n`);
	
	try {
		await exampleBasicSearch();
		console.log('\n' + '='.repeat(50) + '\n');
		
		await exampleCompetitiveIntel();
		console.log('\n' + '='.repeat(50) + '\n');
		
		await exampleFindOpportunities();
	} catch (error) {
		console.error('Error:', error.message);
	}
})();
