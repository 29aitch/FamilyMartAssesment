import requests
import pandas as pd
import time

API_KEY = ""
BRANDS = ["Starbucks", "McDonald's", "CU"]
REGION = "MY"
MAX_RESULTS = 60


def get_places(brand):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"{brand} in Malaysia",
        "region": REGION,
        "key": API_KEY
    }
    response = requests.get(url, params=params).json()
    places = response.get("results", [])


    while "next_page_token" in response and len(places) < MAX_RESULTS:
        params["pagetoken"] = response["next_page_token"]
        time.sleep(2)
        response = requests.get(url, params=params).json()
        places.extend(response.get("results", []))

    return places[:MAX_RESULTS]


data = []
for brand in BRANDS:
    places = get_places(brand)
    for place in places:
        data.append({
            "Brand": brand,
            "Store Name": place.get("name", "N/A"),
            "Address": place.get("formatted_address", "N/A"),
            "Latitude": place["geometry"]["location"]["lat"] if "geometry" in place else "N/A",
            "Longitude": place["geometry"]["location"]["lng"] if "geometry" in place else "N/A"
        })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("store_locations.csv", index=False)
print(f"Saved {len(df)} entries!")