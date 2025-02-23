# Store Location Scraper using Google Places API

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Google Places API](https://img.shields.io/badge/Google_Places_API-Yes-green)

A Python script to retrieve store locations for Starbucks, McDonald's, and CU in Malaysia using Google Places API.

## 📋 Overview
This script queries the Google Places API to fetch store locations (name, address, coordinates) for specified brands in Malaysia. Results are saved to `store_locations.csv`.

## 🛠 Approach
1. **API Integration**: Uses Google Places Text Search API to find stores
2. **Pagination Handling**: Implements `next_page_token` to retrieve up to 60 results per brand
3. **Data Safety**: Gracefully handles missing data fields with "N/A" fallbacks
4. **Efficiency**: Processes data in-memory before CSV export

## 💻 Technologies Used
| Technology       | Purpose                          |
|------------------|----------------------------------|
| Python 3.10      | Core scripting language          |
| Requests         | API interactions                 |
| Pandas           | Data manipulation & CSV export   |
| Google Places API| Location data retrieval          |

## 🚀 Steps to Reproduce

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/29aitch/FamilyMartAssesment
   cd <repository_directory>
   
2. **Get API Key**
   - Create project at [Google Cloud Console](https://console.cloud.google.com/)
   - Enable "Places API"
   - Create API key under "Credentials"

3. **Configure Script**
   ```python
   API_KEY = "YOUR_API_KEY_HERE"  # Replace with your key
Install Dependencies

      ```bash
         pip install requests pandas
Run Script

    ```bash
       python store_scraper.py

Output:
Results saved to store_locations.csv
Columns: Brand, Store Name, Address, Latitude, Longitude

🚨 Challenges & Solutions
Challenge	Solution
API Rate Limits	2-second delay between requests
Missing Location Data	Fallback to "N/A" values
Pagination Complexity	next_page_token implementation

⚠ Important Notes
Free tier allows ~1,000 daily requests

Add error handling for production use

Not affiliated with Google or the brands listed

