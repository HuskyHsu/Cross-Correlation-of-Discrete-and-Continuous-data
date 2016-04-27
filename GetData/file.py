# read file

import numpy as np
#import datetime as dt
from datetime import datetime

def read(name):
    return np.array([float(line.split('\t')[1].rstrip('\n')) for line in open(name, 'r')])
    
def readXY(name):
    x, y = [], []
    for line in open(name, 'r'):
        
        #tem = line.split('\t')[0].split('-')
        #x.append(dt.datetime(int(tem[0]), int(tem[1]), int(tem[2]), int(tem[3]), 0))
        x.append(datetime.strptime(line.split('\t')[0], "%Y-%m-%d-%H"))
        #x.append(line.split('\t')[0].rstrip('\n'))
        y.append(float(line.split('\t')[1].rstrip('\n')))
    return (np.array(x), np.array(y))