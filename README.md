# Overview
This is a time-aware ArcGIS map using Wikidata database to show the current location of Renaissance paintings (1300–1600), aiming to find out where would be the place having the most Renaissance paintings.

Since the Renaissance paintings were produced mostly in Europe, my initial assumption is Europe countries will have more Renaissance paintings than that of other countries. 

Due to time limitation, this project will focus on 2 main sources of data: Wikipedia and Europeana. 

## Data preparation

### Optain Wikipidia data

In the website [Wikidata query service](https://query.wikidata.org/), I run the following query:

```sqarql
SELECT DISTINCT ?painting ?paintingLabel ?artistLabel ?locationLabel ?locationCoord ?year ?image
WHERE {
  ?painting wdt:P31 wd:Q3305213;       # instance of painting
           wdt:P135 wd:Q4692;          # Renaissance movement
           wdt:P170 ?artist;           # creator
           wdt:P571 ?date;             # inception (date)
           wdt:P276 ?location.         # current location (e.g., museum)

  OPTIONAL { ?painting wdt:P18 ?image. }         # image
  OPTIONAL { ?location wdt:P625 ?locationCoord. } # coordinates of the museum

  BIND(YEAR(?date) AS ?year)

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```

This step gives me the `data/wikidata.csv` file

### Obtain Europeana data

Fetch the [Europeana data](https://apis.europeana.eu/en) and convert data into a csv file `europeana_data.csv` using script `europeana.py`.

### Merge table

Merge two files `data/wikidata.csv` and `europeana.py` to prepare for plotting them in GIS. The goal of this step is:
- Clean up data in both `data/wikidata.csv` and `europeana.py`, make sure they all have `longitude` and `latitude` fields
- Merge 2 table to `painting_data.csv` file

Implemented in [mergeData.ipynb](./mergeData.ipynb)


## Reference
1. [Wikidata documents](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help)
2. [Europeana APIs](https://apis.europeana.eu/en)
3. https://www.geeksforgeeks.org/asynchronous-http-requests-with-python/
4. [Geoapify API](https://www.geoapify.com/get-started-with-maps-api/)
5. [Pandas documentation](https://pandas.pydata.org/docs/reference/index.html)


