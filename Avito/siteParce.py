from bs4 import BeautifulSoup as bs
import requests
import pickle
from datetime import date
from desc import url, attrs


class AvitoElement:

    def __init__(self, url, log_name):
        self.url = url
        self.html = requests.get(self.url).content
        self.soup = bs(self.html, "lxml")
        self.log_name = log_name

    def findCascadeElements(self, description):
        self.page = self.soup.find_all(attrs=description)
        self.dumpPage()

    def dumpPage(self, page_num="1"):
        writeDate = str(date.today()).replace("-", "_")
        data_dir = "./dump/"

        with open(data_dir + f'{self.log_name}_{writeDate}_p{page_num}.html', 'wb') as handle:
            handle.write(self.html)


if __name__ == "__main__":
    token = AvitoElement(url, 'iphone')
    token.findCascadeElements(attrs)

    token.dumpPage()