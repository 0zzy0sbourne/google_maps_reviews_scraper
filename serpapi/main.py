from serpapi import GoogleSearch
import json

import config
from url_formatting import parsed_places
from database_manager import DatabaseManager

db_manager = DatabaseManager()

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

  # Create a table inside the database with the name of the place
  db_manager.create_table(place["name"])

  # Insert reviews to the table that is created for a place
  for review in results["place_results"]["user_reviews"]["most_relevant"]: 
    db_manager.insert_into_table(
      place["name"], review["username"], review["rating"], review["description"], review["date"]
    )

  # Describe the table
  db_manager.describe_table(place["name"])
  

"""
results["place_results"].user_reviews.most_relevant --> list of dictionaries. Keys are "username", "rating", "description"
"""