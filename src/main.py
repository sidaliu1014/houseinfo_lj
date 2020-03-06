# -*- coding: utf-8 -*-
"""main module"""
__author__ = 'starstar'
import traceback

from crawl import Crawler
from house import House
from connect2db import DbConnector
from config import HEADERS
import preprocess
from connect2db import action_type

if __name__ == "__main__":
    """main"""
    mysql_connector = DbConnector()
    shcrawler = Crawler(HEADERS, 'sh')
    rg_urls = shcrawler.composeurl(1, 20)
    for region, urls in rg_urls.iteritems():
        for url in urls:
            res = shcrawler.parse(shcrawler.crawl(url))
            for i in res:
                i.region = region
                preprocess.main(i)
                try:
                    action, update_fields = mysql_connector.search(i)
                    if action == action_type.insert:
                        mysql_connector.insert(i)
                    elif action == action_type.update:
                        mysql_connector.update(i, update_fields)
                    elif action == action_type.none:
                        print "already inserted and up-to-date"
                except Exception as e:
                    print e.message + i.title_url
                    traceback.print_exc()
                finally:
                    del i
            print "*" * 30
