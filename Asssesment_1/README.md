{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\froman\fcharset0 Times-Bold;\f2\froman\fcharset0 Times-Roman;
\f3\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat2\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid1\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid2\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid101\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid2}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf0 \expnd0\expndtw0\kerning0
# Store Locations Scraper using Google Places API\
\
## Overview\
\
This project retrieves store location data for selected brands in Malaysia by leveraging the Google Places API. The script sends text search queries for each brand (e.g., Starbucks, McDonald's, CU), manages paginated responses to collect up to 60 results per brand, and extracts essential details such as store name, address, and geographic coordinates. Finally, the data is compiled into a CSV file for analysis.\
\
## Approach\
\
The solution is implemented as follows:\
\
1. **API Request Setup:**\
   - The script constructs a request to the Google Places API by combining the brand name with a location filter ("in Malaysia"), specifying the region, and including an API key.\
   - The `requests` library is used to perform the HTTP GET request.\
\
2. **Handling Pagination:**\
   - The Google Places API often returns a `next_page_token` when additional results are available. The script checks for this token and, if present, waits for 2 seconds (ensuring the token becomes active) before fetching more results.\
   - This loop continues until the script has accumulated the desired maximum number of results (`MAX_RESULTS`).\
\
3. **Data Extraction:**\
   - For each API response, the script extracts key details like store name, formatted address, and location coordinates.\
   - Conditional checks ensure that if some expected fields (e.g., `geometry` or `formatted_address`) are missing, a default value ("N/A") is assigned.\
\
4. **Data Storage:**\
   - The extracted data is stored in a list, then converted into a Pandas DataFrame.\
   - The DataFrame is written to a CSV file (`store_locations.csv`), making the data easily accessible for further analysis.\
\
### Why We Didn\'92t Use a Python Library like BeautifulSoup\
\
BeautifulSoup is a powerful tool for web scraping and parsing HTML content from web pages. However, in this project, we are working with a structured API that returns data in JSON format. This makes the use of BeautifulSoup unnecessary because:\
- **Direct API Access:** The Google Places API provides the data directly in a structured JSON format, eliminating the need to parse HTML.\
- **Simplicity and Efficiency:** Using the `requests` library to interact with the API and then processing the JSON response is more straightforward and efficient than extracting data from HTML.\
- **Reliability:** APIs are designed to provide clean, consistent data, whereas scraping HTML pages can be more error-prone due to changes in webpage structure.\
- **Performance:** Processing JSON responses is generally faster and uses less memory compared to parsing HTML content with BeautifulSoup.\
\
## Technologies and Tools Used\
\
- **Python:** The core programming language.\
- **Requests:** For making HTTP calls to the Google Places API.\
- **Pandas:** For data manipulation and exporting the results to a CSV file.\
- **Time:** To handle delays between API requests, ensuring proper token activation.\
- **Google Places API:** Provides the necessary location-based data.\
  \
## Steps to Reproduce the Results\
\
 1 	**Clone the Repository:**\
  	 bash\
  	 git clone <repository_url>\
  	 cd <repository_directory>\
\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0
\f1\fs24 \cf0 \kerning1\expnd0\expndtw0 {\listtext	2	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Install Dependencies:
\f2\b0  Ensure you have Python 3.x installed. Then, install the required packages:\uc0\u8232 
\f3\fs26 bash\uc0\u8232 pip install requests pandas\u8232 \u8232 
\f2\fs24 \
\ls1\ilvl0
\f1\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Configure API Key:
\f2\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls1\ilvl1\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Open the script file (e.g., 
\f3\fs26 main.py
\f2\fs24 ).\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Replace the placeholder 
\f3\fs26 API_KEY = ""
\f2\fs24  with your valid Google Places API key:
\f3\fs26 python\uc0\u8232 \u8232 API_KEY = "YOUR_GOOGLE_PLACES_API_KEY"\
\uc0\u8232 
\f2\fs24 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0
\f1\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	4	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Run the Script:
\f2\b0  Execute the script to start fetching data:\uc0\u8232 
\f3\fs26 bash\uc0\u8232 python main.py
\f2\fs24 \
\ls1\ilvl0
\f1\b {\listtext	5	}The script will:
\f2\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls1\ilvl1\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Query the Google Places API for each brand specified in the 
\f3\fs26 BRANDS
\f2\fs24  list.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Handle pagination to gather up to 60 results per brand.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Save the collected data to 
\f3\fs26 store_locations.csv
\f2\fs24 .\
\ls1\ilvl1
\f1\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\
\ls1\ilvl1\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Review the Results:
\f2\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls1\ilvl1\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Open 
\f3\fs26 store_locations.csv
\f2\fs24  to verify that the store location data has been correctly extracted and stored.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 The CSV file includes columns for Brand, Store Name, Address, Latitude, and Longitude.\
\pard\tx720\tx1440\pardeftab720\partightenfactor0
\cf0 \
\
\pard\pardeftab720\sa298\partightenfactor0

\f1\b\fs36 \cf0 Encountered Challenges and Resolutions\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0
\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 API Rate Limiting and Token Activation:
\f2\b0 \uc0\u8232 The Google Places API sometimes delays the activation of the 
\f3\fs26 next_page_token
\f2\fs24 . A fixed 2-second delay was implemented before making paginated requests. This value was fine-tuned based on initial tests to balance between waiting long enough for the token to be valid and maintaining a reasonable runtime.\
\ls2\ilvl0
\f1\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Incomplete Data Fields:
\f2\b0 \uc0\u8232 Some API responses did not include certain fields (like 
\f3\fs26 formatted_address
\f2\fs24  or 
\f3\fs26 geometry
\f2\fs24 ), which could potentially break the data extraction logic. This was handled by implementing conditional checks that substitute missing data with "N/A", ensuring consistency in the output.\
\ls2\ilvl0
\f1\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	4	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Avoiding Unnecessary Tools:
\f2\b0 \uc0\u8232 Although libraries like BeautifulSoup are excellent for web scraping, they were not needed in this project because the API returns structured JSON data. This helped streamline the development process and reduced the complexity of the code.\
\pard\pardeftab720\sa298\partightenfactor0

\f1\b\fs36 \cf0 \
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \outl0\strokewidth0 \
}