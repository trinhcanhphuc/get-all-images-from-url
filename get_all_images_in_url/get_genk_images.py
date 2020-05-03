from download_all import download_all_images


def main():

  site_urls = [
    'https://www.google.com/'
  ]

  download_all_images(site_urls, destination='google')

if __name__=="__main__":
  main()
