import re
import unittest
from weathergit.common.config import Config
from weathergit.common.smaputils import SmapUtils

POINT=dict(
    latitude='/garmin0/latitude',
    longitude='/garmin0/longitude',
    soil_moisture='/thetaprobe0/soil_moisture',
    soil_temp='/omega0/soil_temp',
    altitude='/garmin0/altitude',
    num_satellites='/garmin0/num_of_satellites'

)


class SmapUtilsTest(unittest.TestCase):
    def setUp(self):
        self.config=Config("../../common/weatherplotter.conf")
        self.c=SmapUtils()

    def test_get_curr_val(self):
        ""
        self.c.get_curr_val('/garmin0/latitude')
        self.c.get_curr_val('/garmin0/longitude')

