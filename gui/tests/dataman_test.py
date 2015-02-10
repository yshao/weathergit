import unittest
from PyQt4 import QtGui
from gui.ui_datamanwidget import Ui_datamanwidget


login={'conn_string':'','update'}

conn_string = "" % login

update_enable = self.ui.inUpdateEnable.value()
update_interval = self.ui.inUpdateInterval.value()

time_segment_size = self.ui.inTimeSegmentSize.value()

formula_list = self.ui.inFormulatList




class datamanWidget(QtGui.QWidget):
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(datamanWidget, self).__init__(parent)
        self.ui = Ui_datamanwidget()
        self.ui.setupUi(self)

    def populate_formulat_list(self):
        self.ui




class ConversionTest(unittest.TestCase):
    def setUp(self):
        widget=datamanWidget()
        assert update_enable
        assert update_interval == time
        assert time_segment_size == time
        assert formula_list == ['','']

    def test_connection(self):
        assert db.connected == True

    def test_timeSyncOperator(self):


    def test_soilValuesOperator(self):
        target_id_1='soil_temp'



        target_id_2='soil_moisture'

        unit == '%'
        unit == 'C'





