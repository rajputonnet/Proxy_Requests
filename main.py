#############################################
# Author : Akhilesh Singh                   #
# YT Channel : Try2Catch                    #
# Channel Link : http://bit.ly/2wzT9UB      #
#############################################

from PIL import Image

from scraper.image_scraper import ImageScraper
from scraper.user_agent import UserAgent

IMAGE_FORMAT = 'png'  # Change the image type of saved image
URL = 'https://cdn.fileinfo.com/img/ss/lg/jpg_44.jpg'  # Image url which needs to be downloaded
HTTP_PROXY = 'http://167.99.156.196:3128'  # http Proxy ip with port
HTTPS_PROXY = 'https://167.99.156.196:3128'  # https Proxy ip with port

# Getting random user agent
agents = UserAgent().get_random_user_agent()

# Creating header to pass with request
headers = {'User-Agent': agents,
           'Cache-Control': 'no-cache',
           'Accept-Language': 'en-US,en;q=0.5',
           'Upgrade-Insecure-Requests': '1',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Pragma': 'no-cache'
           }

if __name__ == '__main__':

    # Creating dictionary object to pass into get method to as proxies parameter.
    proxies = dict(http=HTTP_PROXY, https=HTTPS_PROXY)

    # Initiating ImageScraper class
    scraper = ImageScraper(url=URL, proxies=proxies, headers=headers)

    # Calling method to get the response of request.
    response = scraper.scrap()

    # If we don't get successful response
    if response.status_code == 200:

        # Getting file name from the image url
        file_name = URL.split('/')[-1]

        # Generating image file from response
        open(file_name, "wb+").write(response.content)

        # Getting image object
        image = Image.open(file_name)

        # If, we have image object then...
        if image:
            print('Image Downloaded Successfully')
