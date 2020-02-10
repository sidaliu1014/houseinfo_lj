# -*- coding: utf-8 -*-
"""config module"""
__author__ = 'starstar'
# rawler header
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 \
    (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',
    'Referer': 'http://www.baidu.com/link?\
                url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;'
               'wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'}
# sql database row
SQL_ROWS = ['title_url',
            'dealdt',
            'totalprice',
            'listingprice',
            'cycle',
            'name',
            'size',
            'type',
            'story',
            'builtyear',
            'direction',
            'decoration',
            'unitprice',
            'region',
            'city']

# html text tag mapping
HTML_TXT_MAPPING = {"title_name": "title",
                    "address": "houseInfo",
                    "dealdt": "dealDate",
                    "totalprice": "totalPrice",
                    "floor": "positionInfo",
                    'dealcycle': "dealCycleeInfo",
                    'unitprice': 'unitPrice'
                    }
# html href tag mapping
HTML_HREF_MAPPING = {'title_url': 'title'}

# city,region dictionary
CITY_REGION_MAPPING = {
    "sh": [
        "pudong",
        "minhang",
        "baoshan",
        "xuhui",
        "putuo",
        "yangpu",
        "changning",
        "songjiang",
        "jiading",
        "huangpu",
        "jingan",
        "hongkou",
        "qingpu",
        "fengxian",
        "jinshan",
        "chongming"]}
