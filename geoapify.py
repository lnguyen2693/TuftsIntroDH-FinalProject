import requests
import os

GEOAPIFY_API_KEY = os.getenv('GEOAPIFY_API_KEY')
EUROPEANA_API_KEY = os.getenv('EUROPEANA_API_KEY')
print(GEOAPIFY_API_KEY)
print(EUROPEANA_API_KEY)

# This function return the corresponding geocode of a location
# def geocoding_from_location(loc: str):
#     loc_string = loc.replace(" ", "%20")
#     print(loc_string)
#     url = "https://api.geoapify.com/v1/geocode/search?text={loc_string}&format=json&apiKey={GEOAPIFY_API_KEY}"
          
#     response = requests.get(url)
#     print(response.json())

# geocoding_from_location("Sylter Heimatmuseum")