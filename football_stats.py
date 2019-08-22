#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
assignment9 - football_stats.py
Created on Wed Aug 21 18:32:51 2019
@author: SPSjroseboom
"""

from bs4 import BeautifulSoup
import urllib2


url = (
'https://www.cbssports.com/nfl/stats/playersort/nfl/'
'year-2018-season-regular-category-touchdowns'
)

def openpage(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    return soup


def main():
    order = 0
    website = openpage(url)
    data_table = website.find('table', class_='data').find_all('tr')
    print '-----------------------------------'
    print ' 2018 TOP 20 PLAYERS IN TOUCHDOWNS '
    print '-----------------------------------'
    for row in data_table[3:23]:
        row_data = row.find_all('td')
        order += 1
        data = ('{}) {}     \n    Position: {}     \n'
               '    Team: {}     \n    Touchdowns: {}').format(
            order,
            row_data[0].text,
            row_data[1].text,
            row_data[2].text,
            row_data[6].text
        )
        print data
        print '--------------------'
        #using the above to divide the prices so it looks cleaner

if __name__ == '__main__':
    main()