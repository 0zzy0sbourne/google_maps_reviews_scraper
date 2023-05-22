
def format_url(url): 

    # Find the start and end indexes of the data ID
    start_index = url.index("!1s") + len("!1s")
    end_index = url.index("!8m2")

    # Extract the data ID from the URL
    data_id = url[start_index:end_index]

    # Construct the URL with the extracted data ID
    formatted_url = "https://www.google.com/async/reviewDialog?hl=en_us&async=feature_id:{data_id},next_page_token:,sort_by:qualityScore,start_index:,associated_topic:,_fmt:pc".format(data_id=data_id)

    return formatted_url

