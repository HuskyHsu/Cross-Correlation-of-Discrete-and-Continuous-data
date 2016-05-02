#清除 variable explorer，避免汙染
from IPython import get_ipython 
get_ipython().magic('reset -sf')

#使用函示庫
#import numpy as np              #矩陣運算 (GetData中呼叫過，可略過)
#import matplotlib.pyplot as plt #繪圖 
#from matplotlib import dates     #繪圖時的時間處理
from pylab import *              #matplotlib 接口
#from datetime import datetime   #日期函數 (GetData中呼叫過，可略過)
#import time                     #計時器
import os                        #資料夾
import sys                       #file

#自訂模組
#import GetData.file as file
import GetData.db as db_         #資料庫讀取
import model.CrossCorrelation as CC #計算CrossCorrelation與繪圖


#tStart = time.time()            #計時開始

"""
0. 決定降雨時間段
1. 決定井
2. 決定雨量站
3. 計算交叉相關分析
4. 出圖
5. 紀錄結果(time window, lag time, r)
"""

#0 決定降雨時間段 與 第幾含水層
eventtime = [datetime.date(2007, 6, 5), datetime.date(2007, 6, 14)]
layer = 2

ROOT = r'E:\work\水利署計畫\result\{ST}_{ET}\layer{n}'.format( ST = str(eventtime[0]), ET = str(eventtime[1]), n = layer)

if not os.path.exists(ROOT):
    os.makedirs(ROOT)

file = open(os.path.join(ROOT, 'layer{n}.csv'.format(n=layer)), 'w')
file.write('site, r, w, l, x, y\n')

#1-1 get have data well list
sites = db_.get_well_list(eventtime, layer)

for site in sites:
    #1-2 get date
    time_w, water = db_.get_well_data(site, eventtime)

    #2.1 fine Precipitation closest to Well
    Psite = db_.get_near_PStations(site, eventtime)
	
    #2-2 get date
    time_P, rain = db_.get_P_data(Psite, eventtime)
    
    #去除資料長度不同測站(有缺才會不同，假設雨量資料無缺)
    if (len(water) != len(rain)):
        print('{w}:{w_l}, {P}:{P_l}'.format(w=site,w_l=len(water),P=Psite,P_l=len(rain)))
        continue

    #3. 設定 時間延遲 以及 時間尺度 計算交叉相關分析
    length = water.shape[0]
    window = 50
    lag = 30 
    
    try:
        #取得r 與 最大的r時的參數
        r, max_index = CC.cal_mat(water, rain, window, lag)
        try:
            #4. 出圖
            CC.printpng(site, Psite, r, max_index, water, rain, time_P, lag, window, length, eventtime, layer, ROOT)
        except:
            print('2')
    
        try:
            #5. 輸出參數
            x, y = db_.get_well_XY(site)
            file.write('{site}, {r}, {w}, {l}, {x}, {y}\n'.format( site=site, r=max_index.max_r, w=max_index.window, l=max_index.lag, x=x, y=y ))
        except:
            print('3')
        
        try:
            print('{site} r:{r}, window:{w}, lag:{l}'.format( site=site, r=max_index.max_r, w=max_index.window, l=max_index.lag ))
        except:
            print('4')
            
    except:
        print('1')
        file.close()
        
file.close()
print('over')

#tEnd = time.time()#計時結束
#print(tEnd - tStart)