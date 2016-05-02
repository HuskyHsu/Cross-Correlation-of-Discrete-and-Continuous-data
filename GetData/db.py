# read file


from pg import DB
import numpy as np

db = DB(dbname='Pingtung', host='localhost', port=5432,
    user='postgres', passwd='husky')
    
#井位清單(時間範圍, 第幾含水層)
def get_well_list(TR, layer):
    #TR = time range
    sites = db.query('select site from "Well_Stations" where starttime < \'{st}\' and endtime > \'{et}\' and layer = {layer}'.format( st = str(TR[0]), et = str(TR[1]), layer = layer)).getresult()
    return np.array([site[0] for site in sites])
   
#井資料(站名, 時間範圍)
def get_well_data(site, TR):
    datas = db.query('select date, value from "Well" where site = \'{site}\' and date >= \'{st}\' and date <= \'{et}\' order by date'.format(site = site, st = str(TR[0]), et = str(TR[1]))).getresult()
    return (np.array([data[0] for data in datas]), np.array([ float(data[1]) for data in datas]))
    
#井座標資料(站名)
def get_well_XY(site):
    siteXY = db.query('select "TWD97_X", "TWD97_Y" from "Well_Stations" where site = \'{site}\''.format(site = site)).getresult()
    return (float(siteXY[0][0]), float(siteXY[0][1]))
        
#井座標資料(站名)
def get_P_XY(site):
    siteXY = db.query('select "TWD97_X", "TWD97_Y" from "Precipitation_Stations" where site = \'{site}\''.format(site = site)).getresult()
    return (float(siteXY[0][0]), float(siteXY[0][1]))
        

#尋找最近的雨量站(站名, 時間範圍)
def get_near_PStations(site_w, TR):
    siteXY = db.query('select "TWD97_X", "TWD97_Y" from "Well_Stations" where site = \'{site}\''.format(site = site_w)).getresult()
    x = float(siteXY[0][0])
    y = float(siteXY[0][1])
    PStations = db.query('select site from "Precipitation_Stations" where starttime < \'{st}\' and endtime > \'{et}\' order by POWER(POWER("TWD97_X"-{x},2) + POWER("TWD97_Y"-{y},2), 0.5) limit 1;'.format(x = x, y = y, st = str(TR[0]), et = str(TR[1]) )).getresult()
    return PStations[0][0]

#雨量資料(站名, 時間範圍)	
def get_P_data(site_P, TR):
    datas = db.query('select date, value from "Precipitation" where site = \'{site}\' and date >= \'{st}\' and date <= \'{et}\' order by date'.format(site = site_P, st = str(TR[0]), et = str(TR[1]))).getresult()
    return (np.array([data[0] for data in datas]), np.array([ 0 if float(data[1]) < 0 else float(data[1]) for data in datas ]))
    