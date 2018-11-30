#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used parse content from a webpage.
"""

import requests
from bs4 import BeautifulSoup


def main():
    url = "http://www.nytimes.com/"
    r_text = requests.get(url).text
    soup = BeautifulSoup(r_text, "html.parser")

    for article in soup.find_all(class_="css-180b3ld"):
        news = article.find_all("span", {"class": None})
        if len(news) > 0:
            print news[0].text


if __name__ == '__main__':
    main()
