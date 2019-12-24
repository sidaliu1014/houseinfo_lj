# -*- coding: utf-8 -*-
__author__ = 'starstar'
import crawl
import house
import connect2db
import config
import parse
import preprocess
import traceback

if __name__ == "__main__":

    sh_house= house.House()
    mysql_connector=connect2db.DbConnector()
    shcrawler = crawl.Crawler(config.headers,'sh',parse.Parser())
    urls = shcrawler.composeurl(1,100)
    for url in urls:
        print url
        res = shcrawler.parse(shcrawler.crawl(url))
        for i in res:
            preprocess.splittitle(i,i.title_name)
            preprocess.splitaddress(i,i.address)
            preprocess.splitfloor(i,i.floor)
            preprocess.splitdealcycle(i,i.dealcycle)
            try:
                flag = mysql_connector.search(i.title_url)
                if flag:
                    mysql_connector.insert(i)
                else:
                    print "already inserted"+ i.title_url
            except Exception as e:
                print e.message + i.title_url
                #traceback.print_exc()
        print "*"*30