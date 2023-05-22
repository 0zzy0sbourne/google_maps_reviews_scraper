from constants import places
from url_formatting import format_url
from scraper import scrape_reviews
from db_entries import * 

# Iterate over the places
for place in places: 
    # Format the url
    formatted_url = format_url(place["url"])
    next_page_token, reviews = scrape_reviews(formatted_url, place["name"])
    