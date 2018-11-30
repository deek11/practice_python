#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used write to a file.
"""

import requests
from bs4 import BeautifulSoup
import codecs


def main():
    url = "http://www.nytimes.com/"
    r_text = requests.get(url).text
    soup = BeautifulSoup(r_text, "html.parser")

    with codecs.open('sample.txt', 'w', 'utf-8') as open_file:
        for article in soup.find_all(class_="css-180b3ld"):
            news = article.find_all("span", {"class": None})
            if len(news) > 0:
                open_file.write(news[0].text+'\n')


if __name__ == '__main__':
    main()
