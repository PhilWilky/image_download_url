import requests
import os
import subprocess
import urllib.request
from bs4 import BeautifulSoup
import tldextract

os.chdir('images')

broken_images = []
image_urls = [
    'https://dgduupz79pcvd.cloudfront.net/productimages/vow_premium/l/kf01548.jpg',
    'https://dgduupz79pcvd.cloudfront.net/productimages/vow_premium/l/ss18941.jpg',
    'https://dgduupz79pcvd.cloudfront.net/productimages/vow_premium/l/kf20016.jpg',
    'https://dgduupz79pcvd.cloudfront.net/productimages/vow_premium/l/wac10041.jpg',
    'https://dgduupz79pcvd.cloudfront.net/productimages/vow_premium/l/phil.jpg',
    ]

for img in image_urls:
    
    # Grabs the file name by take everything right to the last ([-1]) slash
    file_name = img.split('/')[-1]

    r = requests.get(img, stream=True)

    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
    else:
        broken_images.append(img)

    print(file_name)


    print(img)