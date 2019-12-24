
__author__ = 'starstar'

import requests
from bs4 import BeautifulSoup
import config
import parse
import house
import preprocess

""" key : property of object
    value: html div tag name
"""
DIC ={"title_name":"title",
      "address":"houseInfo",
      "dealdt":"dealDate",
      "totalprice":"totalPrice",
      "floor":"positionInfo",
      'dealcycle':"dealCycleeInfo",
      'unitprice':'unitPrice'
      }

class Crawler(object):

    def __init__(self, headers, city,parser):

        self.headers = headers
        self.city = city
        self.parser = parser

    def composeurl(self, start_pg,end_pg):

        urls = []

        if start_pg == 1:
            urls.append( "https://{0}.lianjia.com/chengjiao/".format(self.city))
            for pg in xrange(2,end_pg+1):
                urls.append( "https://{0}.lianjia.com/chengjiao/pg{1}".format(self.city, pg))
        else:
            for pg in xrange(start_pg,end_pg+1):
                urls.append( "https://{0}.lianjia.com/chengjiao/pg{1}".format(self.city, pg))
        return urls

    def crawl(self, url):
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            return r.content
        else:
            return None

    def parse(self,html):

        bs = BeautifulSoup(html,'html.parser')
        houses_html = bs. find('ul', attrs={'class': 'listContent'})
        if len(houses_html):
            for house_html in houses_html:
                obj = house.House()
                for key, value in DIC.iteritems():
                    self.parser.txtparser(obj,key,value,house_html)
                self.parser.hrefparser(obj,'title_url','title',house_html)
                yield obj




