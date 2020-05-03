from unittest import TestCase
import down_all_images
from down_all_images.download_all import download_all_images

class TestCmd(TestCase):
  def test_download_all_files(self):
    site_urls = [
    'https://www.iosicongallery.com/'
  ]

  download_all_images(site_urls, destination='iosicongallery')
