#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
assignment9 - weather.py
EXTRA CREDIT
Created on Wed Aug 21 19:16:34 2019
@author: SPSjroseboom
"""


import urllib2
from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/history/monthly/us/ny/new-york-city/KLGA/date/2019-1'

NYC_WEATHER = urllib2.urlopen(url)
SOUP = BeautifulSoup(NYC_WEATHER.read(), 'lxml')
WEATHER = SOUP.tbody.find_all("tr")

print '-----------------------------------'
print '      AVERAGE TEMPS IN AUGUST      '
print '-----------------------------------'
for item in WEATHER:
    row = [text for text in item.stripped_strings]
    if len(row) == 0:
        pass
    else:
        data = "August {}: Average Temperature(F): {}".format(row[11], row[2])
        print data
        print '-----------------------------------'
        #using the above to divide the days and temperatures

#i get a HTTPError: Forbidden when running
#I'm not sure how to proceed so I'm just gonna stop here."""