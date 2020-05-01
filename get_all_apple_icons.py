from download_all import downloadAllImage


def main():

  site_urls = [
    'https://www.iosicongallery.com/'
  ]

  downloadAllImage(site_urls, destination='iosicongallery')

if __name__=="__main__":
  main()
