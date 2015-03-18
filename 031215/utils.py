import os
import pandas as pd
import scipy
import time


def csv2mat(filep,outfilp):
    basename=os.path.basename(filep)
    data = pd.io.read_csv(basename+".csv",parse_dates=True)
    scipy.io.savemat(basename+'.mat',data)


def get_timestamp():
    timestr = time.strftime("%Y%m%d%H%M%S")
    return timestr


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
