# -*- coding: utf-8 -*-
"""
insert data to PostgreSQL

@author: Shih-Chi
"""

from pg import DB
import numpy as np
import datetime

db = DB(dbname='Pingtung', host='localhost', port=5432,
    user='postgres', passwd='husky')

sites = db.query('select site from "Well_Stations"').getresult()
for site in sites:
    
    mindate = db.query('select MIN(date),MAX(date) from "Well" where site like \'{site}\''.format(site = site[0])).getresult()
    if mindate[0][0] != None: 
        print('{site}: date from {ys}/{ms}/{ds} to {ye}/{me}/{de}'.format(site=site[0],ys=mindate[0][0].year,ms=mindate[0][0].month,ds=mindate[0][0].day,ye=mindate[0][1].year,me=mindate[0][1].month,de=mindate[0][1].day))
        db.query('UPDATE "Well_Stations" SET starttime = \'{ys}/{ms}/{ds}\', endtime = \'{ye}/{me}/{de}\' WHERE site like \'{site}\''.format(site=site[0],ys=mindate[0][0].year,ms=mindate[0][0].month,ds=mindate[0][0].day,ye=mindate[0][1].year,me=mindate[0][1].month,de=mindate[0][1].day));