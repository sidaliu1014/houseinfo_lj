"""crawl module"""
__author__ = 'starstar'

import requests
from bs4 import BeautifulSoup

from parse import Parser
from config import HTML_TXT_MAPPING,HTML_HREF_MAPPING, CITY_REGION_MAPPING
from house import House


class Crawler(object):
    """crawler class"""

    def __init__(self, headers, city):
        """init"""
        self.headers = headers
        self.city = city
        self.parser = Parser()

    def composeurl(self, start_pg, end_pg):
        """compose url with start page and end page, return dictionary with city as key, list of urls as key"""
        res = {}

        if self.city in CITY_REGION_MAPPING:
            for region in CITY_REGION_MAPPING[self.city]:
                urls = []
                if start_pg == 1:
                    urls.append(
                        "https://{0}.lianjia.com/chengjiao/{1}".format(self.city, region))
                    for pg in xrange(2, end_pg + 1):
                        urls.append(
                            "https://{0}.lianjia.com/chengjiao/{1}/pg{2}".format(self.city, region, pg))
                else:
                    for pg in xrange(start_pg, end_pg + 1):
                        urls.append(
                            "https://{0}.lianjia.com/chengjiao/{1}/pg{2}".format(self.city, region, pg))
                res.update({region: urls})
        return res

    def crawl(self, url):
        """request get and return content"""
        res = None
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            res = r.content
        return res

    def parse(self, html):
        """parse content and yield house obj"""
        bs = BeautifulSoup(html, 'html.parser')
        houses_html = bs.find('ul', attrs={'class': 'listContent'})
        if houses_html:
            for house_html in houses_html:
                obj = House()
                obj.city = self.city
                for key, value in HTML_TXT_MAPPING.iteritems():
                    self.parser.txtparser(obj, key, value, house_html)
                for key, value in HTML_HREF_MAPPING.iteritems():
                     self.parser.hrefparser(obj, key, value, house_html)
                yield obj
