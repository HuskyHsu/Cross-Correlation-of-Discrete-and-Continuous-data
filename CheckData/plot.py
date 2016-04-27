#清除 variable explorer，避免汙染
from IPython import get_ipython 
get_ipython().magic('reset -sf')
"""
Plot Well data and Precipitation data

@author: Shih-Chi
"""
from matplotlib import dates     #繪圖時的時間處理
from pylab import *              #matplotlib 接口
from pg import DB
import numpy as np

db = DB(dbname='Pingtung', host='localhost', port=5432, user='postgres', passwd='husky')

eventtime = [datetime.date(2009, 8, 6), datetime.date(2009, 8, 13)]

def get_well_list(TR):
    #TR = time range
    sites = db.query('select site from "Well_Stations" where starttime < \'{st}\' and endtime > \'{et}\''.format( st = str(TR[0]), et = str(TR[1]))).getresult()
    return np.array([site[0] for site in sites])
   
def get_well_data(site, TR):
    datas = db.query('select date, value from "Well" where site = \'{site}\' and date >= \'{st}\' and date <= \'{et}\' order by date'.format(site = site, st = str(TR[0]), et = str(TR[1]))).getresult()
    return (np.array([data[0] for data in datas]), np.array([ float(data[1]) for data in datas]))

def get_P_list(TR):
    #TR = time range
    sites = db.query('select site from "Precipitation_Stations" where starttime < \'{st}\' and endtime > \'{et}\''.format( st = str(TR[0]), et = str(TR[1]))).getresult()
    return np.array([site[0] for site in sites])
   
def get_P_data(site, TR):
    datas = db.query('select date, value from "Precipitation" where site = \'{site}\' and date >= \'{st}\' and date <= \'{et}\' order by date'.format(site = site, st = str(TR[0]), et = str(TR[1]))).getresult()
    return (np.array([data[0] for data in datas]), np.array([ 0 if float(data[1]) < 0 else float(data[1]) for data in datas ]))
    

sites = get_well_list(eventtime)

for site in sites:
    time, data = get_well_data(site, eventtime)
    
    fig = figure(figsize=(12, 8), dpi=300)
    
    title('{site} ({ST}~{ET})'.format(site = site, ST = str(eventtime[0]), ET = str(eventtime[1])))
    plot(time, data, color='b', linewidth=1.5)
    fig.savefig('../../result/{ST}_{ET}/well/{site}.png'.format(site = site, ST = str(eventtime[0]), ET = str(eventtime[1])), dpi=200, bbox_inches='tight')
    print(site)


sites = get_P_list(eventtime)

for site in sites:
    time, data = get_P_data(site, eventtime)
    #print('{site}: {s}'.format(site=site, s=np.sum(data)))

    fig = figure(figsize=(12, 8), dpi=300)
    
    title('{site} ({ST}~{ET})'.format(site = site, ST = str(eventtime[0]), ET = str(eventtime[1])))
    plot(time, data, color='b', linewidth=1.5)
    fig.savefig('../../result/{ST}_{ET}/P/{site}.png'.format(site = site, ST = str(eventtime[0]), ET = str(eventtime[1])), dpi=200, bbox_inches='tight')
    print(site)

    