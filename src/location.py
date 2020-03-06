# encoding=utf-8
__author__ = 'starstar'
import requests


def get_loc(address):

    url = 'https://restapi.amap.com/v3/geocode/geo'
    params = {'address':u"证大家园3期",
              'key':'ca1ea5a0838412bad9a2834cb4655a08'}
    r = requests.get(url,params,timeout=2)
    if r.status_code ==200:
        loc = r.json()["geocodes"][0][u"location"]
    return loc

