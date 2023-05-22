import requests
from bs4 import BeautifulSoup


def scrape_reviews(url):
         
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
        }

        """ 

            URL: 
                "https://www.google.com/maps/place/Makan+Saj/@40.456791,-3.7066082,14z/data=!4m8!3m7!1s0xd4229e9d8626437:0xf068a61d2d56c279!8m2!3d40.4363245!4d-3.6829763!9m1!1b1!16s%2Fg%2F11gydfy28c"
            
            DATA ID OF THIS URL: 
                0xd4229e9d8626437:0xf068a61d2d56c279

            EXAMPLE FORMATTED URL: 
                "https://www.google.com/async/reviewDialog?hl=en_us&async=feature_id:0x3e5f43348a67e24b:0xff45e502e1ceb7e2,next_page_token:,sort_by:qualityScore,start_index:,associated_topic:,_fmt:pc"
                "https://www.google.com/async/reviewDialog?hl=en_us&async=feature_id:0x3e5f43348a67e24b:0xff45e502e1ceb7e2,next_page_token:CAESBkVnSUlDZw==,sort_by:qualityScore,start_index:,associated_topic:,_fmt:pc"

        """
       
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')
            
        reviews = []
        location_info = {}
        data_id = ''
        token = ''

            
        for el in soup.select('.lcorif'):
            data_id = soup.select_one('.loris')['data-fid']
            token = soup.select_one('.gws-localreviews__general-reviews-block')['data-next-page-token']
            location_info = {
                'title': soup.select_one('.P5Bobd').text.strip(),
                # 'address': soup.select_one('.T6pBCe').text.strip(),
                # 'avgRating': soup.select_one('span.Aq14fc').text.strip(),
                # 'totalReviews': soup.select_one('span.z5jxId').text.strip()
            }
     
        for el in soup.select('.gws-localreviews__google-review'):
            reviews.append({
                'name': el.select_one('.TSUbDb').text.strip(),
                # 'link': el.select_one('.TSUbDb a')['href'],
                # 'thumbnail': el.select_one('.lDY1rd')['src'],
                # 'numOfreviews': el.select_one('.Msppse').text.strip(),
                'rating': el.select_one('.BgXiYe .lTi8oc')['aria-label'],
                'review': el.select_one('.Jtu6Td').text.strip(),
                # 'images': [d['style'][21:d['style'].rindex(')')] for d in el.select('.EDblX .JrO5Xe')]
            })
     

        # print("LOCATION INFO: ")
        # print(location_info)
        # print("DATA ID:")
        # print(data_id)
        # print("TOKEN:")
        # print(token)
        # print("USER:")

          # Check if there are more reviews to fetch
        while len(reviews) < 100 and token:
            formatted_url = "https://www.google.com/async/reviewDialog?hl=en_us&async=feature_id:{data_id},next_page_token:{token},sort_by:qualityScore,start_index:,associated_topic:,_fmt:pc".format(
                data_id=data_id,
                token=token
            )
            response = requests.get(formatted_url, headers=headers)
            # data = response.json()
            new_page_soup = BeautifulSoup(response.content, 'html.parser')

            for el in new_page_soup.select('.lcorif'):
                data_id = new_page_soup.select_one('.loris')['data-fid']
                token = new_page_soup.select_one('.gws-localreviews__general-reviews-block')['data-next-page-token']
                # print(token)
                location_info = {
                    'title': new_page_soup.select_one('.P5Bobd').text.strip(),
                    # 'address': soup.select_one('.T6pBCe').text.strip(),
                    # 'avgRating': soup.select_one('span.Aq14fc').text.strip(),
                    # 'totalReviews': soup.select_one('span.z5jxId').text.strip()
                }

            for el in new_page_soup.select('.gws-localreviews__google-review'):
                reviews.append({
                    'name': el.select_one('.TSUbDb').text.strip(),
                    # 'link': el.select_one('.TSUbDb a')['href'],
                    # 'thumbnail': el.select_one('.lDY1rd')['src'],
                    # 'numOfreviews': el.select_one('.Msppse').text.strip(),
                    'rating': el.select_one('.BgXiYe .lTi8oc')['aria-label'],
                    'review': el.select_one('.Jtu6Td').text.strip(),
                    # 'images': [d['style'][21:d['style'].rindex(')')] for d in el.select('.EDblX .JrO5Xe')]
                })

        return token, reviews[:100] # Return up to 100 reviews
     

