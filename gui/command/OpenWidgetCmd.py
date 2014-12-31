import sys
from weathergit.gui.command.command import Command
from weathergit.gui.configparserwidget import pyGTKConfigParser

try:
    import pygtk
    pygtk.require("2.0")
    import gtk, gobject
    gobject.threads_init()
    gtk.gdk.threads_init()
except:
    print >> sys.stderr, "You need to install the python gtk bindings"
    sys.exit(1)

class OpenWidgetCmd(Command):
    # DIALOG={"ConfigEditor":ConfigEditor,}
    def __init__(self,args):
        self.args=args

    def execute(self):
        ""
        gobject.threads_init()
        # args=
        pyGTKConfigParser()

        #initialize threading system, must be before gtk.main
        gtk.gdk.threads_init()

        #run main gtk
        gtk.main()
        return