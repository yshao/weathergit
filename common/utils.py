import os
import pandas as pd
import scipy


def csv2mat(filep,outfilp):
    basename=os.path.basename(filep)
    data = pd.io.read_csv(basename+".csv",parse_dates=True)
    scipy.io.savemat(basename+'.mat',data)



class DaqException(Exception):
    """Generic error"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code

class DeviceException(Exception):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code


class WXT520Exception(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code 
        
class GPS18xLVCException(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code        
        
        
class MLxException(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code

class TrendNetException(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code


class PRACOException(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code
        
