__author__ = 'starstar'

import connect2db


mysql_connector=connect2db.DbConnector()
def sortbydt():
    print mysql_connector.select("select * from house.houseinfo order by deldt desc limit 50")


sortbydt()
