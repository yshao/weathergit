from smap.archiver.client import SmapClient
from weathergit.common.dataclient import DataClient
import numpy as np
import scipy.io

x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)

host='192.168.1.120'
port='8079'
startTime="12-8-2014"
endTime="12-9-2014"

c = SmapClient("http://"+host+":"+port)

from smap.contrib import dtutil

start = dtutil.dt2ts(dtutil.strptime_tz(startTime, "%m-%d-%Y"))
end   = dtutil.dt2ts(dtutil.strptime_tz(endTime, "%m-%d-%Y"))

uuid = [
  "63f6eb56-9bf4-5356-845a-80a315909d75"
]
b=False
while b==False:
    try:
        data = c.data_uuid(uuid, start, end)
        b=True
    # except Error as e:
    except Exception as e:
        print Exception, e
        if str(e) == 'float division by zero':
            b = False
# finally:



# print data
# print data.__class__.__name__

### list
import numpy as np
x = np.array([(1, 'O', 1)],
             dtype=np.dtype([('step', 'int32'),
                             ('symbol', '|S1'),
                             ('index', 'int32')]))

print x
print x.dtype.names


FLOAT='float'
nd=data[0]

# print nd

print "SUBSET"
print nd.shape
# nd=nd.tolist()
# print len(data[0])
# print data[0][0].__class__.__name__
# print data[0].__class__.__name__
# rows=data[0]
# print rows
# print data.__class__.__name__
# ldata=data.tolist()
# fmt = ",".join(["%s"] + ["%10.6e"] * (a.shape[1]-1))
#
# print ldata
# print data.shape

# nd=np.array(nd ,dtype=[('time','<f4'), ('pressure','<f4')])
# print nd.shape
# print nd['time']
# rowheader=['a','b']
# nd.insert(0,rowheader)
# print nd[0]
# print nd[1]
# print nd.dtype.names

# nd1=np.array([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)], dtype=[('a', '<f4'), ('b', '<f4'),('c', '<f4')])
# print nd1
# print nd1.dtype.names

# ,dtype=[('time',FLOAT),('pressure',FLOAT)]


np.array(ll)

ll=nd.tolist()
# print ll
print np.array(ll,dtype=np.dtype([('step', 'float32'),
                             ('symbol', 'float32')]))

def data_to_mat(filep,data):
    header=('time','pressure')

    scipy.io.savemat(filep, data)

def data_to_csv(filep,nd):
    ""
    header=('time','pressure')
    with open(filep, 'w') as datafile:
      datafile.write(', '.join(header) + '\n')
      np.savetxt(datafile, nd, fmt='%f, %f')

def upload_csv(filep,uuid):
    ""

# data_to_matlab(data)
# print nd
data_to_csv('data.csv',nd)

data_to_mat('data.mat',nd)

upload_csv()