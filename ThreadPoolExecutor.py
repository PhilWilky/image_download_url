import requests
import os
import concurrent.futures
import pandas as pd

def extract_single_image(img):
    file_name = img.split('/')[-1]
    
    # Let's try both of these versions in a loop [https:// and https://www.]
    url_paths_to_try = [img, img.replace('https://', 'https://www.')]
    for url_image_path in url_paths_to_try:
        try:
            r = requests.get(img, stream=True)
            if r.status_code == 200:
                with open(file_name, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
                return "Completed"
        except Exception as e:
            pass
    return "Failed"

# Read image URLs from the CSV file
df = pd.read_csv('Images.csv', header=None)
image_urls = df[1].tolist()

# Create a directory for images if it doesn't exist
os.makedirs('images', exist_ok=True)
os.chdir('images')

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(extract_single_image, img): img for img in image_urls}

    for future in concurrent.futures.as_completed(future_to_url):
        try:
            url = future_to_url[future]
            data = future.result()
            print(f'{url}: {data}')
        except Exception as exc:
            print(f'An exception occurred: {exc}')
