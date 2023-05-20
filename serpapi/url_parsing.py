from constants import places

import re

parsed_places = []

for place in places: 
    place_info = {}
    
    place_id_match = re.search(r"1s(0x.*?)!8m", place["url"]).group(1)
    
    place_latitude = re.search(r"!3d([-+]?.*?)!4d", place["url"]).group(1)
    place_info["latitude"] = place_latitude
    
    place_longitude = re.search(r"!4d([-+]?.*)!", place["url"]).group(1)
    place_info["longitude"] = place_longitude
    
    place_id = f"!4m5!3m4!1s{place_id_match}!8m2!3d{place_latitude}!4d{place_longitude}"
    place_info["id"] = place_id

    parsed_places.append(place_info)
    print(parsed_places)

""" 
[
    {'latitude': '40.4363245', 'longitude': '-3.6829763', 'id': '!4m5!3m4!1s0xd4229e9d8626437:0xf068a61d2d56c279!8m2!3d40.4363245!4d-3.6829763'}, 
    {'latitude': '25.2135121', 'longitude': '55.2823895', 'id': '!4m5!3m4!1s0x3e5f4291891e3c65:0xb0b6e4edc706a675!8m2!3d25.2135121!4d55.2823895'}, 
    {'latitude': '51.524387', 'longitude': '-0.0769656', 'id': '!4m5!3m4!1s0x48761ddde7c030f1:0xab65baefda1490f0!8m2!3d51.524387!4d-0.0769656'}
]
"""
