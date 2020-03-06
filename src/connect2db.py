"""sql database module """
# -*- coding: utf-8 -*-

__author__ = 'starstar'

import pyodbc
from config import SQL_ROWS
from enum import Enum
action_type = Enum("action_type", ("insert", "update", "none"))


class DbConnector(object):

    def __init__(self):

        self.connect()

    def connect(self):
        """database connect"""
        conn = pyodbc.connect(
            'Driver={MySQL ODBC 5.2 Unicode Driver};'
            'Server=localhost;Database=house;'
            'uid=root;password=root',
            use_unicode=1,
            charset='utf8')
        self.cursor = conn.cursor()

    def search(self, house):

        action, update_fields = action_type.none, dict()
        string = "select * from house.houseinfo where title_url = '%s'limit 1" % (
            house.title_url)
        res = self.cursor.execute(string).fetchone()
        if res:
            update_fields = self.__check_cols(res, house)
            if update_fields:
                action = action_type.update
        else:
             action = action_type.insert
        return action, update_fields

    def __check_cols(self, searchresult, house):

        update_fields = dict()
        for i, attr in enumerate(SQL_ROWS):
            if getattr(house, attr) != searchresult[i]:
                update_fields.update({attr: getattr(house, attr)})
        return update_fields

    def insert(self, house):
        """insert into sql database
            params: house (object)
        """
        if house.check():
            string = u"insert into house.houseinfo values('{house.title_url}','{house.dealdt}'," \
                 u"'{house.totalprice}','{house.listingprice}','{house.cycle}','{house.name}'," \
                 u"'{house.size}','{house.type}','{house.story}','{house.builtyear}'," \
                 u"'{house.direction}','{house.decoration}','{house.unitprice}'," \
                 u"'{house.region}','{house.city}')".format(house=house)

            print string
            self.cursor.execute(string)
            self.cursor.commit()

    def update(self, house, update_fields):
        """update sql database if record is found in sql
            params: house (object)
                    dict (update fields)
        """
        set_string = ",".join(
            u"{key} = '{value}'".format(
                key=key,
                value=value) for key,
            value in update_fields.items())
        string = u"update house.houseinfo set " + set_string + \
            " where title_url = '%s'" % (house.title_url)
        print string
        self.cursor.execute(string)
        self.cursor.commit()
