import requests
import os
import subprocess
import urllib.request
from bs4 import BeautifulSoup
import tldextract

os.chdir('images')

broken_images = []
image_urls = [
    'http://philwilky.me/img/bg.jpg'
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