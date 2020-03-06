# -*- coding: utf-8 -*-
"""house module"""
__author__ = 'starstar'
from datetime import datetime

DATETIMEFIELDS = ["dealdt"]

class House(object):
    """house class"""
    __slots__ = [
        'title_name',
        'title_url',
        'address',
        'dealdt',
        'totalprice',
        'floor',
        'dealcycle',
        'name',
        'size',
        'type',
        'story',
        'builtyear',
        'direction',
        'decoration',
        'listingprice',
        'cycle',
        'unitprice',
        'region',
        'city']


    def __setattr__(self, key, value):
        if key in DATETIMEFIELDS:
             if len(value.split(".")) == 3:
                 House.__dict__[key].__set__(self,datetime.strptime(value, "%Y.%m.%d").date())
             else:
                 print "please check dealdt:{0} format".format(value)
        else:
            House.__dict__[key].__set__(self,value)

    def check(self):

        for attr in House.__slots__:
            if  not hasattr(self,attr):
                    return False
                    break
        return True
