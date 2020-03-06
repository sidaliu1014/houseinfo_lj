#encoding = utf-8
__author__ = 'starstar'

import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

df = pd.read_csv(
    r"C:\Users\starstar\Desktop\shhouseinfo.csv",
    encoding="utf-8")

int_cols = ["totalprice", 'listingprice', 'cycle', 'size', 'unitprice',
            'builtyear']
for col in int_cols:
    df[col] = df[col].str.extract(r"(\d+)", expand=True)

# derive new columns
df['num_bedroom'] = df['type'].str.extract(r"(\d+)",expand =False)[0]
df['num_livingroom'] = df['type'].str.extract(r'(\d+)',expand=False)[1]
df['total_story'] = df['story'].str.extract(r"(\d+)", expand=True)
# story col
df['story'] = df["story"].str.extract(r"(\D+(?=\())", expand=True)

continuous_columns = [ 'listingprice', 'size',
                      'builtyear', 'num_bedroom', 'num_livingroom',
                      'unitprice', 'total_story']
discrete_columns = ['story', 'direction', 'decoration',
                    'region']

columns = continuous_columns + discrete_columns + ["totalprice"]

# delete NA, empty
#print df[columns].isnull().sum()
#print df[df.isnull().values == True]
df = df[columns].dropna()

#continums_columns normalization
df[continuous_columns] = preprocessing.scale(df[continuous_columns])
#discrete_columns one hot encoding
story_cate = pd.get_dummies(df['story'],prefix = 'story')
dir_cate = pd.get_dummies(df["direction"], prefix="direction")
dec_cate = pd.get_dummies(df["decoration"], prefix="decroration")
region_cate = pd.get_dummies(df['region'], prefix ='region')

res = pd.concat([df,story_cate,dir_cate,dec_cate,region_cate],axis = 1)

target_data = res["totalprice"]
feature_data = res.drop(["totalprice","story","direction","decoration","region"], axis=1)

#print target_data.head()
#print feature_data.head()
X_train, X_test, y_train, y_test = train_test_split(
        feature_data, target_data, test_size=0.3)
lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)

print X_test.head()
print y_pred
print y_test.values
print r2_score(y_test.values,y_pred)
#print lr.intercept_

#print('Coefficients: \n', lr.coef_)
#print("Mean squared error: %.2f"% lr.mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % lr.r2_score(y_test, y_pred))

#print x_axis
#print x_axis
#plt.scatter(X_test["size"], y_test,color='black')
#plt.plot(y_test,label ='real',color='blue')
#plt.plot(x_axis,y_pred,label = 'lr',color = "black")
#plt.show()