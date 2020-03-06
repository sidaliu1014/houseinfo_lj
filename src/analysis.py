# -*- coding: utf-8 -*-
__author__ = 'starstar'

import matplotlib.pyplot as plt
#import connect2db
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import re
# mysql_connector=connect2db.DbConnector()
# def sortbydt():
#    print mysql_connector.select("select * from house.houseinfo order by deldt desc limit 50")


# sortbydt()

def calcorr(filepath):
    data = pd.read_csv(filepath, encoding="utf-8")
    data.drop(["title_url"], axis=1, inplace=True)
    # extract nums out
    data['totalprice'] = data['totalprice'].str.extract(r"(\d+)")
    data['size'] = data['size'].str.extract(r"(\d+)")
    data['listingprice'] = data['listingprice'].str.extract(r"(\d+)")
    data['cycle'] = data['cycle'].str.extract(r"(\d+)")
    data['builtyear'] = data['builtyear'].str.extract(r"(\d+)")
    data['story'] = data['story'].str.extract(r"(\d+)")
    data['unitprice'] = data['unitprice'].str.extract(r"(\d+)")
    # one-hot key
    dir_cate = pd.get_dummies(data["direction"], prefix="direction")
    dec_cate = pd.get_dummies(data["decoration"], prefix="decroration")
    #print dec_cate.head()
    cols = ['totalprice', 'size', 'cycle', 'builtyear', 'story', 'unitprice']
    data_nums = data[cols].astype(float)
    # standardization
    mean = data_nums.loc[:, cols].mean()
    std = data_nums.loc[:, cols].std()
    data_nums.loc[:, cols] = (data_nums.loc[:, cols] - mean) / std
    # heatmap
    corrmatrix = data_nums.corr()
    sns.heatmap(

        corrmatrix,
        square=True,
        vmax=1,
        vmin=-1,
        center=0.0,
        cmap='coolwarm')
    # plt.show()
    # linear regression
    #res =pd.concat([data_nums,dir_cate,dec_cate])
    res = pd.concat([data_nums, data["direction"], data["decoration"]], axis=1)
    feature_data = res.drop("totalprice", axis=1)
    target_data = res["totalprice"]
    X_train, X_test, y_train, y_test = train_test_split(
        feature_data, target_data, test_size=0.3)
    df_train = pd.concat([X_train, y_train], axis=1)
    df_test = pd.concat([X_test, y_test], axis=1)
    lr_model = ols(
        "totalprice~C(direction)+C(decoration)+size+cycle+builtyear+story+unitprice",
        data=df_test).fit()
    print lr_model.summary()
    #print X_train.head()
    #print y_train.head()
    # lr_model.predict(X_test)
    #from sklearn.linear_model import LinearRegression
    #model = LinearRegression()
    # model.fit(X_train,y_train)
    #print "r2 is %.4f" % model.score(X_test,y_test)


def stats(filepath):

    data = pd.read_csv(filepath, encoding="utf-8")
    data.drop(["title_url"], axis=1, inplace=True)
    data.drop(["id"], axis=1, inplace=True)
    # extract nums out
    data['totalprice'] = data['totalprice'].str.extract(
        r"(\d+)", expand=True).astype(float)
    data['size'] = data['size'].str.extract(
        r"(\d+)", expand=True).astype(float)
    data['listingprice'] = data['listingprice'].str.extract(
        r"(\d+)", expand=True).astype(float)
    data['cycle'] = data['cycle'].str.extract(r"(\d+)", expand=True)
    data['builtyear'] = data['builtyear'].str.extract(r"(\d+)", expand=True)
    data['story'] = data['story'].str.extract(r"(\d+)", expand=True)
    data['unitprice'] = data['unitprice'].str.extract(
        r"(\d+)", expand=True).astype(float)
    data['yyyymm'] = data['deldt'].str.extract(
        "([0-9]{4}-[0-9]{1,2})", expand=True)
    # remove nan
    data.dropna(axis=0, how='any', inplace=True)
    print data.isnull().sum()
    print data.head()
    # group by region and month
    region_unitprice_mean = data.groupby(
        ['yyyymm', 'region']).mean()['unitprice']
    #print region_unitprice_mean
    region_unitprice_mean.to_csv(r"C:\Users\starstar\Desktop\region_mean.csv")
    # group by name and month
    name_unitprice_mean = data.groupby(['yyyymm', 'name']).mean()['unitprice']
    #print name_unitprice_mean
    name_unitprice_mean.to_csv(
        r"C:\Users\starstar\Desktop\name_mean.csv",
        encoding='utf-8')

   # sort by total price
    totalprice_rank = data.sort_values(
        by=['totalprice'], ascending=False).head(20)
    #print totalprice_rank
   # sort by size
    size_rank = data.sort_values(by=['size'], ascending=False).head(20)
   # print size_rank

   # total price histgram
    totalprice_hist = data['totalprice'].plot.hist(
        grid=True, bins=100, rwidth=0.9, color='#607c8e')
    # plt.show()

   # group by type
    type_count = data.groupby(['type']).count()['name']
    print type_count

  # group by direction
    direction_count = data.groupby(['direction']).count()['name']
    print direction_count


if __name__ == "__main__":
    filepath = r"C:\Users\starstar\Desktop\shhouseinfo.csv"
    # calcorr(filepath)
    stats(filepath)
