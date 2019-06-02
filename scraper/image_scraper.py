import requests


class ImageScraper:

    def __init__(self, proxies, url, headers, timeout=10):
        self.proxies = proxies
        self.url = url
        self.headers = headers
        self.timeout = timeout

    def scrap(self):
        try:
            response = requests.get(url=self.url, proxies=self.proxies, headers=self.headers, timeout=self.timeout)
        except requests.exceptions.ProxyError:
            print('Max retries exceeded.')
        except requests.exceptions.ConnectTimeout:
            print('Not able to connect with the request. Please check your internet connection.')
        return response
