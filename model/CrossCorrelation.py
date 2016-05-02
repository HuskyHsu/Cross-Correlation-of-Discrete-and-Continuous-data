"""
Cross Correlation

[function] cal(water, rain, window, lag)
[function] cal_mat(water, rain, window, lag)
[function] printpng(site_w, site_P, r, max_index, water, rain, time_P, lag, window, length)
[class] where_max(window, lag, max_r)

author: Shih-Chi
"""

import numpy as np
from matplotlib import dates     #繪圖時的時間處理
from pylab import *              #matplotlib 接口
import os                        #資料夾

#計算單一值
def cal(water, rain, window, lag):
    #check water length as same as rain length
    if water.shape != rain.shape:
        return
    
    length = rain.shape[0]

    water_diff = np.array([water[i]-water[i-window] for i in range(window,length)])
    rain_diff = np.array([np.sum(rain[i-window+1:i+1]) for i in range(window,length)])

    return np.corrcoef(water_diff[lag : length - window], rain_diff[0 : length - window - lag])[0][1]

#計算矩陣值
def cal_mat(water, rain, window, lag):
    
    max_index = where_max(0, 0, -999.9)    
    r = np.zeros((window, lag))
    
    for i in np.arange(0, window):
        for j in np.arange(0, lag):
            r[i][j] = cal(water, rain, i+1, j+1)
            if max_index.max_r < r[i][j]:
                max_index.window = i+1
                max_index.lag = j+1
                max_index.max_r = r[i][j]
            
    return (r, max_index)

#出圖
def printpng(site_w, site_P, r, max_index, water, rain, time_P, lag, window, length, TR, layer, ROOT):
    fig = figure(figsize=(12, 8), dpi=300)
    
    #fig.1 time window & lag
    subplot(4, 1, 1)
    pc1 = pcolor(r, vmin=-1, vmax=1)
    xlim(1, lag), ylim(1, window)
    xlabel("lag time(hr)"), ylabel("Time window(hr)")
    title('{site_w} Cross Correlation {site_P} (Max Correlation is {MC} in time window = {MTW}hr, lag time = {MLT}hr)'.format(site_w=site_w, site_P=site_P, MTW=max_index.window, MLT=max_index.lag, MC = round(max_index.max_r, 2)))

    cbar_ax = fig.add_axes([0.95, 0.789, 0.02, 0.168])
    fig.colorbar(pc1, cax=cbar_ax, ticks=[-1, -0.5, 0, 0.5, 1])

    #fig.2 time window = 1
    ax1 = subplot(4,1,2)
    ax2 = ax1.twinx()

    tem = np.array([water[i] - water[i-1] for i in range(1, length)])

    ax1.xaxis.set_major_locator(dates.DayLocator(interval=2))
    ax1.xaxis.set_major_formatter(dates.DateFormatter('%y/%m/%d'))
    ax2.xaxis.set_major_locator(dates.DayLocator(interval=2))
    ax2.xaxis.set_major_formatter(dates.DateFormatter('%y/%m/%d'))

    #lns1 = ax1.step(time[1:length], rain[1:length], where='mid', linewidth=1.5, label='1hr Accumulated Precipitation')
    #lns2 = ax2.step(time[1:length], tem, where='mid', color='g', linewidth=1.5, label='1hr Difference Groundwater')

    lns1 = ax1.plot(time_P[1:length], rain[1:length], color='b', linewidth=1.5, label='1hr Accumulated Precipitation')
    lns2 = ax2.plot(time_P[1:length], tem, color='g', linewidth=1.5, label='1hr Difference Groundwater')

    # added these three lines
    lns = lns1+lns2
    labs1 = [l.get_label() for l in lns]
    ax2.legend(lns, labs1, loc='upper right')

    ax1.set_xlim(time_P[1], time_P[length-1])
    ax2.set_xlim(time_P[1], time_P[length-1])
    ax1.set_ylim(0, np.max(rain)*1.2)
    ax2.set_ylim(-np.max(np.abs(tem))*1.1, np.max(np.abs(tem))*1.1)
    ax1.set_xlabel("Time Series(hr)"), ax1.set_ylabel("Precipitation(mm)")
    ax2.set_ylabel("Diff Groundwater(m)")

    ax1.grid()
    del tem


    #fig.3 max r of time window
    ax3 = subplot(4,1,3)
    ax4 = ax3.twinx()

    tem_r = np.array([np.sum(rain[i-max_index.window+1:i+1]) for i in range(max_index.window, length)])
    tem_w = np.array([water[i] - water[i-max_index.window] for i in range(max_index.window, length)])

    lns3 = ax3.plot(time_P[max_index.window:length], tem_r, color='b', linewidth=1.5, label= '{0}{1}'.format(max_index.window, 'hr Accumulated Precipitation'))
    lns4 = ax4.plot(time_P[max_index.window:length], tem_w, color='g', linewidth=1.5, label= '{0}{1}'.format(max_index.window, 'hr Difference Groundwater'))

    lns = lns3+lns4
    labs2 = [l.get_label() for l in lns]
    ax4.legend(lns, labs2, loc='upper right')

    ax3.set_xlim(time_P[max_index.window], time_P[length-1])
    ax4.set_xlim(time_P[max_index.window], time_P[length-1])
    ax3.set_ylim(0, np.max(tem_r)*1.2)
    ax4.set_ylim(np.min(np.abs(tem_w))*0.8, np.max(np.abs(tem_w))*1.1)
    ax3.set_xlabel("Time Series(hr)"), ax3.set_ylabel("Precipitation(mm)")
    ax4.set_ylabel("Diff Groundwater(m)")

    ax3.xaxis.set_major_locator(dates.DayLocator(interval=2))
    ax3.xaxis.set_major_formatter(dates.DateFormatter('%y/%m/%d'))
    ax4.xaxis.set_major_locator(dates.DayLocator(interval=2))
    ax4.xaxis.set_major_formatter(dates.DateFormatter('%y/%m/%d'))
    
    ax3.grid()
    del tem_r, tem_w

    #fig.4 r of max time window
    subplot(4,1,4)
    plot(np.array([i for i in range(1, lag+1)]), np.array([cal(water, rain, max_index.window, i) for i in range(1, lag+1)]), color="blue", linewidth=1.5, linestyle="-", label= 'Correlation of Time window {0}hr'.format(max_index.window))
    plot(np.array([i for i in range(1, lag+1)]), np.array([cal(water, rain, 1, i) for i in range(1, lag+1)]), color="red", linewidth=1.5, linestyle="-", label= 'Correlation of Time window 1hr')
    xlim(1, lag), ylim(-1, 1)
    xlabel("lag time(hr)"), ylabel("Correlation")
    grid()
    legend()

    fig.tight_layout()
    
    fig.savefig(os.path.join(ROOT, '{site_w}_{site_P}.png'.format(site_w = site_w,site_P = site_P)), dpi=200, bbox_inches='tight')
    #fig.savefig("../result/{S}_{E}/layer{layer}/{site_w}_{site_P}.png".format(site_w = site_w,site_P = site_P, S=str(TR[0]), E=(TR[1]), layer = layer), dpi=200, bbox_inches='tight')
    
    close('all')
    return '{site_w} {site_P} cal and save png [OK]'.format(site_w = site_w,site_P = site_P)

class where_max:
    def __init__(self, window, lag, max_r):
        self.window = window
        self.lag = lag
        self.max_r = max_r
        
    def __str__(self):
        return '{0}, {1}, {2}'.format(self.window, self.lag, self.max_r)
        