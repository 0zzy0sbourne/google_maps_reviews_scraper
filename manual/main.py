import logging
from constants import places
from url_formatting import format_url
from scraper import scrape_reviews
from database_manager import DatabaseManager

logger = logging.getLogger(__name__)

def process_place(place):
    try:
        db_manager = DatabaseManager()

        formatted_url = format_url(place["url"])
        next_page_token, reviews = scrape_reviews(formatted_url)

        # Create a table inside the database with the name of the place
        db_manager.create_table(place["name"])

        # Insert reviews into the table created for the place
        for review in reviews:
            db_manager.insert_into_table(
                place["name"], review["reviewer_name"], review["rating"], review["review"], review["date"]
            )

        # Describe the table
        db_manager.describe_table(place["name"])

    except Exception as e:
        logger.exception(f"Error processing place '{place['name']}': {str(e)}")

def main():
    for place in places:
        process_place(place)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

