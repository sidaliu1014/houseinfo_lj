# -*- coding: utf-8 -*-

__author__ = 'starstar'
import pyodbc

class DbConnector(object):

    def __init__(self):
        self.connect()
        pass

    def connect(self):
        #print pyodbc.drivers()

        conn = pyodbc.connect('Driver={MySQL ODBC 5.2 Unicode Driver};'
                             'Server=localhost;Database=wine;'
                             'uid=root;password=root',use_unicode=1, charset='utf8')

        self.cursor = conn.cursor()
        res = self.cursor.execute('show databases')
        pass

    def search(self,key):
        string = "select * from house.houseinfo where title_url = '%s'"%(key)
        res = self.cursor.execute(string).fetchall()
        return True if len(res) == 0 else False

    def insert(self,house):

        string = "insert into house.houseinfo values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(house.title_url,
                                                                                             house.dealdt,
                                                                                             house.totalprice
                                                                                             , house.listingprice,
                                                                                             house.cycle
                                                                                             , house.name,
                                                                                              house.size,house.type,house.story,
                                                                                              house.builtyear,house.direction,
                                                                                              house.decoration,house.unitprice)

        print string
        self.cursor.execute(string)
        self.cursor.commit()
        print "correct"
        pass

    def select (self,sqlquery):
        return self.cursor.execute(sqlquery).fetchall()