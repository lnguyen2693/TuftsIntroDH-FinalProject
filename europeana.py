import requests
import csv
import os

EUROPEANA_API_KEY = os.getenv('EUROPEANA_API_KEY')
print(EUROPEANA_API_KEY)

QUERY = 'renaissance painting'
URL = f'https://api.europeana.eu/record/v2/search.json?wskey={EUROPEANA_API_KEY}&query={QUERY}&reusability=all'

response = requests.get(URL)
results = response.json().get('items', [])

print(response)