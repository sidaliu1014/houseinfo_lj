# -*- coding: utf-8 -*-
"""main module"""
__author__ = 'starstar'
import traceback

from crawl import Crawler
from house import House
from connect2db import DbConnector
from config import HEADERS
import preprocess

if __name__ == "__main__":
    """main"""
    mysql_connector = DbConnector()
    shcrawler = Crawler(HEADERS, 'sh')
    rg_urls = shcrawler.composeurl(1, 21)
    for region, urls in rg_urls.iteritems():
        for url in urls:
            res = shcrawler.parse(shcrawler.crawl(url))
            for i in res:
                i.region = region
                preprocess.main(i)
                try:
                    flag, update_fields = mysql_connector.search(i)
                    if flag:
                        if update_fields:
                            mysql_connector.insert(i)
                        else:
                            print "already inserted and up-to-date"
                    else:
                        mysql_connector.update(i, update_fields)
                except Exception as e:
                    print e.message + i.title_url
                    traceback.print_exc()
                finally:
                    del i
            print "*" * 30
