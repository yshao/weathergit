import pandas as pd
import matplotlib.pyplot as plt 

def myinterpolator(grp, cols = ['I', 'A', 'B', 'C', 'D', 'E']):
    ""
    index = pd.date_range(freq='1min',
            start=grp['t'][grp.first_valid_index()],
            end=grp['t'][grp.last_valid_index()])

    # print grp['t'].first_valid_index()
    # index = pd.date_range(freq='60T', start=ts.first_valid_index(), periods=5)
    # print grp['t'][0]
    print grp.first_valid_index()
    print grp.last_valid_index()

    print "index"
    print index
    print set(grp['t'])
    print set(grp['t']).union(index)

    print grp
    g1  = grp.reindex(set(grp.index).union(index)).sort_index()
    for col in cols:
        g1[col] = g1[col].interpolate('time').ix[index]
    g1['F'] = g1['E'].cumsum()    
    return g1 


def myplot(df, ilist, clist):
    df1 = df[df['I'].isin(ilist)][clist + ['I']]
    fig, ax = plt.subplots(len(clist))
    for I, grp in df1.groupby('I'):
        for j, col in enumerate(clist):
            grp[col].plot(ax=ax[j], sharex=True)


df = pd.read_csv("tinyexample.csv", sep=',', parse_dates=[1],
                 header=None, names=['I','t','A','B','C','D','E'])

print df
print type(df['t'])
print df['t']
###
import datetime
from pandas import *

dates = [datetime(2011, 1, 2, 1), datetime(2011, 1, 2, 2), datetime(2011, 1, 2, 3),
          datetime(2011, 1, 2, 4), datetime(2011, 1, 2, 5), datetime(2011, 1, 2, 6)]
ts = Series(np.arange(6.), index=dates)
print "0"
print ts

index = pd.date_range(freq='60T', start=ts.first_valid_index(), periods=5)
print ts.reindex(set(ts.index).union(index)).sort_index().interpolate('time').ix[index]

index = pd.date_range(freq='66T', start=ts.first_valid_index(), periods=5)
print index

print ts.reindex(set(ts.index).union(index)).sort_index().interpolate('time').ix[index]
print "1"


index = pd.date_range(freq='65T', start=ts.first_valid_index(), periods=5)
print index

print ts.reindex(set(ts.index).union(index)).sort_index().interpolate('time').ix[index]
print "2"


import datetime
your_timestamp = 1331856000000
date = datetime.datetime.fromtimestamp(your_timestamp / 1e3)

print date


print "3"
index = pd.date_range(freq='70T', start=ts.first_valid_index(), periods=10)
print ts.reindex(set(ts.index).union(index)).sort_index().interpolate('time').ix[index]

df1=DataFrame(np.random.randint(500, size=(500, 10)),
                       columns=list('abcdefghij'))

print df1

import time

def ctime(str):
    # print datetime.datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
    return calendar.timegm(time.strptime(str,'%Y-%m-%d %H:%M:%S'))


# df1=DataFrame(np.random.randint(300, size=(300, 1)),
#                        columns=list('counter'))


print df1

t1='2013-04-03 01:20:40'
# print datetime.datetime.strptime(t1,'%Y-%m-%d %H:%M:%S')
t2='2013-04-04 01:20:40'
# print datetime.datetime(t2)
t3='2013-04-05 01:20:40'
# print datetime.datetime(t3)

import calendar

time1=ctime(t1)

a= [None]*99
df=a+[ctime(t1)]+a+[ctime(t2)]+a+[ctime(t3)]
print "4"
print df

df2=DataFrame(df)

# print df2.interpolate("time")
print df2
print df2.interpolate()

def stime(num):
    print num
    return calendar.timegm(num)

df2.apply(stime)

print df2

### pytseries
# x = ma.arange(20)
# x[(x%4) !=0] = ma.masked
# print xprint forward_fille(x)

### interpolate counter val at 0 from timestamp_counter


###

### pandas data
for I, grp in df.groupby('I'):
    print I
    print grp

# ls=[grp for I, grp in df.groupby('I')]
# print ls

df_interpolated = pd.concat([myinterpolator(grp) for I, grp in df.groupby('I')])
myplot(df_interpolated, ilist=[1,4], clist=['F', 'A', 'C'])
plt.tight_layout()   