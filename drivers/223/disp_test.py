from PyQt4 import QtGui
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)



from PyQt4.QtGui import QApplication, QWidget, QTextEdit, QGridLayout, QLineEdit, QCheckBox, QSpinBox, QComboBox, \
    QMainWindow
from pyqtconfig import ConfigManager
import sys


class DispWidget(QtGui.QWidget):
    def __init__(self):
        super(DispWidget, self).__init__()


    def slotResult(self):
        ""
        i=0
        print self.vis.as_dict()
        for item in self.vis.as_dict().keys():
            te = QLineEdit()
            te.setEnabled(False)
            self.vis.add_handler(item,te)
            gd.addWidget(te,i,1)
            i=i+1


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('PyQtConfig Demo')
        self.vis = ConfigManager()
        #
        # CHOICE_A = 1
        # CHOICE_B = 2
        # CHOICE_C = 3
        # CHOICE_D = 4
        #
        # map_dict = {
        #     'Choice A': CHOICE_A,
        #     'Choice B': CHOICE_B,
        #     'Choice C': CHOICE_C,
        #     'Choice D': CHOICE_D,
        # }

        self.vis.set_defaults({
            'text1': 'hello1',
            'text2': 'hello2',
            'text3': 'hello3',
            'text4': 'hello4',
        })

        # self.vis.set_defaults({
        #     'number': 13,
        #     'text': 'hello',
        #     'active': True,
        #     'combo': CHOICE_C,
        # })

        gd = QGridLayout()
        #
        # sb = QSpinBox()
        # gd.addWidget(sb, 0, 1)
        # self.vis.add_handler('number', sb)
        #
        # te = QLineEdit()
        # gd.addWidget(te, 1, 1)
        # self.vis.add_handler('text', te)
        #
        # cb = QCheckBox()
        # gd.addWidget(cb, 2, 1)
        # self.vis.add_handler('active', cb)
        #
        # cmb = QComboBox()
        # cmb.addItems(map_dict.keys())
        # gd.addWidget(cmb, 3, 1)
        # self.vis.add_handler('combo', cmb, mapper=map_dict)
        #
        # self.current_config_output = QTextEdit()
        # gd.addWidget(self.current_config_output, 0, 3, 3, 1)

        i=0
        print self.vis.as_dict()
        for item in self.vis.as_dict().keys():
            te = QLineEdit()
            te.setEnabled(False)
            self.vis.add_handler(item,te)
            gd.addWidget(te,i,1)
            i=i+1

        # self.vis.updated.connect(self.show_config)

        # self.show_config()

        self.window = QWidget()
        self.window.setLayout(gd)
        self.setCentralWidget(self.window)
    #
    # def show_config(self):
    #     self.current_config_output.setText(str(self.vis.as_dict()))

# Create a Qt application
app = QApplication(sys.argv)
app.setOrganizationName("PyQtConfig")
app.setOrganizationDomain("martinfitzpatrick.name")
app.setApplicationName("PyQtConfig")

w = MainWindow()
w.show()
app.exec_()  # Enter Qt application main loop
