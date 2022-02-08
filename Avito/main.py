from pprint import pprint
from typing import List

import bs4
from bs4 import BeautifulSoup as bs
import requests
from datetime import date
from desc import url, gridAttrs, underelement
import os


class File:
    writeDate = str(date.today()).replace("-", "_")
    dump_dir = os.getcwd() + "/dump/"
    page_num = 'p1'

    def fileName(self, log_name):
        body = '_'.join([log_name, self.writeDate, self.page_num])
        return os.path.join(self.dump_dir, body) + '.html'

    def dumpPage(self, html):
        p = self.fileName("iphones")
        with open(p, "w") as handle:
            handle.write(html)


class ExtractElements:

    def __init__(self, bs_class):
        self.soup = bs_class
        self.collect_underelements()

    def num_of_pages(self) -> int:
        return self.soup.find(attrs={"class": "page-title-count-wQ7pG", "data-marker": "page-title/count"}).text

    def grid_of_elements(self) -> List[str]:
        return self.soup.find_all(attrs=gridAttrs)

    def collect_underelements(self):
        self.__go = lambda block_name: self.soup.find_all(attrs=underelement[block_name])


        self.offer_name = self.__go('offer_name')
        self.price = self.__go('price')
        self.description = self.__go('description')
        self.seller_name = self.__go('seller_name')
        self.seller_url = self.__go('seller_url')

        self.seller_rewiew = self.__go('seller_rewiew')

        # self.seller_rewiew = self.soup.find_all(underelement['seller_rewiew'])
        # self.public_hours_ago = self.soup.find_all(underelement['public_hours_ago'])
        # self.show_phone_button = self.soup.find_all(underelement['show_phone_button'])
        # self.metro_stantion = self.soup.find_all(underelement['metro_stantion'])


class AvitoElement:
    def __init__(self, url, from_dumped):
        self.from_dumped = from_dumped
        self.url = url

        self.file = File()
        self.soup = self.__cookSoup__()
        self.extract = self.__extract()

    def __extract(self):
        return ExtractElements(self.soup)

    def __cookSoup__(self):
        if self.from_dumped:
            dump_file = os.path.join(self.file.dump_dir, os.listdir(self.file.dump_dir)[-1])

            with open(dump_file) as file:
                self.html = file.read()

        else:
            self.html = requests.get(self.url).text
            self.file.dumpPage(self.html)

        return bs(self.html, "lxml")

    def gogo(self):
        pass
        # print(type(self.elementGrid))


if __name__ == "__main__":
    token = AvitoElement(url, from_dumped=1)
    # print(token.soup)
    pprint(
        (
            token.extract.price,
            len(token.extract.offer_name),
            len(token.extract.price),
            len(token.extract.description),
            len(token.extract.seller_name)
        )
    )
    print(len(token.extract.grid_of_elements()))