from serpapi import GoogleSearch
import config
from database_manager import DatabaseManager
from url_formatting import parsed_places

import logging 

logger = logging.getLogger(__name__)

def process_place(place):
    try:
        db_manager = DatabaseManager()

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

        # Insert reviews into the table created for the place
        for review in results["place_results"]["user_reviews"]["most_relevant"]:
            db_manager.insert_into_table(
                place["name"], review["username"], review["rating"], review["description"], review["date"]
            )

        # Describe the table
        db_manager.describe_table(place["name"])

    except Exception as e:
        logger.exception(f"Error processing place '{place['name']}': {str(e)}")

def main():
    for place in parsed_places:
        process_place(place)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()




