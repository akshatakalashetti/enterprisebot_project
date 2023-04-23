import requests
from bs4 import BeautifulSoup
from .models import Reviews
import urllib.request
from selenium import webdriver
import time

url_red_64 =        "https://www.amazon.in/New-Apple-iPhone-12-64GB/product-reviews/B08L5TGWD1/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&pageNumber={pn}&formatType=current_format"
url_purple_256 =    "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B0932RLX4G/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&formatType=current_format&pageNumber={pn}"
url_white_256 =     "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_viewopt_fmt?ie=UTF8&pageNumber={pn}&formatType=current_format"
url_green_256 =     "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B08L5VJM1K/ref=cm_cr_arp_d_viewopt_fmt?ie=UTF8&pageNumber={pn}&formatType=current_format"

#response = requests.get(url_red_64)
#print(response)
#html_red = response.text



def multiple_page_parser(url):

    driver = webdriver.Chrome()
    driver.get(url.format(pn=1))
    cookies= [{'domain': 'www.amazon.in', 'expiry': 1712475806, 'httpOnly': False, 'name': 'csm-hit', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tb:MFCCJ30GTEASFWJD2573+s-073331D11WJVCW3Z50HZ|1682235806183&t:1682235806183&adb:adblk_no'}, {'domain': '.amazon.in', 'expiry': 1713771796, 'httpOnly': False, 'name': 'i18n-prefs', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'INR'}, {'domain': '.amazon.in', 'expiry': 1716795804, 'httpOnly': False, 'name': 'session-id-time', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '2082787201l'}, {'domain': '.amazon.in', 'expiry': 1713771796, 'httpOnly': True, 'name': 'sess-at-acbin', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"gbMRFrhqYnhYQfxXny5J2kGDEymcq1xbZSk3K9GnzTU="'}, {'domain': '.amazon.in', 'expiry': 1713771796, 'httpOnly': False, 'name': 'x-acbin', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"8piY4vMfz7buyjM4PkkgnP23ItehyWAukVTzxtH@1FohWjpjIdmfHj74SetjAYHg"'}, {'domain': '.amazon.in', 'expiry': 1713771796, 'httpOnly': True, 'name': 'sst-acbin', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'Sst1|PQEpN6WE51vAn7O_LSlkC5h0CcszEgr7CO5Oz2zZ_zR64u_0EqrWPZwrc4FLF0dzn_7kvpB-2Tt7yiSO3Z35vYcsV-t6CBjU5uZbwzOXaLRaHcYpR0YSmPfeBRAPj8A2wEIsVQ0Gj0ZsXe1808rpvHAGytKUdxcYEaIQFklJdxJZRHpc4kdJvHKFxF6SjnFVteWpL_KQ5g1jjDNnd9YfMXZNFOb4JoIYgJvWBvCphzbWm_IUKg_R13C57IxMISTQtxv0voSWzz99a0KT1io0Z3TNbu5CwAA_n-4CdSjNRxZmz20'}, {'domain': '.amazon.in', 'expiry': 1713771796, 'httpOnly': True, 'name': 'at-acbin', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'Atza|IwEBILqgaw77AQ6Yw0trleK5yK7xhwYYmd2UlC8IBkLd2NLl0e6Z3QbqKWVnhx814W5zUii4Apefbx644l8vqbl-FfJjXbroN1rm_m4KLGuwEK1-zYTTwqv1vuV6Egvo5_QYp-gydMn_F72neEQBrwIdEDtnzFEoF1qqbAaKdTYA-EebOGSf7r7Id996yti3wttEUYuiSPEBS996wCOkQ8dmDpOqr8JZRDA5iLZQ7YLiWsBSBD5D0F6XKi5VOWA5lqHjx6o'}, {'domain': '.amazon.in', 'expiry': 1716795804, 'httpOnly': True, 'name': 'session-token', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '5TQyEyVPuumaO3i7OBv9x6XbPHR/IqRQ5tHmFd8Vuk7aXKlNFNPqnZfanhEEN0ftt1gYH0liu9iW8AdP2sLP/ox+GS3z3RFiODBDpWS1EkDh9fOvxzuqd7u+1ykYZgGGgoFPOcXH4kD6fzLcJakqepRwZrLIB+z17W43Cc5pjG/f9TZCTUNIqrsEtjzbfQ5wh2jQPGoQko8oK5MFpQjsj5CXxRZfvTYx64stNGCOJgIIEuIm+u/ZQ22Hu4bKkqun'}, {'domain': '.amazon.in', 'expiry': 1713771796, 'httpOnly': False, 'name': 'ubid-acbin', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '260-8368852-7326236'}, {'domain': '.amazon.in', 'expiry': 1716795804, 'httpOnly': False, 'name': 'session-id', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '258-6900366-9333749'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(5)

    
    for page_number in range(1,1000):
        #response = requests.get(url.format(pn=page_number))
        try:
            driver.get(url.format(pn=page_number))
            #response = urllib.request.urlopen(url.format(pn=page_number))
            #print(response.status_code)
            time.sleep(2)
            
        except Exception as e:
            print(e)
            continue
        html_text = driver.page_source
        print(len(html_text))
        time.sleep(2)
        try:
            review_parser(html_text)
        except Exception as e:
            print(str(e))
            
    driver.quit()

#print(html)
# Parsing the HTML response using BeautifulSoup
def review_parser(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    for review in soup.find_all('div',attrs={'data-hook': 'review'}):
        title = review.find('a',attrs={'data-hook':'review-title'}).span.string
        text = review.find('span',attrs={'data-hook':'review-body'}).span.get_text()
        try:
            color = review.find('a', attrs={'data-hook': 'format-strip'}).get_text().split('Size:')[0].strip()
        except:
            color='NA'
        try:
            size = review.find('a', attrs={'data-hook': 'format-strip'}).get_text().split('Size:')[1].split('Pattern Name:')[0].strip()
        except:
            size='NA'
        if review.find('span',attrs={'class':'a-declarative'}) is not None:
            is_verified = True
        else:
            is_verified = False

        try:
            # Check if the review with the given title and review body already exists
            existing_review = Reviews.objects.filter(title=str(title), review_body=str(text)).first()

            if not existing_review:
                # If the review does not exist, create a new row
                review = Reviews(title=str(title), review_body=str(text), size=str(size), color=str(color), is_verified_purchase=is_verified, best_or_worst='null')
                review.save()
                print("Review added successfully.")
            else:
                print("existing review",str(title))
        except Exception as e:
            print("error")
            