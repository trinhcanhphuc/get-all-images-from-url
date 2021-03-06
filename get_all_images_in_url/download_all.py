import requests
import os
from os import path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

currentDirectory = os.getcwd()

def download_all_images(url, destination):
  if not destination:
    destination = currentDirectory
  if isinstance(url, list):
    download_all_images_in_list_URL(url, destination)
  else:
    download_all_images_in_single_URL(url, destination)

def download_all_images_in_single_URL(site_url, destination):
  req = Request(site_url, headers={'User-Agent': 'Mozilla/5.0'})
  html = urlopen(req).read().decode('utf-8')
  html = BeautifulSoup(html, 'html.parser')
  imgTags = html.findAll('img')
  for imgTag in imgTags:
    imgURL = imgTag.get('src')
    print('===============================================================================================')
    file_name = imgURL.split('/')[-1]
    r = requests.get(imgURL, allow_redirects=True)
    if r.status_code == 200:
      print("Downloading from url", imgURL)
      des_file_path = path.join(destination, file_name)
      open(des_file_path, 'wb').write(r.content)
      if path.exists(des_file_path):
        print("Downloaded from url", imgURL)
      else:
        print("!!!Error from url", imgURL)
    else:
      print("!!!Not found url", imgURL)

def download_all_images_in_list_URL(site_urls, destination):
  for site_url in site_urls:
    download_all_images_in_single_URL(site_url, destination)
