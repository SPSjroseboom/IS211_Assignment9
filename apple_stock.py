#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
assignment9 - apple_stock.py
Created on Wed Aug 21 18:21:38 2019
@author: SPSjroseboom
"""


import urllib2
from bs4 import BeautifulSoup

url = 'https://www.nasdaq.com/symbol/aapl/historical'

APPLE_STOCK = urllib2.urlopen(url)
SOUP = BeautifulSoup(APPLE_STOCK.read(), 'lxml')
STOCK = SOUP.tbody.find_all('tr')

print '-----------------------------------'
print '    APPLE STOCK CLOSING PRICES     '
print '-----------------------------------'

for item in STOCK:
    row = [text for text in item.stripped_strings]
    if len(row) == 0:
        pass
    else:
        data = "{}: Close Price: ${}".format(row[0], row[4])
        print data
        print '-----------------------------------'
        #using the above to divide the prices so it looks cleaner