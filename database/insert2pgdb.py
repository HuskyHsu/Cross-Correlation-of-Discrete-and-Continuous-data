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


db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'中正(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'石化(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'林園(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'潮寮(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'永芳(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'昭明(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'溪埔(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'九曲(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'大樹(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'旗山(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'美濃(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'旗美(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'新威(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'清溪(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'海豐(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'前進\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'東港(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'新庄(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'萬丹(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'社皮(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'鹽埔(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'高樹(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'關福(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'高樹\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'赤山(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'佳佐   \'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'老埤(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'隘寮   \'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'西勢(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'大湖(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'大湖   \'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'新埤(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'萬隆(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'大嚮(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'餉潭(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'萬隆   \'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'水底寮 \'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'枋寮(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'大庄(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'德興(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'新園(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'崁頂(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'港東(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'崎峰(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'塭豐(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'瑪家(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 1 WHERE name like \'鳳鳴(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'中正(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'石化(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'昭明(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'潮寮\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'溪埔(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'大樹(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'中州(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'旗山(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'廣福\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'吉洋工作站\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'美濃(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'吉洋(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'新威(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'清溪(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'海豐(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'大潭(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'東港(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'新庄(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'萬丹(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'繁華(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'德協\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'麟洛\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'九如(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'土庫\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'里港(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'彭厝(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'高樹(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'泰山(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'新南(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'泰山\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'萬巒(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'赤山(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'建興(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'西勢(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'大湖(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'大嚮(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'餉潭(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'德興(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'港東(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'崎峰(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'塭豐(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'瑪家(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 2 WHERE name like \'西勢(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'林園(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'潮寮(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'永芳(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'昭明(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'溪埔(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'九曲(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'大樹(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'中州(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'吉洋(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'清溪(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'海豐(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'大潭(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'東港(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'新庄(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'萬丹(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'九如(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'里港(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'鹽埔(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'彭厝(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'泰山(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'關福(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'萬巒(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'赤山(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'建興(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'內埔(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'老埤(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'西勢(4)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'大湖(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'新埤(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'萬隆(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'枋寮(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'大庄(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'德興(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'崁頂(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'港東(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'崎峰(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'瑪家(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 3 WHERE name like \'新埤(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'林園(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'潮寮(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'永芳(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'昭明(4)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'大樹(4)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'前進(1)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'東港(4)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'繁華(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'新南(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'內埔(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'大湖(4)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'新埤(4)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'新園(2)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'崁頂(3)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'港東(4)\'');
db.query('UPDATE "Well_Stations" SET layer = 4 WHERE name like \'崎峰(4)\'');




'''

#取得測站以及日期清單
sites = db.query('select site, starttime, endtime from "Precipitation_Stations"').getresult()
# where site like \'C0V730\'

for site in sites:
        
    print('上傳至{site}測站'.format(site=site[0]))
    date = site[1]
    
    #檢查時間區段
    while( date <= site[2] ):
        filename = 'Pingtung/Precipitation/{site}/CWB_A_{site}_{yyyymm}.txt'.format(site=site[0], yyyymm=date.strftime('%Y%m'))
        print(filename)
        
        #讀取檔案
        try:
            for line in open(filename, 'r'):
                data = line.strip().split()
                if len(data) == 0 :
                    continue
                name = data[0]
                date2 = "{y}-{m}-{d} {h}:00".format(y=data[1][0:4], m=data[1][4:6], d=data[1][6:8], h=data[1][8:10])
                value = float(data[-2])
                db.insert('Precipitation', site=name, date=date2, value=value)
        except EOFError:
            print('找不到"{filename}"檔案'.format(filename))
        except:
            print('不明的程式中斷')

        #切換下一檔案時間
        date = date + datetime.timedelta(31)
        date = date - datetime.timedelta(date.day-1)
'''

