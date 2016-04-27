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

import os
for filename in os.listdir('Pingtung/Well'):
    site = filename[0:8]
    year = filename[9:13]
    print(filename)
    sites = db.query('select site, starttime, endtime from "Well_Stations" where site like \'{site}\''.format(site=site)).getresult()
    if sites != []:
        for line in open('Pingtung/Well/{FN}'.format(FN=filename), 'r'):
            #檢查時間是否相符
            data = line.split()
            if len(data[1]) == 8:
                if (data[0][0:4] != year) and (data[0][5:10] != '01-01'):
                    print('檔案有誤 日期不對')
                    break
            else:
                print('檔案有誤 時間不對')
                break
                
            db.insert('Well', site=site, date='{date} {time}'.format(date=data[0], time=data[1]), value=data[2])
    else:
        print('查無此站')


