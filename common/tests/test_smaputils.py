import os
import re
import unittest
# from weathergit.server.client import SmapClient
# from weathergit.common.dataclient import DataClient
from weathergit.common.config import Config
from weathergit.common.smaputils import SmapUtils

from xlwings import Workbook, Sheet, Range
import numpy as np

POINT=dict(
    latitude='/garmin0/latitude',
    longitude='/garmin0/longitude',
    soil_moisture='/thetaprobe0/soil_moisture',
    soil_temp='/omega0/soil_temp',
    altitude='/garmin0/altitude',
    num_satellites='/garmin0/num_of_satellites',
    speed='/garmin0/speed',
)


def export_csv(streamp,startdt,enddt):
    # dc=DataClient()

    opt='EXCEL'
    # data=dc.load_data(streamp,startdt,enddt)
    if opt == 'EXCEL':

        wb=Workbook("test.xlsx")
        wb.caller()
        n = Range('Sheet1', 'B1').value  # Write desired dimensions into Cell B1
        rand_num = np.random.randn(n, n)
        # Range('Sheet1', 'C3').value = rand_num
        # Range('Sheet2', 'A1').value = data

# def load_csv(filep,streamp):
#     ""
#     sc=SmapClient()
#
#     sc.load_csv(filep)

path='/garmin0/altitude'
startdt=""
enddt=""
fpath=re.replace(path,'/','_')+'.xlsx'

export_csv(path,startdt,enddt)
# assert os.path.exists(fpath)

# class SmapUtilsTest(unittest.TestCase):
#     EXCEL=1
#
#     def setUp(self):
#         self.config=Config("../../common/weatherplotter.conf")
#         self.c=SmapUtils()
#
#     def test_get_curr_val(self):
#         ""
#         self.c.get_curr_val('/garmin0/latitude')
#         self.c.get_curr_val('/garmin0/longitude')
#
#     def test_load_csv(self):
#         ""
#
#     def test_export_csv(self):
#         ""
#
#         # self.c.
#         # opts={'EXCEL',excel}
#         # value=
#         # method_name = 'visit_' + str(value)
#         # switch (opts)
#         #
#         # case EXCEL:
#         #
#         # case CSV:
#
#
#
#
#
