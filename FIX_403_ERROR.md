# FIXING 403 FORBIDDEN ERROR

## The Problem
API key works, but Custom Search API isn't enabled on your project.

## Solution:

### 1. Enable Custom Search API
- Go to: https://console.cloud.google.com/apis/library
- In the search bar, type: **"Custom Search API"** (or "Custom Search JSON API")
- Click on "Custom Search API" in the results
- Click the blue **"ENABLE"** button
- Wait 30 seconds for it to activate

### 2. OR Use This Direct Link
https://console.cloud.google.com/apis/library/customsearch.googleapis.com

Click ENABLE on that page.

### 3. Verify It's Enabled
- Go to: https://console.cloud.google.com/apis/dashboard
- Look for "Custom Search API" or "Custom Search JSON API" in your enabled APIs list
- Should show as "Enabled"

### 4. Test Again
Wait 1-2 minutes, then:
```bash
cd /media/palmerschallon/ThePod1
python3 web_search.py "test query"
```

---

## If Still Getting 403:

### Check Billing
Google requires a billing account (even for free tier):
- Go to: https://console.cloud.google.com/billing
- Link a credit card (you won't be charged for the 100 free queries/day)
- Free tier is truly free, but Google requires payment method on file

### Check Quotas
- Go to: https://console.cloud.google.com/apis/api/customsearch.googleapis.com/quotas
- Make sure you have quota available (100/day default)

---

**Most likely: Just need to enable the Custom Search API in the APIs Library.** 🔥

