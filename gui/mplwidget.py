#!/usr/bin/env python

# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

# Matplotlib Figure object
import matplotlib.pyplot as plt

class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('title')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')


        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)


from matplotlib import pyplot, dates

class MplWidget(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        # set the layout to the vertical box
        self.setLayout(self.vbl)

    def plot_date(self,x, y, fmt='bo', tz=None, xdate=True, ydate=False, hold=None,
              **kwargs):
        ax = self.canvas.ax
        # allow callers to override the hold state by passing hold=True|False
        washold = ax.ishold()

        # print x
        if hold is not None:
            ax.hold(hold)
        try:
            ret = ax.plot_date(x, y, fmt=fmt, tz=tz, xdate=xdate, ydate=ydate,
                               **kwargs)
            # draw_if_interactive()
        finally:
            ax.hold(washold)

        return ret




    def update_labels(self,title,xLabel,yLabel):
        """"""
        self.canvas.set_window_title(title)
        # self.canvas.fig.set_label("Fig")
        self.canvas.ax.set_xlabel(xLabel)
        self.canvas.ax.set_ylabel(yLabel)
        self.canvas.ax.set_title(title)

