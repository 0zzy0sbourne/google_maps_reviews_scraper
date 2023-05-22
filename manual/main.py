from constants import urls
from url_formatting import format_url
from scraper import scrape_reviews


# Iterate over the places
for index, url in enumerate(urls): 
    # Format the url
    formatted_url = format_url(url)
    next_page_token, reviews = scrape_reviews(formatted_url)
    if index == 0: 
        print("------ REVIEWS OF MAKAN SAJ ------")
       
    elif index == 1: 
        print("------ REVIEWS OF ZUMA DUBAI ------")
       
    elif index == 2: 
        print("------ REVIEWS OF BAO NOODLE SHOP ------")
        for review in reviews: 
            print(review["name"])
    
    