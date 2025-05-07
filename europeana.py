import requests
import csv
import os

EUROPEANA_API_KEY = os.getenv('EUROPEANA_API_KEY')
print(EUROPEANA_API_KEY)

QUERY = 'renaissance painting'
URL = f'https://api.europeana.eu/record/v2/search.json?wskey={EUROPEANA_API_KEY}&query={QUERY}&reusability=all'

response = requests.get(URL)
results = response.json().get('items', [])

with open('data/europeana_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['paintingLabel', 'artistLabel', 'locationLabel', 'locationCoord', 'year', 'image'])

    for item in results:
        title = item.get('title', [''])[0]
        artist = item.get('dcCreator', [''])[0]
        location = item.get('dataProvider', '')
        coord = ''  # Europeana doesn't provide this directly
        year = item.get('timestamp_created', '')[:4] if item.get('timestamp_created') else ''
        image = item.get('edmPreview', [''])[0] if item.get('edmPreview') else ''
        
        writer.writerow([title, artist, location, coord, year, image])