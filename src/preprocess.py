# -*- coding: utf-8 -*-
"""preprocess module"""
__author__ = 'starstar'
from datetime import datetime

def _splittitle(obj):
    """split title into three elements: name,type,size and assign to obj attrs"""
    title_name = getattr(obj,'title_name') if hasattr(obj,'title_name') else None
    if title_name:
        res = title_name.split(" ")
        if len(title_name.split(" ")) == 3:
            setattr(obj, "name", res[0].strip())
            setattr(obj, "type", res[1].strip())
            setattr(obj, "size", res[2].strip())
        else:
            print "please check title: " + title_name
    else:
        print "no title_name property in house object"

def _splitaddress(obj):
    """split address into two elements: direction , decoration and assign to obj attrs"""
    address = getattr(obj,'address') if hasattr(obj,'address') else None
    if address:
        res = address.split("|")
        if len(res) == 2:
            setattr(obj, "direction", res[0].strip())
            setattr(obj, "decoration", res[1].strip())
        else:
            print "please check address"
    else:
        print " no address property in house object"

def _splitfloor(obj):
    """split floor into two eles: story,builtyear and assign to obj attrs"""
    floor = getattr(obj, 'floor') if hasattr(obj,'floor') else None
    if floor:
        res = floor.split(" ")
        if len(res) == 2:
            setattr(obj, "story", res[0].strip())
            setattr(obj, "builtyear", res[1].strip())
        else:
            print "please check floor"
    else:
        print "no floor property in house object"

def _splitdealcycle(obj):
    """split dealcycle into two eles: listingprice,cycle and assign to obj attrs"""
    dealcycle = getattr(obj,'dealcycle') if hasattr(obj,'dealcycle') else None
    if dealcycle:
        res = dealcycle.split(u"万")
        if len(res) == 2:
            setattr(obj, 'listingprice', res[0].strip()+u"万")
            setattr(obj, 'cycle', res[1].strip())
        else:
            print "please check dealcycle"
    else:
        print "no dealcycle property in house object"

def main(obj):
    _splittitle(obj)
    _splitaddress(obj)
    _splitfloor(obj)
    _splitdealcycle(obj)
