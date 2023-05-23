from constants import places
from url_formatting import format_url
from scraper import scrape_reviews
from database_manager import DatabaseManager

db_manager = DatabaseManager()

# Iterate over the places
for place in places: 
    # Format the url
    formatted_url = format_url(place["url"])
    next_page_token, reviews = scrape_reviews(formatted_url)

    # Create a table inside the database with the name of the place
    db_manager.create_table(place["name"])

    # Insert reviews to the table that is created for a place
    for review in reviews: 
        db_manager.insert_into_table(place["name"], review["reviewer_name"], review["rating"], review["review"], review["date"])

    # Describe the table
    db_manager.describe_table(place["name"])
    
