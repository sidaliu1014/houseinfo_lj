# -*- coding: utf-8 -*-
"""parser module"""
__author__ = 'starstar'


class Parser(object):
    """parser class"""
    @classmethod
    def txtparser(cls, obj, attr, keyword, content):
        """parse text and assign to obj attrs"""
        res = content.find('div', attrs={'class': keyword})
        if res:
            if attr in obj.__slots__:
                setattr(obj, attr, res.get_text().strip())
            else:
                print "not valid attribute"
        else:
            setattr(obj, attr, "")

    @classmethod
    def hrefparser(cls, obj, attr, keyword, content):
        """parse href and assign to obj attrs"""
        res = content.find('div', attrs={'class': keyword})
        if res:
            if attr in obj.__slots__:
                setattr(obj, attr, (res.find('a')).get('href').strip())
            else:
                print "not valid attribute"
        else:
            setattr(obj, attr, "")
