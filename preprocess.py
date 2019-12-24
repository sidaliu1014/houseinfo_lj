# -*- coding: utf-8 -*-
__author__ = 'starstar'


def splittitle(obj,title):

    res = title.split(" ")
    if len(res)==3:
        setattr(obj,"name",res[0])
        setattr(obj,"type",res[1])
        setattr(obj,"size",res[2])
    else:
        print "please check title"

def splitaddress(obj,address):

    res =address.split("|")
    if len(res)==2:
        setattr(obj,"direction",res[0])
        setattr(obj,"decoration",res[1])
    else:
        print "please check address"

def splitfloor(obj,floor):

    res = floor.split(" ")
    if len(res) ==2 :
        setattr(obj,"story",res[0])
        setattr(obj,"builtyear",res[1])
    else:
        print "please check floor"

def splitdealcycle(obj,dealcycle):
    res = dealcycle.split(u"万")
    if len(res) ==2:
        setattr(obj,'listingprice',res[0]+u"万")
        setattr(obj,'cycle',res[1])
    else:
        print "please check dealcycle"