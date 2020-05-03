from download_all import download_all_images


def main():

  site_urls = [
    'https://www.iosicongallery.com/'
  ]

  download_all_images(site_urls, destination='iosicongallery')

if __name__=="__main__":
  main()
