from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup

def extract_location_id(google_maps_link):
    parsed_url = urlparse(google_maps_link)
    query_params = parse_qs(parsed_url.query)

    if 'entry' in query_params:
        entry_value = query_params['entry'][0]
        entry_parts = entry_value.split(':')
        
        if len(entry_parts) > 1:
            location_id = entry_parts[1]
            return location_id

    return None


def access_google_maps_page(google_maps_link):
    response = requests.get(google_maps_link)

    if response.status_code == 200:
        # The page was successfully accessed
        print("[INFO] The page is successfully accessed ...")
        html_content = response.content
        print(html_content)

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the necessary information from the HTML
        # place_info(soup)
        get_address(soup)
        # location = extract_location(soup)
        # working_hours = extract_working_hours(soup)

        # Print or process the extracted information
        # print("Location:", location)
        # print("Working Hours:", working_hours)

        # Return the extracted information as needed
        # return location, working_hours
    else:
        # Failed to access the page
        print(f"[ERROR] Failed to access the Google Maps page. Status code: {response.status_code}")


def extract_location(soup):
    # Find the HTML element containing the location information
    location_element = soup.find('h1', class_='section-hero-header-title-title')
    
    # Extract the location text
    location = location_element.text.strip()
    
    # Return the extracted location
    return location

def extract_working_hours(soup):
    # Find the HTML element containing the working hours information
    working_hours_element = soup.find('div', class_='section-info-hour-text')

    # Extract the working hours text
    working_hours = working_hours_element.text.strip()
    
    # Return the extracted working hours
    return working_hours


def extract_desired_values(soup):
    # Example: Extract the text of all paragraph tags with a specific class
    desired_values = []
    paragraphs = soup.find_all('p', class_='my-class')
    for paragraph in paragraphs:
        desired_values.append(paragraph.text)
    
    # Add more code to extract other desired values from the HTML content as needed
    
    return desired_values

def place_info(soup):
    place_info_div = soup.find('div', {'aria-label': 'Makan Saj ile ilgili bilgiler'})

    if place_info_div: 
        print("[INFO] Place Info div is found")
        print(place_info_div)
    else: 
        print("[ERROR] Place Info div could not be found")

def get_address(soup):
    # Find the div containing the address
    div_array = soup.find_all("div")
    print(div_array)


google_maps_link = 'https://goo.gl/maps/JMQEk2CsYQGyw9649?coh=178571&entry=tt'
maps_page = access_google_maps_page(google_maps_link)



