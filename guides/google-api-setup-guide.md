# Google API Setup Guide for Content Marketing Assistant

## 🎯 **Overview**
We'll set up Google APIs to enable trend analysis, web search, and content research capabilities in our AI agent.

## 📋 **Required APIs**
1. **Custom Search JSON API** - Web search functionality
2. **YouTube Data API v3** - Video content analysis
3. **Google Trends** - Trend analysis (via pytrends library)

## 🚀 **Step 1: Create Google Cloud Project**

### **1.1 Go to Google Cloud Console**
- Open: https://console.cloud.google.com/
- Sign in with your Google account

### **1.2 Create New Project**
1. Click "Select a project" dropdown (top left)
2. Click "New Project"
3. **Project name**: `content-marketing-assistant`
4. **Organization**: Leave as default
5. Click "Create"

### **1.3 Wait for Project Creation**
- Takes 30-60 seconds
- You'll get a notification when ready

## 🔑 **Step 2: Enable APIs**

### **2.1 Enable Custom Search API**
1. In Cloud Console, go to "APIs & Services" → "Library"
2. Search for "Custom Search API"
3. Click on "Custom Search JSON API"
4. Click "Enable"

### **2.2 Enable YouTube Data API**
1. In the same Library, search for "YouTube Data API v3"
2. Click on "YouTube Data API v3"
3. Click "Enable"

### **2.3 Enable additional APIs (optional)**
- Google Search Console API
- Google Analytics Reporting API
- Google My Business API

## 🗝️ **Step 3: Create API Credentials**

### **3.1 Create API Key**
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "API Key"
3. **Copy the API key** - you'll need this!
4. Click "Restrict Key" (recommended)

### **3.2 Restrict API Key (Security)**
1. **Name**: `content-marketing-assistant-key`
2. **Application restrictions**: 
   - Select "IP addresses"
   - Add your current IP (or leave unrestricted for development)
3. **API restrictions**:
   - Select "Restrict key"
   - Choose:
     - Custom Search JSON API
     - YouTube Data API v3
4. Click "Save"

## 🔍 **Step 4: Set Up Custom Search Engine**

### **4.1 Create Custom Search Engine**
1. Go to: https://cse.google.com/cse/
2. Click "Add" or "Create"
3. **Sites to search**: `*` (to search entire web)
4. **Language**: English
5. **Name**: `Content Marketing Search`
6. Click "Create"

### **4.2 Get Search Engine ID**
1. Click on your new search engine
2. Click "Control Panel"
3. **Copy the Search Engine ID** - you'll need this!

### **4.3 Enable Image Search (optional)**
1. In Control Panel, go to "Look and feel"
2. Enable "Image search"
3. Click "Save"

## 🧪 **Step 5: Test Your APIs**

### **5.1 Test Custom Search API**
Open Terminal and run:
```bash
# Replace YOUR_API_KEY and YOUR_CSE_ID with your actual values
curl "https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_CSE_ID&q=artificial+intelligence+trends"
```

### **5.2 Test YouTube API**
```bash
# Replace YOUR_API_KEY with your actual API key
curl "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q=content+marketing+trends&key=YOUR_API_KEY"
```

## 📝 **Step 6: Update Your .env File**

Add these to your `.env` file:
```env
# Google API Configuration
GOOGLE_API_KEY=your_actual_api_key_here
GOOGLE_CSE_ID=your_search_engine_id_here

# YouTube API (same key as above)
YOUTUBE_API_KEY=your_actual_api_key_here
```

## 💡 **Important Notes**

### **API Quotas & Limits**
- **Custom Search**: 100 queries/day (free)
- **YouTube Data**: 10,000 units/day (free)
- **Google Trends**: No API key needed (uses pytrends)

### **Cost Management**
- Free tier is generous for development
- Set up billing alerts in Google Cloud Console
- Monitor usage in "APIs & Services" → "Quotas"

### **Security Best Practices**
- Restrict API keys to specific IPs in production
- Use separate keys for different environments
- Monitor API usage regularly
- Enable API key restrictions

## 🔧 **Troubleshooting**

### **Common Issues**
1. **"API not enabled"**: Go back to Library and enable the API
2. **"Invalid API key"**: Check key is copied correctly
3. **"Quota exceeded"**: Wait 24 hours or enable billing
4. **"Access denied"**: Check API key restrictions

### **Testing Commands**
```bash
# Test if curl is working
curl --version

# Test basic Google API connectivity
curl "https://www.googleapis.com/customsearch/v1?key=test&cx=test&q=test"
# Should return an error about invalid key (that's expected)
```

## 🎯 **Next Steps**
Once you have your API keys:
1. Update your `.env` file with real values
2. Test the APIs using the curl commands above
3. We'll integrate these into our Python code in Step 2!

## 📞 **Need Help?**
If you encounter any issues:
- Check the Google Cloud Console for error messages
- Verify your project has the APIs enabled
- Make sure billing is set up (even for free tier)
- Double-check API key restrictions