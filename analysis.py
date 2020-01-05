# -*- coding: utf-8 -*-
__author__ = 'starstar'

import connect2db
import pandas as pd
import numpy as np
import re
#mysql_connector=connect2db.DbConnector()
#def sortbydt():
#    print mysql_connector.select("select * from house.houseinfo order by deldt desc limit 50")


#sortbydt()

def calcorr(filepath):
    data = pd.read_csv(filepath,encoding = "utf-8")
    data.drop(columns=["title_url"],axis =1 ,inplace=True)
    # extract nums out
    data['totalprice']=data['totalprice'].str.extract("(\d+)")
    data['size'] =data['size'].str.extract("(\d+)")
    data['listingprice']=data['listingprice'].str.extract("(\d+)")
    data['cycle']=data['cycle'].str.extract("(\d+)")
    data['builtyear']=data['builtyear'].str.extract("(\d+)")
    data['story'] = data['story'].str.extract("(\d+)")
    #min-max normalization
    #df_norm = data.apply(lambda x:(x - np.min(x)) / (np.max(x) - np.min(x)))
    res =data[['totalprice','size','cycle','builtyear','story']].astype(float)
    df_norm = res.apply(lambda x:(x - np.min(x)) / (np.max(x) - np.min(x)))
    #print (df_norm)
    print(df_norm.corr())
    #print (res.corr())

if __name__ == "__main__":
    filepath = r"C:\Users\starstar\Desktop\shhouseinfo.csv"
    calcorr(filepath)

