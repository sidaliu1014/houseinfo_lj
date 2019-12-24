__author__ = 'starstar'

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import house
import requests
from bs4 import BeautifulSoup
import time
from collections import OrderedDict
import pandas as pd

# 设置访问网站的请求头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',
    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'}


def geturl(city, page):

    if page != 1:
        url = "https://{0}.lianjia.com/chengjiao/pg{1}".format(city, page)
    else:
        url = "https://{0}.lianjia.com/chengjiao/".format(city)
    return url


def crawl(url, headers):

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.content


def gethouselist(content):

    bs = BeautifulSoup(content, 'html.parser')
    houselist = bs.find('ul', attrs={'class': 'listContent'})
    return houselist


def parse(c):
    # title
    title = c.find('div', attrs={'class': 'title'})
    if title is not None:
        title_name = title.get_text()
        title_url = (title.find('a')).get('href')
        print title_url, title_name
    else:
        title_name = ""
        title_url = ""

    # address
    address = c.find('div', attrs={'class': 'houseInfo'})
    if address is not None:
        address_houseIcon = address.get_text()
        print address_houseIcon
    else:
        address_houseIcon = ""

    # dealDate
    if(c.find('div', attrs={'class': 'dealDate'})) is not None:
        dealDate = (c.find('div', attrs={'class': 'dealDate'})).get_text()
        print dealDate
    else:
        dealDate = ""

    # totalPrice
    if (c.find('div', attrs={'class': 'totalPrice'})) is not None:
        totalPrice = (c.find('div', attrs={'class': 'totalPrice'})).get_text()
        print totalPrice
    else:
        totalPrice = ""

    # flood
    flood = c.find('div', attrs={'class': 'flood'})
    if (flood.find('div', attrs={'class': 'positionInfo'})) is not None:
        flood_positionIcon = (
            flood.find(
                'div', attrs={
                    'class': 'positionInfo'})).get_text()
        print flood_positionIcon
    else:
        flood_positionIcon = ""

    # dealHouseInfo
    dealHouseInfo = c.find('div', attrs={'class': 'dealHouseInfo'})
    if dealHouseInfo is not None:
        dealHouseInfo_dealHouseTxt = dealHouseInfo.get_text()
        print dealHouseInfo_dealHouseTxt
    else:
        dealHouseInfo = ""

    # dealCycleIcon
    dealCycleInfo = c.find('div', attrs={'class': 'dealCycleeInfo'})
    if dealCycleInfo is not None:
        dealCycleInfo_dealCycleTxt = dealCycleInfo.get_text()
        print dealCycleInfo_dealCycleTxt
    else:
        dealCycleInfo = ""


def main():
    pass

