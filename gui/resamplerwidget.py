from PyQt4.QtGui import QWidget

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '3:50 PM'

class ResamplerWidget(QWidget):
  def __init__(self):
    ""
    self.tree=TreeView('resampler.json')