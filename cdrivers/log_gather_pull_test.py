from PyQt4 import Qt
from PyQt4.QtGui import QStandardItemModel, QCompleter, QLineEdit


def populate_source_client_cmds():
    word_list=["alpha","omega","omicron","zeta"]
    self.ui.comboBox.clear()
    self.ui.comboBox.addItems(word_list)
    completer = QCompleter(word_list)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    # lineEdit = QLineEdit()
    self.ui.lineEdit.setCompleter(completer);

