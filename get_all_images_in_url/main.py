#!/usr/bin/env python

from download_all import download_all_images
import argparse

def execute():

  welcome = 'Welcome to Download All Images from URL'
  parser = argparse.ArgumentParser(description=welcome)

  parser.add_argument(
    '--urls', '-u',
    required=True,
    help='URL or URLs you need get images from it. Format: "http://example.com" or "http://example.com", "http://gallery.com"'
  )
  parser.add_argument(
    '--destination',
    '-d',
    help='destination path save files from urls. Default: current directory'
  )
  args = parser.parse_args()

  destination_path = args.destination
  urls = args.urls.split(',')

  download_all_images(urls, destination=destination_path)

if __name__=="__main__":
  execute()
