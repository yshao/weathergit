from PyQt4.QtGui import QTreeView
from pyface.viewer.tree_viewer import TreeViewer
from attributetablemodel import AttributeTableModel

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/24/2015' '2:44 PM'




class EventViewer(TreeViewer):
    def __init__(self):
        ""

    def gen_event(self):
        e=self.render(Event())
        self.append(e)



    def remove_event(self):
        self.remove()

    def render(self):
        ""
        event=dict


        return event

