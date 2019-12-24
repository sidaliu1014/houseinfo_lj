# -*- coding: utf-8 -*-
__author__ = 'starstar'


class Parser(object):

    def txtparser(self,obj,attr,keyword,content):

        res=content.find('div',attrs={'class':keyword})
        if res is not None:
            if attr in obj.__slots__:
                setattr(obj,attr,res.get_text().strip())
            else:
                print "not valid attribute"
        else:
            setattr(obj,attr,"")

    def hrefparser(self,obj,attr,keyword,content):
        res=content.find('div',attrs={'class':keyword})
        if res is not None:
            if attr in obj.__slots__:
                setattr(obj,attr,(res.find('a')).get('href').strip())
            else:
                print "not valid attribute"
        else:
            setattr(obj,attr,"")