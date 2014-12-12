import sip
sip.setapi('QString', 2)

from PyQt4 import QtGui
from common.dbconn import DbConn
from common.config import Config

from gui.mplwidget import MplWidget
from gui.weatherclient import WeatherClient

config=Config("../../common/weatherplotter.conf")


# try:
import sys

app = QtGui.QApplication(sys.argv)
plotter = WeatherClient()
plotter.setConfig(config)
plotter.show()
sys.exit(app.exec_())

# except Exception,e:
#     print e
