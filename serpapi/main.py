from serpapi import GoogleSearch
import json

import config
# from db_entries import *
from url_formatting import parsed_places

for place in parsed_places: 
  
  params = {
    "api_key": config.API_KEY,
    "engine": "google_maps",
    "type": "place",
    "google_domain": "google.com",
    "q": "Coffee",
    "hl": "en",
    "ll": "@40.7455096,-74.0083012,14z",
    "data": place["id"]
  }

  search = GoogleSearch(params)
  results = search.get_dict()

  # print(results["place_results"]["title"])
  # print(json.dumps(results["place_results"], indent=2, ensure_ascii=False))

  for review in results["place_results"]["user_reviews"]["most_relevant"]: 
    print(review["username"])
    
  """
  for review in results["place_results"]["user_reviews"]["most_relevant"]: 
      print(review["username"])

  # Create a table inside the database with the name of the place
  create_table(place["name"])

  # Insert reviews to the table that is created for a place
  for review in results["place_results"]["user_reviews"]["most_relevant"]: 
      insert_into_table(place["name"], review["username"], review["rating"], review["description"])

  # Describe the table
  describe_table(place["name"])
  """




"""
results["place_results"].user_reviews.most_relevant --> list of dictionaries, username, rating, description


!4m5!3m4!1s0xd4229e9d8626437:0xf068a61d2d56c279!8m2!3d40.4363245!4d-3.6829763
"""