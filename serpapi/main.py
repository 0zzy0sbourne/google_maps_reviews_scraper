from serpapi import GoogleSearch
import json

params = {
  "api_key": "7472d980a85496d47374c1c49459354267a840100158a130ac4be54182888453",
  "engine": "google_maps",
  "type": "place",
  "google_domain": "google.com",
  "q": "Coffee",
  "hl": "en",
  "ll": "@40.7455096,-74.0083012,14z",
  "data": "!4m5!3m4!1s0xd4229e9d8626437:0xf068a61d2d56c279!8m2!3d40.4363245!4d-3.6829763" # should not be static
}

search = GoogleSearch(params)
results = search.get_dict()

print(results["place_results"]["title"])
print(json.dumps(results["place_results"], indent=2, ensure_ascii=False))