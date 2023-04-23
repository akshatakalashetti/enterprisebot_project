import requests
from bs4 import BeautifulSoup
from .models import Reviews
import urllib.request


url_red_64 =        "https://www.amazon.in/New-Apple-iPhone-12-64GB/product-reviews/B08L5TGWD1/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&pageNumber={pn}&formatType=current_format"
url_purple_256 =    "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B0932RLX4G/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&formatType=current_format&pageNumber={pn}"
url_white_256 =     "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_viewopt_fmt?ie=UTF8&pageNumber={pn}&formatType=current_format"
url_green_256 =     "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B08L5VJM1K/ref=cm_cr_arp_d_viewopt_fmt?ie=UTF8&pageNumber={pn}&formatType=current_format"

#response = requests.get(url_red_64)
#print(response)
#html_red = response.text


def multiple_page_parser(url):
    for page_number in range(1,25):
        #response = requests.get(url.format(pn=page_number))
        try:
            response = urllib.request.urlopen(url.format(pn=page_number))
            print(response.status_code)
        except Exception as e:
            print(e)
            
            continue
        html_text = response.read().decode('utf-8')
        try:
            review_parser(html_text)
        except:
            pass


#print(html)
# Parsing the HTML response using BeautifulSoup
def review_parser(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    for review in soup.find_all('div',attrs={'data-hook': 'review'}):
        title = review.find('a',attrs={'data-hook':'review-title'}).span.string
        text = review.find('span',attrs={'data-hook':'review-body'}).span.string
        color = review.find('a', attrs={'data-hook': 'format-strip'}).text.split('Size:')[0].strip()
        size = review.find('a', attrs={'data-hook': 'format-strip'}).text.split('Size:')[1].split('Pattern Name:')[0].strip()

        if review.find('span',attrs={'class':'a-declarative'}) is not None:
            is_verified = True
        else:
            is_verified = False

        try:
            # Check if the review with the given title and review body already exists
            existing_review = Reviews.objects.filter(title=title, review_body=text).first()

            if not existing_review:
                # If the review does not exist, create a new row
                review = Reviews(title=title, review_body=text, size=size, color=color, is_verified_purchase=is_verified, best_or_worst='null')
                review.save()
                print("Review added successfully.")
        except Exception as e:
            print("Error occurred while adding review:", str(e))