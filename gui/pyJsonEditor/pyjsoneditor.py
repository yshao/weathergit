#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
if not sys.getdefaultencoding() == "utf-8":
    reload(sys)
    sys.setdefaultencoding("utf-8")
sys.setrecursionlimit(10000)
import platform


ShouldExit = False


if not sys.version_info[0:2] in [(2, 5), (2, 6), (2, 7)]:
    print "Your Python version is %s" % platform.python_version()
    print "Python version 2.5 or 2.6 or 2.7 is needed." + "\n"
    ShouldExit = True



try:
    from _ordereddict import ordereddict, sorteddict
except ImportError:
    print "ordereddict (a version of dict that keeps keys in insertion/sorted order) is required."
    print "You can find it here: http://www.xs4all.nl/~anthon/Python/ordereddict/" + "\n"
    ShouldExit = True


try:
    from chardet.universaldetector import UniversalDetector
except ImportError:
    print "chardet (Universal Encoding Detector) is required."
    print "You can find it here: http://chardet.feedparser.org" + "\n"
    ShouldExit = True


try:
    import simplejson
    if not simplejson.__version__ >= "2.1.2":
        raise ValueError
except ValueError:
    print "Your simplejson version is %s" % simplejson.__version__
    print "simplejson version '2.1.2' is needed. (at least Revision: r232)"
    print "You can find it here: http://code.google.com/p/simplejson/source/checkout" + "\n"
    ShouldExit = True
except ImportError:
    print "simplejson (simple, fast, extensible JSON encoder/decoder for Python) is required."
    print "You can find it here: http://code.google.com/p/simplejson/source/checkout" + "\n"
    ShouldExit = True
    
    
try:
    from PyQt4 import QtCore, QtGui
except ImportError:
    print "PyQt4 (Qt4 bindings for Python) is required."
    print "You can find it here: http://www.riverbankcomputing.co.uk" + "\n"
    ShouldExit = True
    


if ShouldExit:
    sys.exit()
    

import os
import time
import codecs
import socket
from BaseHTTPServer import BaseHTTPRequestHandler
import urllib2
import qrc_resources
from decimal import Decimal
import cStringIO


if not os.path.dirname(sys.argv[0]) == "":
    os.chdir(os.path.dirname(sys.argv[0]))
    

from ui_mainwindow import Ui_MainWindow
from input_dialog import Input_Dialog
from find_dialog import Find_Dialog

socket.setdefaulttimeout(10)

__version__ = "1.2"

__nan__ = Decimal(str(float("NaN")))
__inf__ = Decimal(str(float("Infinity")))



def list2dict(lst):
    d = ordereddict()
    for i in xrange(len(lst)):
        d[i] = lst[i]
    return d


def getODict(d, b=True):
    return ordereddict(d, relax=b)


def detectEncoding(fileStr):
    detector = UniversalDetector()
    for line in fileStr.splitlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result


def getFirstOrdinalOf(text):
    if len(text) == 0:
        return sys.maxunicode
    else:
        return ord(text[0])







class Iter(QtGui.QTreeWidgetItemIterator):
    def __init__(self, parent):
        QtGui.QTreeWidgetItemIterator.__init__(self, parent)
    
    def next(self):
        self.__iadd__(1)
        value = self.value()
        if value:
            return self.value()
        else:
            raise StopIteration
    
    def previous(self):
        self.__isub__(1)
        value = self.value()
        if value:
            return self.value()
        else:
            raise StopIteration





class Report(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.connect(self,QtCore.SIGNAL("addNode(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),self.addNode,QtCore.Qt.DirectConnection)
        self.connect(self,QtCore.SIGNAL("addLeaves(PyQt_PyObject,PyQt_PyObject)"),self.addLeaves,QtCore.Qt.DirectConnection)
        self.connect(self,QtCore.SIGNAL("getJson(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),self.getJson,QtCore.Qt.DirectConnection)
        self.connect(self,QtCore.SIGNAL("parseJson(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),self.parseJson,QtCore.Qt.DirectConnection)
        self.connect(self,QtCore.SIGNAL("makeRoot(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),self.makeRoot,QtCore.Qt.DirectConnection)

        
        self.responses = BaseHTTPRequestHandler.responses
        self.log_file = codecs.open("log.txt", "a+", "utf-8")
        self.error_message = "Couldn't get file"
        
        ########################
        self.data = {}
        self.jsonEncoding = {}
        ########################

        
        
        
    def handleUrl(self, currentTabNum, request):
        if str(type(request)) == "<type 'cStringIO.StringO'>":
            json_str = request
            request = None
        elif os.path.isfile(request) == True:
            try:
                json_str = open(request ,"r")
            except Exception, e:
                self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>Couldn't open file</b><br><br><u>Details:</u> <i>%s</i>" % e.__str__())
                json_str = (str(e.__class__), e.__str__(), request)
        else:
            if not request.startswith("http://") and not request.startswith("ftp://") and not request.startswith("https://") and not request.startswith("ftps://"):
                request = "http://" + request
            request = urllib2.quote(request.encode("utf-8"), safe=";/?:@&=+$,")
            
            Request = urllib2.Request(request)
            #Request.add_header('Referer', 'http://alpha-beta-pisi.blogspot.com/')
            try:
                json_str = urllib2.urlopen(Request)
            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    if hasattr(e.reason, 'args'):
                        if len(e.reason.args) >= 2:
                            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>Failed to reach the server</b><br><br>Reason: <i>%s</i><br><br><b>%s</b>" % (e.reason.args[1],self.error_message))
                            json_str = ('has_reason', str(e.reason.args[1]), Request.get_full_url())
                        else:
                            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>Failed to reach the server</b><br><br>Reason: <i>%s</i><br><br><b>%s</b>" % (e.reason.args[0],self.error_message))
                            json_str = ('has_reason', str(e.reason.args[0]), Request.get_full_url())
                    else:
                        self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>Failed to reach the server</b><br><br>Reason: <i>%s</i><br><br><b>%s</b>" % (e.reason,self.error_message))
                        json_str = ('has_reason', str(e.reason), Request.get_full_url())
                elif hasattr(e, 'code'):
                    self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>The server couldn't fulfill the Request</b><br><br><u>Error code:</u> <b>%d(%s)</b><br><br><u>Details:</u> <i>%s</i><br><br><b>%s</b>" % (e.code,self.responses[e.code][0],self.responses[e.code][1],self.error_message))
                    json_str = ('has_code', e.code, Request.get_full_url())
            
            except Exception, e:
                self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>An error occured</b><br><br><u>Details:</u> <i>%s</i><br><br><b>%s</b>" % (e.__str__(), self.error_message))
                json_str = (str(e.__class__), e.__str__(), Request.get_full_url())

        self.emit(QtCore.SIGNAL("getJson(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), currentTabNum, request, json_str)
        
        
        
    
    def getJson(self, currentTabNum, request, json_str):
        charset = None
        try:
            if isinstance(json_str, file):
                temp = json_str.read()
                lastModified = str(os.path.getmtime(json_str.name))
            elif json_str.__class__.__name__ == 'addinfourl':
                temp = json_str.read()
                lastModified = ""
                try:
                    charset = json_str.headers.getparam("charset")
                except:
                    pass
            elif request == None:
                temp = json_str.getvalue()
                lastModified = ""
            elif isinstance(json_str, tuple):
                self.log_file.write("Time: %s" % time.asctime() + "\n")
                self.log_file.write("Function: %s" % "getJson" + "\n")
                self.log_file.write("Exception: %s->%s->%s" % json_str + "\n\n")
                return

        except IOError, t:
            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject, PyQt_PyObject)"), currentTabNum, u"<b>IOError</b><br><br><u>Details:</u> <i>%s</i><br><br><b>%s</b>" % (t.__str__(), self.error_message))
            self.log_file.write("Time: %s" % time.asctime() + "\n")
            self.log_file.write("Function: %s" % "getJson" + "\n")
            self.log_file.write("Exception: %s->%s->%s" % (str(t.__class__), t.__str__(), request) + "\n\n")
            return
        except socket.error, t:
            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>socket error</b><br><br><u>Details:</u> <i>%s</i><br><br><b>%s</b>" % (t.__str__(), self.error_message))
            self.log_file.write("Time: %s" % time.asctime() + "\n")
            self.log_file.write("Function: %s" % "getJson" + "\n")
            self.log_file.write("Exception: %s->%s->%s" % (str(t.__class__), t.__str__(), request) + "\n\n")
            return
        except Exception, t:
            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>An error occured</b><br><br><u>Details:</u> <i>%s</i><br><br><b>%s</b>" % (t.__str__(), self.error_message))
            self.log_file.write("Time: %s" % time.asctime() + "\n")
            self.log_file.write("Function: %s" % "getJson" + "\n")
            self.log_file.write("Exception: %s->%s->%s" % (str(t.__class__), t.__str__(), request) + "\n\n")
            return
        finally:
            try:
                json_str.close()
            except:
                pass
        
        self.emit(QtCore.SIGNAL("parseJson(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), currentTabNum, request, lastModified, charset, temp)
        
        
        
        
    
    def parseJson(self, currentTabNum, request, lastModified, charset, temp):
        try:
            self.jsonEncoding[currentTabNum] = "utf-8"
            self.data[currentTabNum] = simplejson.loads(temp, parse_constant=Decimal, object_pairs_hook=getODict, use_decimal=True)
        except ValueError, e:
            if isinstance(e, UnicodeError):
                if charset:
                    try:
                        self.jsonEncoding[currentTabNum] = charset
                        self.data[currentTabNum] = simplejson.loads(temp, encoding=self.jsonEncoding[currentTabNum], parse_constant=Decimal, object_pairs_hook=getODict, use_decimal=True)
                    except UnicodeError:
                        try:
                            self.jsonEncoding[currentTabNum] = detectEncoding(temp)["encoding"]
                            self.data[currentTabNum] = simplejson.loads(temp, encoding=self.jsonEncoding[currentTabNum], parse_constant=Decimal, object_pairs_hook=getODict, use_decimal=True)
                        except UnicodeError, f:
                            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>%s</b><br><br><b>Reason:</b> %s" % (f.__class__.__name__, f.__str__()))
                            return
                        except simplejson.JSONDecodeError, f:
                            try:
                                self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, [unicode(temp, self.jsonEncoding[currentTabNum]), f, u"<b>%s</b><br><br><b>Reason:</b> %s" % (f.__class__.__name__, f.__str__())])
                            except Exception, g:
                                self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, "<b>%s</b> (Invalid JSON)<br><br><b>Reason:</b> %s" % (g.__class__.__name__, g.__str__()))
                            return
                    except simplejson.JSONDecodeError, f:
                        try:
                            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, [unicode(temp, self.jsonEncoding[currentTabNum]), f, u"<b>%s</b><br><br><b>Reason:</b> %s" % (f.__class__.__name__, f.__str__())])
                        except Exception, g:
                            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, "<b>%s</b> (Invalid JSON)<br><br><b>Reason:</b> %s" % (g.__class__.__name__, g.__str__()))
                        return
                else:
                    try:
                        self.jsonEncoding[currentTabNum] = detectEncoding(temp)["encoding"]
                        self.data[currentTabNum] = simplejson.loads(temp, encoding=self.jsonEncoding[currentTabNum], parse_constant=Decimal, object_pairs_hook=getODict, use_decimal=True)
                    except UnicodeError, f:
                        self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, u"<b>%s</b><br><br><b>Reason:</b> %s" % (f.__class__.__name__, f.__str__()))
                        return
                    except simplejson.JSONDecodeError, f:
                        try:
                            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, [unicode(temp, self.jsonEncoding[currentTabNum]), f, u"<b>%s</b><br><br><b>Reason:</b> %s" % (f.__class__.__name__, f.__str__())])
                        except Exception, g:
                            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, "<b>%s</b> (Invalid JSON)<br><br><b>Reason:</b> %s" % (g.__class__.__name__, g.__str__()))
                        return
            else:
                try:
                    self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, [unicode(temp, self.jsonEncoding[currentTabNum]), e, u"<b>%s</b><br><br><b>Reason:</b> %s" % (e.__class__.__name__, e.__str__())])
                except Exception, g:
                    self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, "<b>%s</b> (Invalid JSON)<br><br><b>Reason:</b> %s" % (g.__class__.__name__, g.__str__()))
                return
        
        self.emit(QtCore.SIGNAL("makeRoot(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), currentTabNum, request, lastModified)

        

        
        

        
    def makeRoot(self, currentTabNum, request, lastModified):
        if isinstance(self.data[currentTabNum], dict):
            root = QtGui.QTreeWidgetItem(None)
            root.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
            root.setText(0,"JSON")
            root.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.emit(QtCore.SIGNAL("addLeaves(PyQt_PyObject,PyQt_PyObject)"), [root], self.data[currentTabNum].items())
        elif isinstance(self.data[currentTabNum], list):
            root = QtGui.QTreeWidgetItem(None)
            root.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(2))
            root.setText(0,"JSON")
            root.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.emit(QtCore.SIGNAL("addLeaves(PyQt_PyObject,PyQt_PyObject)"), [root], getODict(list2dict(self.data[currentTabNum])).items())
        else:
            self.emit(QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, "A JSON payload should be a dict or list.")
            #del root
            return
        
        rootClone = root.clone()
        self.emit(QtCore.SIGNAL("makeTree(PyQt_PyObject)"), [currentTabNum, rootClone, self.data[currentTabNum], self.jsonEncoding[currentTabNum], request, lastModified])
        
#        del root
#        for i in [self.data, self.jsonEncoding]:
#            try:
#                del i[currentTabNum]
#            except:
#                pass
        
        
        
        

        
    
    def addLeaves(self, node, items):
        for key, value in items:
            self.emit(QtCore.SIGNAL("addNode(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), node, key, value)
        
                
    
    def addNode(self, node, key, value):
        if isinstance(value, dict):
            noded = QtGui.QTreeWidgetItem(node[0])
            noded.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
        elif isinstance(value, list):
            noded = QtGui.QTreeWidgetItem(node[0])
            noded.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(2))
        else:
            noded = QtGui.QTreeWidgetItem(node[0])
            noded.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(3))

        if isinstance(key, int):
            noded.setText(0, str(key))
        else:
            noded.setText(0, key)
      
        noded.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
        #print node[0].text(0),noded.text(0)
        if isinstance(value, dict):
            #print "*** " + noded.text(0) + " has %s child" % len(value)
            self.emit(QtCore.SIGNAL("addLeaves(PyQt_PyObject,PyQt_PyObject)"), [noded], value.items())
        elif isinstance(value, list):
            #print "*** " + noded.text(0) + " has %s child" % len(value)
            self.emit(QtCore.SIGNAL("addLeaves(PyQt_PyObject,PyQt_PyObject)"), [noded], getODict(list2dict(value)).items())
            



    def makeChildrenFromValue(self, varList):
        tabNum = varList[0]
        item = varList[1]
        pathData = varList[2]
        if isinstance(pathData, dict):
            root = QtGui.QTreeWidgetItem(None)
            root.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
            root.setText(0,"JSON")
            root.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.emit(QtCore.SIGNAL("addLeaves(PyQt_PyObject,PyQt_PyObject)"), [root], pathData.items())
        elif isinstance(pathData, list):
            root = QtGui.QTreeWidgetItem(None)
            root.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(2))
            root.setText(0,"JSON")
            root.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.emit(QtCore.SIGNAL("addLeaves(PyQt_PyObject,PyQt_PyObject)"), [root], getODict(list2dict(pathData)).items())
        
        rootClone = root.takeChildren()
        self.emit(QtCore.SIGNAL("process_saveValue(PyQt_PyObject)"), [tabNum, item , rootClone])






class Worker(QtCore.QThread):
    def __init__(self, parent):
        QtCore.QThread.__init__(self, parent)
        self.parent = parent
    
    def run(self):
        self.report = Report()
        
        self.connect(self.parent,QtCore.SIGNAL("handleUrl(PyQt_PyObject,PyQt_PyObject)"),self.report.handleUrl,QtCore.Qt.QueuedConnection)
        self.connect(self.parent,QtCore.SIGNAL("makeChildrenFromValue(PyQt_PyObject)"),self.report.makeChildrenFromValue,QtCore.Qt.QueuedConnection)

        
        
        self.connect(self.report,QtCore.SIGNAL("msg_from_worker(PyQt_PyObject,PyQt_PyObject)"),self.parent.msg_from_worker,QtCore.Qt.QueuedConnection)
        self.connect(self.report,QtCore.SIGNAL("makeTree(PyQt_PyObject)"),self.parent.makeTree,QtCore.Qt.QueuedConnection)
        self.connect(self.report,QtCore.SIGNAL("process_saveValue(PyQt_PyObject)"),self.parent.process_saveValue,QtCore.Qt.QueuedConnection)

        self.exec_()

        



class JsonEditor(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.worker = Worker(self)
        self.worker.start()
        
        
        
        self.searchTabNum = None
        self.wordList = QtCore.QStringList()
        self.completer = None
        

        ######################################################
        self.tabNums = [1]
        self.isTabBusyDict = {"1": False}
        self.undoDict = {"1": []}
        self.redoDict = {"1": []}
        self.undoDataDict = {"1": []}
        self.redoDataDict = {"1": []}
        ######################################################
        
        
        
        ######################################################
        self.data = {}
        self.jsonEncoding = {}
        self.query = {}
        self.findCase = {}
        self.findWhole = {}
        self.it = {}
        self.found = {}
        ######################################################
        
        
        ######################################################
        self.itemClipBoard = {"item": None, "value":None}
        self.tempClipBoard = {"item": None, "value":None}
        ######################################################
        
        
        ################################################################
        self.combo_dict = ordereddict()
        
        self.combo_dict["<type 'dict'>"] = 0
        self.combo_dict["<type '_ordereddict.ordereddict'>"] = 0
        self.combo_dict["<type '_ordereddict.sorteddict'>"] = 0
        
        self.combo_dict["<type 'list'>"] = 1
        #self.combo_dict["<type 'tuple'>"] = 1
        
        self.combo_dict["<type 'str'>"] = 2
        self.combo_dict["<type 'unicode'>"] = 3
        self.combo_dict["<type 'int'>"] = 4
        self.combo_dict["<type 'long'>"] = 5
        self.combo_dict["<type 'bool'>"] = 6
        self.combo_dict["<type 'NoneType'>"] = 7
        
        self.combo_dict["<class 'decimal.Decimal'>"] = 8
        #self.combo_dict["<type 'float'>"] = 8
        ################################################################

        


        
        self.cornerLeft = QtGui.QToolButton(self)
        self.cornerLeft.setCursor(QtCore.Qt.ArrowCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tab_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cornerLeft.setIcon(icon)
        self.cornerLeft.setToolTip('New')
        
        self.cornerRight = QtGui.QToolButton(self)
        self.cornerRight.setCursor(QtCore.Qt.ArrowCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tab_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cornerRight.setIcon(icon)
        self.cornerRight.setToolTip('Close')

        self.connect(self.cornerLeft, QtCore.SIGNAL("clicked()"), self.add_tab)
        self.connect(self.cornerRight, QtCore.SIGNAL("clicked()"), self.remove_tab)
        
        self.tabWidget.setCornerWidget(self.cornerLeft, QtCore.Qt.TopLeftCorner)
        self.tabWidget.setCornerWidget(self.cornerRight, QtCore.Qt.TopRightCorner)
        
        
        
        
        
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.setObjectName("fileToolBar")
        self.addActions(self.fileToolBar, (self.actionOpen,self.actionInput_JSON,None,self.actionSave,self.actionSave_As,self.actionReload))

        
        self.undoAction = self.createAction("Undo", self.undo, "Ctrl+Z", "undo", "Undo")
        self.redoAction = self.createAction("Redo", self.redo, "Ctrl+Y", "redo", "Redo")

        
        self.addChildFirstAction = self.createAction("Add Child First", self.addChild, "Ctrl+Shift+A", "addchild", "Add Child First")
        self.addChildLastAction = self.createAction("Add Child Last", self.addChild, "Shift+A", "addchild", "Add Child Last")
        self.addSiblingBeforeAction = self.createAction("Add Sibling Before", self.addSibling, "Ctrl+Shift+B", "addsibling_before", "Add Sibling Before")
        self.addSiblingAfterAction = self.createAction("Add Sibling After", self.addSibling, "Shift+B", "addsibling_after", "Add Sibling After")
        
        self.delItemAction = self.createAction("Delete Item", self.delItem, "Del", "delete", "Delete Item")
        self.renameItemAction = self.createAction("Rename Item", self.renameItem, "Ctrl+R", "rename", "Rename Item")
        self.cutItemAction = self.createAction("Cut Item", self.cutItem, "Ctrl+X", "cut", "Cut Item")
        self.copyItemAction = self.createAction("Copy Item", self.copyItem, "Ctrl+C", "copy", "Copy Item")
        self.pasteItemAsChildAction = self.createAction("Paste as Child", self.pasteItemAsChild, "Ctrl+Shift+V", "pastechild", "Paste as Child")
        self.pasteItemAsSiblingAction = self.createAction("Paste as Sibling", self.pasteItemAsSibling, "Ctrl+V", "pastesibling", "Paste as Sibling")

        self.moveItemUpAction = self.createAction("Move Item Up", self.moveItemUp, "Ctrl+Up", "1uparrow", "Move Item Up")
        self.moveItemDownAction = self.createAction("Move Item Down", self.moveItemDown, "Ctrl+Down", "1downarrow", "Move Item Down")
        self.moveItemTopAction = self.createAction("Move Item Top", self.moveItemTop, "Ctrl+PgUp", "2uparrow", "Move Item Top")
        self.moveItemBottomAction = self.createAction("Move Item Bottom", self.moveItemBottom, "Ctrl+PgDown", "2downarrow", "Move Item Bottom")
        self.indentItemAction = self.createAction("Indent", self.indentItem, "Ctrl+Shift+Right", "indent", "Indent")
        self.unindentItemAction = self.createAction("Unindent", self.unindentItem, "Ctrl+Shift+Left", "unindent", "Unindent")
        self.sortItemAction = self.createAction("Sort", self.sortChildrenOfItem, "Shift+S", "sort", "Sort")
        
        
        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.setObjectName("editToolBar")
        self.addActions(self.editToolBar, (self.undoAction,self.redoAction,None,self.addChildLastAction,self.addSiblingAfterAction,None,self.delItemAction,self.renameItemAction,self.cutItemAction,self.copyItemAction,self.pasteItemAsChildAction,self.pasteItemAsSiblingAction,None,self.moveItemUpAction,self.moveItemDownAction,self.unindentItemAction,self.indentItemAction,self.sortItemAction))

        self.addActions(self.menuEdit, (self.undoAction,self.redoAction,None,self.addChildFirstAction,self.addChildLastAction,self.addSiblingBeforeAction,self.addSiblingAfterAction,None,self.delItemAction,self.renameItemAction,self.cutItemAction,self.copyItemAction,self.pasteItemAsChildAction,self.pasteItemAsSiblingAction,None,self.moveItemTopAction,self.moveItemUpAction,self.moveItemDownAction,self.moveItemBottomAction,self.unindentItemAction,self.indentItemAction,self.sortItemAction))


        self.remove_tab(0, False)
        
        
    
    
    def undo(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        
        undoDataOp = self.undoDataDict[currentTabNum].pop(0)
        if undoDataOp[0] == "dataAddChildSibling":
            self.dataAddChildSibling(undoDataOp[1], undoDataOp[2], undoDataOp[3], undoDataOp[4], undoDataOp[5], False)
            self.redoDataDict[currentTabNum].insert(0, ("dataDelItem", undoDataOp[1], undoDataOp[2], undoDataOp[3]))
        elif undoDataOp[0] == "dataDelItem":
            key, value = self.dataDelItem(undoDataOp[1], undoDataOp[2], undoDataOp[3], False)
            self.redoDataDict[currentTabNum].insert(0, ("dataAddChildSibling", undoDataOp[1], undoDataOp[2], undoDataOp[3], key, value))
        elif undoDataOp[0] == "dataRenameItem":
            self.dataRenameItem(undoDataOp[1], undoDataOp[2], undoDataOp[3], undoDataOp[4], False)
            self.redoDataDict[currentTabNum].insert(0, ("dataRenameItem", undoDataOp[1], undoDataOp[2], undoDataOp[4], undoDataOp[3]))
        elif undoDataOp[0] == "dataSaveValue":
            if undoDataOp[3] == None:
                key, value = None, self.data[currentTabNum]
            else:
                pathDataParent = self.getPathData(currentTabNum, undoDataOp[2])
                if isinstance(pathDataParent, dict):
                    key, value = pathDataParent.popitem(undoDataOp[3])
                elif isinstance(pathDataParent, list):
                    key, value = undoDataOp[3], pathDataParent.pop(undoDataOp[3])
                
            self.redoDataDict[currentTabNum].insert(0, ("dataSaveValue", currentTabNum, undoDataOp[2], undoDataOp[3], key, value, undoDataOp[6]))
 
            if undoDataOp[2] == None:
                self.data[currentTabNum] = undoDataOp[5]
            else:
                self.dataAddChildSibling(undoDataOp[1], undoDataOp[2], undoDataOp[3], undoDataOp[4], undoDataOp[5], False)
            
            if isinstance(undoDataOp[5], dict):
                undoDataOp[6].setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
            elif isinstance(undoDataOp[5], list):
                undoDataOp[6].setData(0, QtCore.Qt.UserRole, QtCore.QVariant(2))
            else:
                undoDataOp[6].setData(0, QtCore.Qt.UserRole, QtCore.QVariant(3))


        
        
        undoOp = self.undoDict[currentTabNum].pop(0)
        if undoOp[1] == "takeChild":
            thenCurItem = self.itemAbove(undoOp[0].child(undoOp[2]))
            #####
            if undoOp[0].data(0, QtCore.Qt.UserRole).toPyObject() == 2:
                for i in range(undoOp[2] + 1, undoOp[0].childCount()):
                    undoOp[0].child(i).setText(0, str(i-1))
            #####
            taken = undoOp[0].takeChild(undoOp[2])
            self.redoDict[currentTabNum].insert(0, (undoOp[0], "insertChild", undoOp[2], taken))

        
        elif undoOp[1] == "insertChild":
            thenCurItem = undoOp[3]
            #####
            if undoOp[0].data(0, QtCore.Qt.UserRole).toPyObject() == 2:
                newItemText = undoOp[2]
                
                for i in range(undoOp[2], undoOp[0].childCount()):
                    undoOp[0].child(i).setText(0, str(i+1))
                
                undoOp[3].setText(0, str(newItemText))
            else:
                newItemText = self.getNewItemText(undoOp[0], undoOp[3].text(0))
                if newItemText == False:
                    return
                else:
                    newItemText = unicode(newItemText, self.jsonEncoding[currentTabNum])
                undoOp[3].setText(0, newItemText)
            #####
            undoOp[0].insertChild(undoOp[2], undoOp[3])
            self.redoDict[currentTabNum].insert(0, (undoOp[0], "takeChild", undoOp[2]))

        
        elif undoOp[1] == "setText":
            thenCurItem = undoOp[0]
            self.redoDict[currentTabNum].insert(0, (undoOp[0], "setText", undoOp[0].text(0)))
            undoOp[0].setText(0, undoOp[2])

        
        elif undoOp[1] == "insertChildren":
            thenCurItem = undoOp[0]
            taken = undoOp[0].takeChildren()
            undoOp[0].insertChildren(0, undoOp[2])
            self.redoDict[currentTabNum].insert(0, (undoOp[0], "insertChildren", taken))

            
        
        self.__getattribute__("treeWidget_" + currentTabNum).update()
                
        if len(self.undoDataDict[currentTabNum]) > 0:
            self.setTabDirty(currentTabNum, True)
        else:
            self.setTabDirty(currentTabNum, False)
        
        self.__getattribute__("treeWidget_"+ currentTabNum).setCurrentItem(thenCurItem)
        self.printit(thenCurItem)
        if len(self.undoDataDict[currentTabNum]):
            if len(self.undoDataDict[currentTabNum][0]) == 0:
                self.redoDataDict[currentTabNum].insert(0, self.undoDataDict[currentTabNum].pop(0))
                self.redoDict[currentTabNum].insert(0, self.undoDict[currentTabNum].pop(0))
                self.undo()

    
    
    
    def redo(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        
        redoDataOp = self.redoDataDict[currentTabNum].pop(0)
        if redoDataOp[0] == "dataAddChildSibling":
            self.dataAddChildSibling(redoDataOp[1], redoDataOp[2], redoDataOp[3], redoDataOp[4], redoDataOp[5], False)
            self.undoDataDict[currentTabNum].insert(0, ("dataDelItem", redoDataOp[1], redoDataOp[2], redoDataOp[3]))
        elif redoDataOp[0] == "dataDelItem":
            key, value = self.dataDelItem(redoDataOp[1], redoDataOp[2], redoDataOp[3], False)
            self.undoDataDict[currentTabNum].insert(0, ("dataAddChildSibling", redoDataOp[1], redoDataOp[2], redoDataOp[3], key, value))
        elif redoDataOp[0] == "dataRenameItem":
            self.dataRenameItem(redoDataOp[1], redoDataOp[2], redoDataOp[3], redoDataOp[4], False)
            self.undoDataDict[currentTabNum].insert(0, ("dataRenameItem", redoDataOp[1], redoDataOp[2], redoDataOp[4], redoDataOp[3]))
        elif redoDataOp[0] == "dataSaveValue":
            if redoDataOp[3] == None:
                key, value = None, self.data[currentTabNum]
            else:
                pathDataParent = self.getPathData(currentTabNum, redoDataOp[2])
                if isinstance(pathDataParent, dict):
                    key, value = pathDataParent.popitem(redoDataOp[3])
                elif isinstance(pathDataParent, list):
                    key, value = redoDataOp[3], pathDataParent.pop(redoDataOp[3])
                
            self.undoDataDict[currentTabNum].insert(0, ("dataSaveValue", currentTabNum, redoDataOp[2], redoDataOp[3], key, value, redoDataOp[6]))
 
            if redoDataOp[2] == None:
                self.data[currentTabNum] = redoDataOp[5]
            else:
                self.dataAddChildSibling(redoDataOp[1], redoDataOp[2], redoDataOp[3], redoDataOp[4], redoDataOp[5], False)
            
            if isinstance(redoDataOp[5], dict):
                redoDataOp[6].setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
            elif isinstance(redoDataOp[5], list):
                redoDataOp[6].setData(0, QtCore.Qt.UserRole, QtCore.QVariant(2))
            else:
                redoDataOp[6].setData(0, QtCore.Qt.UserRole, QtCore.QVariant(3))


        
        
        redoOp = self.redoDict[currentTabNum].pop(0)
        if redoOp[1] == "takeChild":
            thenCurItem = self.itemAbove(redoOp[0].child(redoOp[2]))
            #####
            if redoOp[0].data(0, QtCore.Qt.UserRole).toPyObject() == 2:
                for i in range(redoOp[2] + 1, redoOp[0].childCount()):
                    redoOp[0].child(i).setText(0, str(i-1))
            #####
            taken = redoOp[0].takeChild(redoOp[2])
            self.undoDict[currentTabNum].insert(0, (redoOp[0], "insertChild", redoOp[2], taken))

        
        elif redoOp[1] == "insertChild":
            thenCurItem = redoOp[3]
            #####
            if redoOp[0].data(0, QtCore.Qt.UserRole).toPyObject() == 2:
                newItemText = redoOp[2]
                
                for i in range(redoOp[2], redoOp[0].childCount()):
                    redoOp[0].child(i).setText(0, str(i+1))
                
                redoOp[3].setText(0, str(newItemText))
            else:
                newItemText = self.getNewItemText(redoOp[0], redoOp[3].text(0))
                if newItemText == False:
                    return
                else:
                    newItemText = unicode(newItemText, self.jsonEncoding[currentTabNum])
                redoOp[3].setText(0, newItemText)
            #####
            redoOp[0].insertChild(redoOp[2], redoOp[3])
            self.undoDict[currentTabNum].insert(0, (redoOp[0], "takeChild", redoOp[2]))

        
        elif redoOp[1] == "setText":
            thenCurItem = redoOp[0]
            self.undoDict[currentTabNum].insert(0, (redoOp[0], "setText", redoOp[0].text(0)))
            redoOp[0].setText(0, redoOp[2])

        
        elif redoOp[1] == "insertChildren":
            thenCurItem = redoOp[0]
            taken = redoOp[0].takeChildren()
            redoOp[0].insertChildren(0, redoOp[2])
            self.undoDict[currentTabNum].insert(0, (redoOp[0], "insertChildren", taken))

            
        
        self.__getattribute__("treeWidget_" + currentTabNum).update()
                
        self.setTabDirty(currentTabNum, True)
        
        self.__getattribute__("treeWidget_"+ currentTabNum).setCurrentItem(thenCurItem)
        self.printit(thenCurItem)
        if len(self.redoDataDict[currentTabNum]):
            if len(self.redoDataDict[currentTabNum][0]) == 0:
                self.undoDataDict[currentTabNum].insert(0, self.redoDataDict[currentTabNum].pop(0))
                self.undoDict[currentTabNum].insert(0, self.redoDict[currentTabNum].pop(0))
                self.redo()

    
    
    def clearRedo(self, currentTabNum):
        self.redoAction.setDisabled(True)
        self.redoDict[currentTabNum] = []
        self.redoDataDict[currentTabNum] = []
    
    
    
    
    def getNewIndexOnOverWrite(self, tabIndex, filename):
        tabToolTipExists = self.tabToolTipExists(tabIndex, filename)
        if tabToolTipExists[0] == True:
            reply = QtGui.QMessageBox.question(self, "Overwrite?", "You have already opened '%s',\n\nDo you want to save it with a different name?\nChoosing 'Discard' will overwrite it." % filename, QtGui.QMessageBox.Save, QtGui.QMessageBox.Discard)
            if reply == QtGui.QMessageBox.Save:
                if not self.saveAs(str(self.tabNums[tabToolTipExists[1]]), twinFileName=filename):
                    self.remove_tab(tabToolTipExists[1], False)
                    if tabToolTipExists[1] < tabIndex:
                        tabIndex = tabIndex - 1
            elif reply == QtGui.QMessageBox.Discard:
                self.remove_tab(tabToolTipExists[1], False)
                if tabToolTipExists[1] < tabIndex:
                    tabIndex = tabIndex - 1
            return tabIndex
        else:
            return tabIndex
    
    
    
    def dontLoseChanges(self, currentTabNum):
        if self.isTabDirty(currentTabNum):
            tabIndex = self.getTabIndex(currentTabNum)
            tabFile = unicode(self.tabWidget.tabToolTip(tabIndex), "utf-8")
            reply = QtGui.QMessageBox.question(self, "Save Changes?", "'%s' has been modified,\n\nDo you want to save changes?" % tabFile, QtGui.QMessageBox.Save, QtGui.QMessageBox.Discard, QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Save:
                if os.path.isfile(unicode(self.tabWidget.tabToolTip(tabIndex),"utf-8")):
                    self.save(currentTabNum)
                else:
                    self.saveAs(currentTabNum)
                return True
            elif reply == QtGui.QMessageBox.Discard:
                return True
            elif reply == QtGui.QMessageBox.Cancel:
                return False
        else:
            return True
    
    
    def reload_tab(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        tabFile = self.tabWidget.tabToolTip(self.getTabIndex(currentTabNum))
        self.lineEdit_0.setText(tabFile)
        self.get_file()
    
    
    def setBranchCollExp(self, collexp=True):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        
        if self.sender() == self.actionExpand_Tree:
            collexp = True
        elif self.sender() == self.actionCollapse_Tree:
            collexp = False
        
        itemBelow = self.itemBelow(curItem)
        it = Iter(curItem)
        
        while it.value():
            try:
                if it.value() == itemBelow:
                    break
                elif it.value().childCount() > 0:
                    it.value().setExpanded(collexp)
                    self.__getattribute__("treeWidget_" + currentTabNum).update()
                it.next()
            except StopIteration:
                break
    
    
    def getTabIndex(self, currentTabNum):
        return self.tabWidget.indexOf(self.__getattribute__("tab_" + currentTabNum))
    
    def isTabHoldsFile(self, currentTabNum):
        return not self.tabWidget.tabWhatsThis(self.getTabIndex(currentTabNum)) == ""
    
    def isTabHoldsInput(self, currentTabNum):
        isTabHoldsFile = self.isTabHoldsFile(currentTabNum)
        tabToolTip = unicode(self.tabWidget.tabToolTip(self.getTabIndex(currentTabNum)),"utf-8")
        tabText = unicode(self.tabWidget.tabText(self.getTabIndex(currentTabNum)),"utf-8")
        if not isTabHoldsFile:
            if tabToolTip == tabText:
                return True
            elif "*" + tabToolTip == tabText:
                return True
        else:
            return False
        
    
    
    
    def closeEvent(self, event):
        tabsModified = self.getModifiedTabs()
        
        if len(tabsModified):
            answer = QtGui.QMessageBox.question(self, "Save Changes?", "%d file(s) have been modified,\n\nDo you want to save changes?" % len(tabsModified), QtGui.QMessageBox.Save, QtGui.QMessageBox.Discard, QtGui.QMessageBox.Cancel)
            if answer == QtGui.QMessageBox.Save:
                for currentTabNum in tabsModified:
                    if self.isTabDirty(currentTabNum):
                        tabIndex = self.getTabIndex(currentTabNum)
                        tabFile = unicode(self.tabWidget.tabToolTip(tabIndex), "utf-8")
                        reply = QtGui.QMessageBox.question(self, "Save Changes?", "'%s' has been modified,\n\nDo you want to save changes?" % tabFile, QtGui.QMessageBox.Save, QtGui.QMessageBox.Discard)
                        if reply == QtGui.QMessageBox.Save:
                            if os.path.isfile(unicode(self.tabWidget.tabToolTip(tabIndex),"utf-8")):
                                self.save(currentTabNum)
                            else:
                                self.saveAs(currentTabNum)
                        elif reply == QtGui.QMessageBox.Discard:
                            pass
            elif answer == QtGui.QMessageBox.Discard:
                pass
            elif answer == QtGui.QMessageBox.Cancel:
                event.ignore()
                return

        event.accept()
        
        
    
    def getModifiedTabs(self):
        tabsModified = [] 
        for i in range(self.tabWidget.count()):
            currentTabNum = str(self.tabNums[i])
            if self.isTabDirty(currentTabNum):
                tabsModified.append(currentTabNum)
        return tabsModified
    
    
    def tabToolTipExists(self, tabIndex, tooltip):
        for i in range(self.tabWidget.count()):
            if i == tabIndex:
                pass
            elif tooltip == unicode(self.tabWidget.tabToolTip(i), "utf-8"):
                return (True, i)
        return (False, None)
    
    
    
    def isFileChangedSince(self, index):
        filename = unicode(self.tabWidget.tabToolTip(index), "utf-8")
        if not os.path.exists(filename):
            return None
        else:
            try:
                return not str(self.tabWidget.tabWhatsThis(index)) == str(os.path.getmtime(filename))
            except OSError:
                return False
                
    
    
    def showTreeContextMenu(self, pos):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        menu = QtGui.QMenu(self)
        menu.addActions(self.menuEdit.actions())
        menu.exec_(self.__getattribute__("treeWidget_"+ currentTabNum).viewport().mapToGlobal(pos))
    
    
    
    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):
        action = QtGui.QAction(text, self)
        if icon is not None:
            action.setIcon(QtGui.QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
        
        
        
        
    
    def isDuplicate(self, item, newItemText):
        for i in range(item.childCount()):
            if item.child(i).text(0) == newItemText:
                return True
        return False
    
    
    def getNewItemText(self, item, q=None, defaultText=""):
        if q == None:
            newItemText, ok = QtGui.QInputDialog.getText(self, "Enter Key", "Enter Key (without path):", QtGui.QLineEdit.Normal, defaultText)
            if newItemText == defaultText and not defaultText == "":
                return False
        else:
            newItemText, ok = q, True
        if ok:
            duplicate = newItemText
            suffix = 2
            while True:
                if self.isDuplicate(item, newItemText):
                    newItemText = duplicate + "_%s" % suffix
                    suffix = suffix + 1
                else:
                    return newItemText
        else:
            return False
        
    
    
    def isUnicodeNeeded(self, key, encoding):
        if isinstance(key, unicode):
            try:
                if len(key) == len(key.encode(encoding)):
                    return key.encode(encoding)
                else:
                    return key
            except UnicodeError:
                return key
        else:
            return key
    
    
    def isKeyUnicode(self, key, encoding):
        try:
            if len(key) == len(key.encode(encoding)):
                return "['%s']" % key.encode(encoding)
            else:
                return '[%r]' % key
        except UnicodeError:
            return '[%r]' % key
        
    
    def getPath(self, currentTabNum, item):
        if item.parent() == None:
            return ""
        key_holder = []
        encoding = self.jsonEncoding[currentTabNum]
        while True:
            if item.parent().data(0, QtCore.Qt.UserRole).toPyObject() == 2:
                key_holder.insert(0, '[%r]' % int(item.text(0)))
            else:
                key_holder.insert(0, self.isKeyUnicode(unicode(item.text(0).toUtf8(), encoding), encoding))
            if item.parent().parent() == None:
                break
            item = item.parent()
        return "".join(key_holder)
    
    
    
    
    def getPathData(self, currentTabNum, path):
        return eval('self.data[currentTabNum]'+ path)
            
    
    
    
    
    def addChild(self, newItem=None, chil_sibAfter=1):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        path = self.getPath(currentTabNum, curItem)
        
        if self.sender() == self.addChildFirstAction:
            chil_sibAfter = 0
        elif self.sender() == self.addChildLastAction:
            chil_sibAfter = 1

        if chil_sibAfter:
            index = curItem.childCount()
        else:
            index = 0

        if newItem == None:
            value = ordereddict()
            newItem = QtGui.QTreeWidgetItem()
            newItem.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
            q = None
        else:
            value = newItem["value"]
            newItem = newItem["item"].clone()
            q = newItem.text(0)
            
        if curItem.data(0, QtCore.Qt.UserRole).toPyObject() == 2:
            newItemText = index
            
            for i in range(index, curItem.childCount()):
                curItem.child(i).setText(0, str(i+1))
            
            newItem.setText(0, str(newItemText))
        else:
            newItemText = self.getNewItemText(curItem, q)
            if newItemText == False:
                return
            else:
                newItemText = unicode(newItemText, self.jsonEncoding[currentTabNum])
            
            newItem.setText(0, newItemText)

        

        newItemText = self.isUnicodeNeeded(newItemText, self.jsonEncoding[currentTabNum])

        self.dataAddChildSibling(currentTabNum, path, index, newItemText, value)

        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        curItem.insertChild(index, newItem)
        self.undoDict[currentTabNum].insert(0, (curItem, "takeChild", index))
        
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(newItem)
        self.__getattribute__("treeWidget_" + currentTabNum).update()
        


                
        
        
    def addSibling(self, newItem=None, chil_sibAfter=1):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        curItemParent = curItem.parent()
        path = self.getPath(currentTabNum, curItemParent)
        
        if self.sender() == self.addSiblingBeforeAction:
            chil_sibAfter = 0
        elif self.sender() == self.addSiblingAfterAction:
            chil_sibAfter = 1
        
        if newItem == None:
            value = ordereddict()
            newItem = QtGui.QTreeWidgetItem()
            newItem.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
            q = None
        else:
            value = newItem["value"]
            newItem = newItem["item"].clone()
            q = newItem.text(0)
            
        if curItemParent.data(0, QtCore.Qt.UserRole).toPyObject() == 2:
            newItemText = int(curItem.text(0)) + chil_sibAfter
            index = newItemText
            
            for i in range(index, curItemParent.childCount()):
                curItemParent.child(i).setText(0, str(i+1))
            
            newItem.setText(0, str(newItemText))
        else:
            newItemText = self.getNewItemText(curItemParent, q)
            if newItemText == False:
                return
            else:
                newItemText = unicode(newItemText, self.jsonEncoding[currentTabNum])
            index = curItemParent.indexOfChild(curItem) + chil_sibAfter
            
            newItem.setText(0, newItemText)
            
        

        newItemText = self.isUnicodeNeeded(newItemText, self.jsonEncoding[currentTabNum])

        self.dataAddChildSibling(currentTabNum, path, index, newItemText, value)

                
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        curItemParent.insertChild(index, newItem)
        self.undoDict[currentTabNum].insert(0, (curItemParent, "takeChild", index))
        
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(newItem)
        self.__getattribute__("treeWidget_" + currentTabNum).update()
        

     


    def avoidExact(self, pathData):
        if isinstance(pathData, list):
            return self.avoidExactInList(pathData[:])
        elif isinstance(pathData, dict):
            return self.avoidExactInDict(pathData.copy())
        else:
            return pathData
    
    
    
    def avoidExactInList(self, value):
        newValue = []
        for i in range(len(value)):
            if isinstance(value[i], dict):
                x = self.avoidExactInDict(value[i].copy())
            elif isinstance(value[i], list):
                x = self.avoidExactInList(value[i][:])
            else:
                x = value[i]
            newValue.append(x)
        return newValue
    
    
    def avoidExactInDict(self, value):
        newValue = ordereddict()
        j = 0
        for i in value.keys():
            if isinstance(value[i], dict):
                x = self.avoidExactInDict(value[i].copy())
            elif isinstance(value[i], list):
                x = self.avoidExactInList(value[i][:])
            else:
                x = value[i]
            newValue.insert(j, i, x)
            j = j + 1
        return newValue
    
    
    
    def dataAddChildSibling(self, currentTabNum, path, index, key, value, addToUndo=True):
        pathData = self.getPathData(currentTabNum, path)
        if isinstance(pathData, list):
            pathData.insert(index, value)
        elif isinstance(pathData, dict):
            pathData.insert(index, key, value)
        
        if addToUndo:
            self.clearRedo(currentTabNum)
            self.undoDataDict[currentTabNum].insert(0, ("dataDelItem", currentTabNum, path, index))
        self.setTabDirty(currentTabNum, True)
                


   
    def delItem(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        curItemParent = curItem.parent()
        path = self.getPath(currentTabNum, curItemParent)
        index = curItemParent.indexOfChild(curItem)
        if curItemParent.data(0, QtCore.Qt.UserRole).toPyObject() == 2:
            for i in range(index + 1, curItemParent.childCount()):
                curItemParent.child(i).setText(0, str(i-1))
        
        self.dataDelItem(currentTabNum, path, index)
        taken = curItemParent.takeChild(index)
        self.undoDict[currentTabNum].insert(0, (curItemParent, "insertChild", index, taken))
        self.__getattribute__("treeWidget_" + currentTabNum).update()
        
        

    
    def dataDelItem(self, currentTabNum, path, index, addToUndo=True):
        pathData = self.getPathData(currentTabNum, path)
        if isinstance(pathData, list):
            key, value = index, pathData.pop(index)
        else:
            key, value = pathData.popitem(index)
        
        if addToUndo:
            self.clearRedo(currentTabNum)
            self.undoDataDict[currentTabNum].insert(0, ("dataAddChildSibling", currentTabNum, path, index, key, value))
        self.setTabDirty(currentTabNum, True)
        return key, value
    
    
    
    
    def renameItem(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        curItemParent = curItem.parent()
        path = self.getPath(currentTabNum, curItemParent)
        
        oldItemText = self.isUnicodeNeeded(unicode(curItem.text(0).toUtf8(), self.jsonEncoding[currentTabNum]), self.jsonEncoding[currentTabNum])
        
        newItemText = self.getNewItemText(curItemParent, None, curItem.text(0))
        if newItemText == False:
            return
        else:
            newItemText = self.isUnicodeNeeded(unicode(newItemText.toUtf8(), self.jsonEncoding[currentTabNum]), self.jsonEncoding[currentTabNum])
        
        
        self.dataRenameItem(currentTabNum, path, oldItemText, newItemText)
        self.undoDict[currentTabNum].insert(0, (curItem, "setText", curItem.text(0)))
        curItem.setText(0, newItemText)

        self.__getattribute__("treeWidget_" + currentTabNum).update()
        
        self.printit(curItem)        
        
    
    
    
    def dataRenameItem(self, currentTabNum, path, oldkey, newkey, addToUndo=True):
        pathData = self.getPathData(currentTabNum, path)
        pathData.rename(oldkey, newkey)
        
        if addToUndo:
            self.clearRedo(currentTabNum)
            self.undoDataDict[currentTabNum].insert(0, ("dataRenameItem", currentTabNum, path, newkey, oldkey))
        self.setTabDirty(currentTabNum, True)
    
    
    def cutItem(self):
        self.copyItem()
        self.delItem()
    
    
    def copyItem(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        path = self.getPath(currentTabNum, curItem)
        pathData = self.getPathData(currentTabNum, path)
        if self.sender() in [self.copyItemAction, self.cutItemAction]:
            self.itemClipBoard["item"] = curItem.clone()
            self.itemClipBoard["value"] = self.avoidExact(pathData)
        else:
            self.tempClipBoard["item"] = curItem.clone()
            self.tempClipBoard["value"] = self.avoidExact(pathData)
        
        self.applyEditRules(currentTabNum, curItem)
            
    
    
    
    def pasteItemAsChild(self, chil_sibAfter=1):
        if self.sender() == self.pasteItemAsChildAction:
            self.addChild(self.itemClipBoard, chil_sibAfter)
        else:
            self.addChild(self.tempClipBoard, chil_sibAfter)
    
    def pasteItemAsSibling(self, chil_sibAfter=1):
        if self.sender() == self.pasteItemAsSiblingAction:
            self.addSibling(self.itemClipBoard, chil_sibAfter)
        else:
            self.addSibling(self.tempClipBoard, chil_sibAfter)

    
    
    def itemBelow(self, item):
        if item.parent():
            index = item.parent().indexOfChild(item)
            if item.parent().child(index + 1):
                return item.parent().child(index + 1)
            else:
                try:
                    index = item.parent().parent().indexOfChild(item.parent())
                except:
                    return None
                return item.parent().parent().child(index + 1)
        else:
            return None
            
            

    def itemAbove(self, item):
        if item.parent():
            index = item.parent().indexOfChild(item)
            if item.parent().child(index - 1):
                return item.parent().child(index - 1)
            else:
                return item.parent()
        else:
            return None
        
        

    def prevSibling(self, item):
        if item.parent():
            index = item.parent().indexOfChild(item)
            return item.parent().child(index - 1)
        else:
            return None
        
    

    def nextSibling(self, item):
        if item.parent():
            index = item.parent().indexOfChild(item)
            return item.parent().child(index + 1)
        else:
            return None


    
    def moveItemUp(self):
        ##### if topLevelItem(0) disable
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        itemAbove = self.itemAbove(curItem)
        chil_sibAfter = 0
        self.cutItem()
        self.undoDict[currentTabNum].insert(0, ())
        self.undoDataDict[currentTabNum].insert(0, ())
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(itemAbove)
        self.pasteItemAsSibling(chil_sibAfter)
        
    
    def moveItemTop(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        itemAbove = curItem.parent().child(0)
        chil_sibAfter = 0
        self.cutItem()
        self.undoDict[currentTabNum].insert(0, ())
        self.undoDataDict[currentTabNum].insert(0, ())
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(itemAbove)
        self.pasteItemAsSibling(chil_sibAfter)
    
    
    def moveItemDown(self):
        ##### if itemBelow None disable
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        itemBelow = self.itemBelow(curItem)
        chil_sibAfter = 1
        self.cutItem()
        self.undoDict[currentTabNum].insert(0, ())
        self.undoDataDict[currentTabNum].insert(0, ())
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(itemBelow)    
        self.pasteItemAsSibling(chil_sibAfter)
        
        
    def moveItemBottom(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        itemBelow = curItem.parent().child(curItem.parent().childCount() - 1)
        chil_sibAfter = 1
        self.cutItem()
        self.undoDict[currentTabNum].insert(0, ())
        self.undoDataDict[currentTabNum].insert(0, ())
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(itemBelow)    
        self.pasteItemAsSibling(chil_sibAfter)
        
        
    def indentItem(self):
        #ustundeki elemanin childi yap
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        chil_sibAfter = 1
        self.cutItem()
        self.undoDict[currentTabNum].insert(0, ())
        self.undoDataDict[currentTabNum].insert(0, ())
        self.pasteItemAsChild(chil_sibAfter)
    
    def unindentItem(self):
        #ebeveyninin siblingi yap
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        curItemParent = curItem.parent()
        chil_sibAfter = 1
        self.cutItem()
        self.undoDict[currentTabNum].insert(0, ())
        self.undoDataDict[currentTabNum].insert(0, ())
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(curItemParent)
        self.pasteItemAsSibling(chil_sibAfter)
        
        
    def sortChildrenOfItem(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        curItemParent = curItem.parent()
        
        if curItemParent == None:
            pathParent = None
            index = None
        else:
            pathParent = self.getPath(currentTabNum, curItemParent)
            index = curItemParent.indexOfChild(curItem)
        
        
        sortOrder, ok = QtGui.QInputDialog.getItem(self, "Choose Sort Order", "Sort Order:", ["Ascending", "Descending"], 0, False)
        if not ok:
            return
        
        if sortOrder == "Ascending":
            sortOrder = QtCore.Qt.AscendingOrder
            reversed = False
        elif sortOrder == "Descending":
            sortOrder = QtCore.Qt.DescendingOrder
            reversed = True
        
        self.sortDataOfItem(currentTabNum, curItem, pathParent, index, reversed)
        
        curItemClone = curItem.clone()
        taken = curItemClone.takeChildren()
        self.undoDict[currentTabNum].insert(0, (curItem, "insertChildren", taken))
        
        itemBelow = self.itemBelow(curItem)
        it = Iter(curItem)
        
        while it.value():
            try:
                if it.value() == itemBelow:
                    break
                elif it.value().childCount() > 0 and not it.value().data(0, QtCore.Qt.UserRole).toPyObject() == 2:
                    it.value().sortChildren(0, sortOrder)
                    self.__getattribute__("treeWidget_" + currentTabNum).update()
                it.next()
            except StopIteration:
                break
        
        curItem.setExpanded(False)
        curItem.setExpanded(True)
        
        self.printit(curItem)
            
            
    
    
    def sortDataOfItem(self, currentTabNum, curItem, pathParent, index, reversed):
        if index == None:
            key, value = None, self.data[currentTabNum]
            if isinstance(self.data[currentTabNum], dict):
                v = sorteddict(self.data[currentTabNum], getFirstOrdinalOf)
                if reversed:
                    v.reverse()
                newValue = self.sortDictData(ordereddict(v,relax=True), reversed)
                self.data[currentTabNum] = newValue
            elif isinstance(self.data[currentTabNum], list):
                newValue = self.sortListData(self.data[currentTabNum], reversed)
                self.data[currentTabNum] = newValue
                
        else:
            pathDataParent = self.getPathData(currentTabNum, pathParent)    
            if isinstance(pathDataParent, dict):
                key, value = pathDataParent.popitem(index)
                if isinstance(value, dict):
                    v = sorteddict(value, getFirstOrdinalOf)
                    if reversed:
                        v.reverse()
                    pathDataParent.insert(index, key, self.sortDictData(ordereddict(v,relax=True), reversed))
                elif isinstance(value, list):
                    pathDataParent.insert(index, key, self.sortListData(value, reversed))
                                    
            elif isinstance(pathDataParent, list):
                key, value = index, pathDataParent.pop(index)
                if isinstance(value, dict):
                    v = sorteddict(value, getFirstOrdinalOf)
                    if reversed:
                        v.reverse()
                    pathDataParent.insert(index, self.sortDictData(ordereddict(v,relax=True), reversed))
                elif isinstance(value, list):
                    pathDataParent.insert(index, self.sortListData(value, reversed))
        
        self.clearRedo(currentTabNum)
        self.undoDataDict[currentTabNum].insert(0, ("dataSaveValue", currentTabNum, pathParent, index, key, value, curItem))
        self.setTabDirty(currentTabNum, True)
                
                
    
    
    def sortDictData(self, pathData, reversed):
        newValue = ordereddict()
        j = 0
        for i in pathData.keys():
            if isinstance(pathData[i], dict):
                v = sorteddict(pathData[i], getFirstOrdinalOf)
                if reversed:
                    v.reverse()
                x = self.sortDictData(ordereddict(v,relax=True), reversed)
            elif isinstance(pathData[i], list):
                x = self.sortListData(pathData[i], reversed)
            else:
                x = pathData[i]
            newValue.insert(j, i, x)
            j = j + 1
        return newValue
    
    
    
    def sortListData(self, pathData, reversed):
        newValue = []
        for i in range(len(pathData)):
            if isinstance(pathData[i], dict):
                v = sorteddict(pathData[i], getFirstOrdinalOf)
                if reversed:
                    v.reverse()
                x = self.sortDictData(ordereddict(v,relax=True), reversed)
            elif isinstance(pathData[i], list):
                x = self.sortListData(pathData[i], reversed)
            else:
                x = pathData[i]
            newValue.append(x)
        return newValue
    
    
    
    
    
    def onTabChanged(self, newIndex):
        if newIndex == -1:
            self.add_tab()
            return
        
        currentTabNum = str(self.tabNums[newIndex])
        self.setWindowTitle("pyJsonEditor - " + self.tabWidget.tabToolTip(newIndex))
        
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        if not curItem == None:
            self.applyEditRules(currentTabNum, curItem)
        
        self.applyTabBusyRules(newIndex, self.isTabBusyDict[currentTabNum])



    def applyTabBusyRules(self, index, b):
        self.menuFile.setDisabled(b)
        self.menuEdit.setDisabled(b)
        self.fileToolBar.setDisabled(b)
        self.editToolBar.setDisabled(b)
        
        self.actionExpand_Tree.setDisabled(b)
        self.actionCollapse_Tree.setDisabled(b)
        self.actionFind.setDisabled(b)

        if b:
            self.actionFind_Next.setDisabled(b)
            self.actionFind_Previous.setDisabled(b)
        else:
            if index == self.tabWidget.currentIndex():
                currentTabNum = str(self.tabNums[index])
                try:
                    if self.found[currentTabNum]:
                        self.actionFind_Next.setDisabled(b)
                        self.actionFind_Previous.setDisabled(b)
                        self.searchTabNum = currentTabNum
                    else:
                        self.actionFind_Next.setDisabled(not b)
                        self.actionFind_Previous.setDisabled(not b)
                except KeyError:
                    self.actionFind_Next.setDisabled(not b)
                    self.actionFind_Previous.setDisabled(not b)
            
                self.applyFileChangedRules(index)
            
        
        
    
    def applyFileChangedRules(self, index):
        if not self.tabWidget.tabWhatsThis(index) == "":
            currentTabNum = str(self.tabNums[index])
            filename = unicode(self.tabWidget.tabToolTip(index),"utf-8")
            isFileChangedSince = self.isFileChangedSince(index)
            if isFileChangedSince == True:
                msgBox = QtGui.QMessageBox()
                msgBox.setWindowTitle("File changed on disk")
                msgBox.setText("File '%s' changed since you have opened it,\nDo you want to reload file?" % filename)
                reloadFile = msgBox.addButton("Reload File", msgBox.AcceptRole)
                overWriteFile = msgBox.addButton("Overwrite File", msgBox.DestructiveRole)
                msgBox.exec_()
                if msgBox.clickedButton() == reloadFile:
                    self.lineEdit_0.setText(self.tabWidget.tabToolTip(index))
                    self.get_file()
                elif msgBox.clickedButton() == overWriteFile:
                    if self.saveToFile(currentTabNum, filename):
                        pass
                    else:
                        QtGui.QMessageBox.information(self, "Overwrite Failed", "Couldn't overwrite '%s', will now reload it." % filename)
                        self.lineEdit_0.setText(self.tabWidget.tabToolTip(index))
                        self.get_file()
            elif isFileChangedSince == None:
                reply = QtGui.QMessageBox.question(self, "File deleted on disk", "File '%s' has been deleted,\nDo you want to save changes?" % filename, QtGui.QMessageBox.Save, QtGui.QMessageBox.Discard)
                if reply == QtGui.QMessageBox.Save:
                    if self.saveToFile(currentTabNum, filename):
                        pass
                    else:
                        QtGui.QMessageBox.information(self, "Save Failed", "Couldn't save '%s', will now remove tab holding it." % filename)
                        self.remove_tab(index, False)
                elif reply == QtGui.QMessageBox.Discard:
                    self.remove_tab(index, False)            
    
    
    
    
    def add_tab(self):
        self.cornerRight.setDisabled(True)
        num = self.tabWidget.count() + 1
        
        if num == 1:
            pass
        else:
            while True:
                if not num in self.tabNums:
                    break
                num = num + 1
        ########################################
        self.tabNums.append(num)
        num = str(num)
        self.isTabBusyDict[num] = False
        self.undoDict[num] = []
        self.redoDict[num] = []
        self.undoDataDict[num] = []
        self.redoDataDict[num] = []
        ########################################
            
        self.__setattr__("tab_" + num, QtGui.QWidget())
        self.__getattribute__("tab_" + num).setObjectName("tab_" + num)
        self.__setattr__("gridLayout_" + num, QtGui.QGridLayout(self.__getattribute__("tab_" + num)))
        self.__getattribute__("gridLayout_" + num).setObjectName("gridLayout_" + num)
        self.__setattr__("splitter_" + num, QtGui.QSplitter(self.__getattribute__("tab_" + num)))
        self.__getattribute__("splitter_" + num).setOrientation(QtCore.Qt.Vertical)
        self.__getattribute__("splitter_" + num).setObjectName("splitter_" + num)
        self.__setattr__("treeWidget_"+ num, QtGui.QTreeWidget(self.__getattribute__("splitter_" + num)))
        self.__getattribute__("treeWidget_"+ num).setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.__getattribute__("treeWidget_"+ num).setObjectName("treeWidget_" + num)
        self.__getattribute__("treeWidget_"+ num).setHeaderHidden(True)
        self.__getattribute__("treeWidget_"+ num).headerItem().setText(0,"Working...")
        self.__setattr__("textBrowser_" + num, QtGui.QTextBrowser(self.__getattribute__("splitter_" + num)))
        self.__getattribute__("textBrowser_" + num).setUndoRedoEnabled(True)
        self.__getattribute__("textBrowser_" + num).setReadOnly(False)
        self.__getattribute__("textBrowser_" + num).setAcceptRichText(False)
        self.__getattribute__("textBrowser_" + num).setObjectName("textBrowser_" + num)
        self.__getattribute__("gridLayout_" + num).addWidget(self.__getattribute__("splitter_" + num), 0, 0, 1, 1)
        
        
        
        self.__setattr__("horizontalLayout_" + num, QtGui.QHBoxLayout())
        self.__getattribute__("horizontalLayout_" + num).setObjectName("horizontalLayout_" + num)
        self.__setattr__("label_" + num + "_1", QtGui.QLabel("PATH:", self.__getattribute__("tab_" + num)))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__getattribute__("label_" + num + "_1").sizePolicy().hasHeightForWidth())
        self.__getattribute__("label_" + num + "_1").setSizePolicy(sizePolicy)
        self.__getattribute__("label_" + num + "_1").setFrameShape(QtGui.QFrame.Box)
        self.__getattribute__("label_" + num + "_1").setFrameShadow(QtGui.QFrame.Sunken)
        self.__getattribute__("label_" + num + "_1").setObjectName("label_" + num + "_1")
        self.__getattribute__("horizontalLayout_" + num).addWidget(self.__getattribute__("label_" + num + "_1"))
        self.__setattr__("lineEdit_" + num, QtGui.QLineEdit(self.__getattribute__("tab_" + num)))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__getattribute__("lineEdit_" + num).sizePolicy().hasHeightForWidth())
        self.__getattribute__("lineEdit_" + num).setSizePolicy(sizePolicy)
        self.__getattribute__("lineEdit_" + num).setReadOnly(True)
        self.__getattribute__("lineEdit_" + num).setObjectName("lineEdit_" + num)
        self.__getattribute__("horizontalLayout_" + num).addWidget(self.__getattribute__("lineEdit_" + num))
        
        
        self.__setattr__("label_" + num + "_2", QtGui.QLabel("Type:", self.__getattribute__("tab_" + num)))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__getattribute__("label_" + num + "_2").sizePolicy().hasHeightForWidth())
        self.__getattribute__("label_" + num + "_2").setSizePolicy(sizePolicy)
        self.__getattribute__("label_" + num + "_2").setFrameShape(QtGui.QFrame.Box)
        self.__getattribute__("label_" + num + "_2").setFrameShadow(QtGui.QFrame.Sunken)
        self.__getattribute__("label_" + num + "_2").setObjectName("label_" + num + "_2")
        self.__getattribute__("horizontalLayout_" + num).addWidget(self.__getattribute__("label_" + num + "_2"))
        
        
        self.__setattr__("comboBox_" + num, QtGui.QComboBox(self.__getattribute__("tab_" + num)))
        self.__getattribute__("comboBox_" + num).setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__getattribute__("comboBox_" + num).sizePolicy().hasHeightForWidth())
        self.__getattribute__("comboBox_" + num).setSizePolicy(sizePolicy)
        self.__getattribute__("comboBox_" + num).setFrame(True)
        self.__getattribute__("comboBox_" + num).setObjectName("comboBox_" + num)
        self.__getattribute__("comboBox_" + num).addItem("ordereddict")
        self.__getattribute__("comboBox_" + num).addItem("list")
        self.__getattribute__("comboBox_" + num).addItem("str")
        self.__getattribute__("comboBox_" + num).addItem("unicode")
        self.__getattribute__("comboBox_" + num).addItem("int")
        self.__getattribute__("comboBox_" + num).addItem("long")
        self.__getattribute__("comboBox_" + num).addItem("bool")
        self.__getattribute__("comboBox_" + num).addItem("NoneType")
        self.__getattribute__("comboBox_" + num).addItem("Decimal")
        self.__getattribute__("comboBox_" + num).addItem("undefined")
        self.__getattribute__("horizontalLayout_" + num).addWidget(self.__getattribute__("comboBox_" + num))
        
        
        self.__setattr__("label_" + num + "_3", QtGui.QLabel("Length:", self.__getattribute__("tab_" + num)))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__getattribute__("label_" + num + "_3").sizePolicy().hasHeightForWidth())
        self.__getattribute__("label_" + num + "_3").setSizePolicy(sizePolicy)
        self.__getattribute__("label_" + num + "_3").setFrameShape(QtGui.QFrame.Box)
        self.__getattribute__("label_" + num + "_3").setFrameShadow(QtGui.QFrame.Sunken)
        self.__getattribute__("label_" + num + "_3").setObjectName("label_" + num + "_3")
        self.__getattribute__("horizontalLayout_" + num).addWidget(self.__getattribute__("label_" + num + "_3"))
        
        
        
        self.__setattr__("label_" + num + "_4", QtGui.QLabel("Encoding:", self.__getattribute__("tab_" + num)))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__getattribute__("label_" + num + "_4").sizePolicy().hasHeightForWidth())
        self.__getattribute__("label_" + num + "_4").setSizePolicy(sizePolicy)
        self.__getattribute__("label_" + num + "_4").setFrameShape(QtGui.QFrame.Box)
        self.__getattribute__("label_" + num + "_4").setFrameShadow(QtGui.QFrame.Sunken)
        self.__getattribute__("label_" + num + "_4").setObjectName("label_" + num + "_4")
        self.__getattribute__("horizontalLayout_" + num).addWidget(self.__getattribute__("label_" + num + "_4"))
        
        
        self.__setattr__("pushButton_" + num + "_1", QtGui.QPushButton(self.__getattribute__("tab_" + num)))
        self.__getattribute__("pushButton_" + num + "_1").setText("Save Value")
        self.__getattribute__("pushButton_" + num + "_1").setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.__getattribute__("pushButton_" + num + "_1").sizePolicy().hasHeightForWidth())
        self.__getattribute__("pushButton_" + num + "_1").setSizePolicy(sizePolicy)
        self.__getattribute__("pushButton_" + num + "_1").setAutoDefault(False)
        self.__getattribute__("pushButton_" + num + "_1").setDefault(False)
        self.__getattribute__("pushButton_" + num + "_1").setFlat(False)
        self.__getattribute__("pushButton_" + num + "_1").setObjectName("pushButton_" + num + "_1")
        self.__getattribute__("horizontalLayout_" + num).addWidget(self.__getattribute__("pushButton_" + num + "_1"))
        self.connect(self.__getattribute__("pushButton_" + num + "_1"), QtCore.SIGNAL("clicked()"), self.saveValue)
        self.connect(self.__getattribute__("textBrowser_" + num), QtCore.SIGNAL("undoAvailable(bool)"), self.__getattribute__("pushButton_" + num + "_1").setEnabled)
        
        self.__getattribute__("gridLayout_" + num).addLayout(self.__getattribute__("horizontalLayout_" + num), 1, 0, 1, 1)

        
        tab_index = self.tabWidget.addTab(self.__getattribute__("tab_" + num), "")
        self.tabWidget.setTabText(tab_index, "Tab " + num)
        self.tabWidget.setTabToolTip(tab_index, "Tab " + num)
        self.tabWidget.setTabWhatsThis(tab_index, "")
        if tab_index == self.tabWidget.currentIndex():
            self.setWindowTitle("pyJsonEditor - " + "Tab " + num)
        self.tabWidget.setCurrentIndex(tab_index)
        
        
        
        self.connect(self.__getattribute__("treeWidget_"+ num), QtCore.SIGNAL("currentItemChanged(QTreeWidgetItem *,QTreeWidgetItem *)"), self.printit)
        self.connect(self.__getattribute__("treeWidget_"+ num), QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.showTreeContextMenu)     
        ############################################
        self.data[num] = ordereddict()
        self.jsonEncoding[num] = "utf-8"
        self.query[num] = None
        self.findCase[num] = None
        self.findWhole[num] = None
        self.it[num] = None
        self.found[num] = False
        ############################################
        
        root = QtGui.QTreeWidgetItem(None)
        root.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
        root.setText(0,"JSON")
        root.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.__getattribute__("treeWidget_" + num).addTopLevelItem(root)
        self.__getattribute__("treeWidget_" + num).setCurrentItem(root)
        self.__getattribute__("label_" + num + "_4").setText("Encoding: " + self.jsonEncoding[num])


        self.cornerRight.setDisabled(False)
    
    
    def remove_tab(self, index=None, checkForDirty=True):
        if index == None:
            index = self.tabWidget.currentIndex()
        currentTabNum = str(self.tabNums[index])
        
        if checkForDirty:
            if not self.dontLoseChanges(currentTabNum):
                return
        
        self.cornerLeft.setDisabled(True)
        
        try:
            del self.data[currentTabNum], self.jsonEncoding[currentTabNum], self.query[currentTabNum], self.findCase[currentTabNum], self.findWhole[currentTabNum], self.it[currentTabNum], self.found[currentTabNum]
        except:
            pass
        
        ########################################
        self.tabNums.pop(index)
        self.isTabBusyDict.pop(currentTabNum)
        self.undoDict.pop(currentTabNum)
        self.redoDict.pop(currentTabNum)
        self.undoDataDict.pop(currentTabNum)
        self.redoDataDict.pop(currentTabNum)
        ########################################
        
        self.tabWidget.removeTab(index)

        self.cornerLeft.setDisabled(False)
        
        
    
    def setCurStatus(self, currentTabNum, b):
        self.isTabBusyDict[currentTabNum] = b
        self.__getattribute__("treeWidget_" + currentTabNum).setHeaderHidden(not b)
        self.__getattribute__("treeWidget_" + currentTabNum).setDisabled(b)
        self.__getattribute__("textBrowser_" + currentTabNum).setDisabled(b)
        
        self.applyTabBusyRules(self.getTabIndex(currentTabNum), b)
    
    
    
    
    def fill_lineedit_completer(self, word):
        if not self.wordList.contains(word, QtCore.Qt.CaseSensitive):
            self.wordList.prepend(word)
            self.completer = QtGui.QCompleter(self.wordList, self)
            self.connect(self.completer, QtCore.SIGNAL("activated(const QString&)"), self.get_file)
            self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.lineEdit_0.setCompleter(self.completer)
            self.recentFiles()
        
    def recentFiles(self):
        self.menuOpen_Recent.clear()
        for i in self.wordList[:10]:
            i = unicode(i, "utf-8")
            action = QtGui.QAction("%s [%s]" % (os.path.basename(i), i), self)
            action.setProperty("dest", QtCore.QVariant(i))
            self.connect(action, QtCore.SIGNAL("triggered()"), self.openRecent)
            self.menuOpen_Recent.addAction(action)
            
            
    def openRecent(self):
        self.lineEdit_0.setText(self.sender().property("dest").toPyObject())
        QtCore.QTimer.singleShot(250, self.get_file)
        
    
    
    def setTabDirty(self, currentTabNum, dirty):
        tabIndex = self.getTabIndex(currentTabNum)
        if dirty:
            self.tabWidget.setTabText(tabIndex, "*" + os.path.basename(unicode(self.tabWidget.tabToolTip(tabIndex), "utf-8")))
        else:
            self.tabWidget.setTabText(tabIndex, os.path.basename(unicode(self.tabWidget.tabToolTip(tabIndex), "utf-8")))
            
        
    
    def isTabDirty(self, currentTabNum):
        tabIndex = self.getTabIndex(currentTabNum)
        return not os.path.basename(unicode(self.tabWidget.tabToolTip(tabIndex), "utf-8")) == unicode(self.tabWidget.tabText(tabIndex), "utf-8")

    
    
    
    def avoidBidInDict(self, value):
        newValue = ordereddict()
        j = 0
        for i in value.keys():
            if str(type(value[i])) == "<type '_ordereddict.ordereddict'>":
                x = self.avoidBidInDict(value[i])
            elif isinstance(value[i], dict):
                x = self.avoidBidInDict(ordereddict(value[i], relax=True))
            elif isinstance(value[i], (list, tuple)):
                x = self.avoidBidInList(value[i])
            elif isinstance(value[i], float):
                x = Decimal(str(value[i]))
            else:
                x = value[i]
            newValue.insert(j, i, x)
            j = j + 1
        return newValue
    
    def avoidBidInList(self, value):
        newValue = []
        for i in range(len(value)):
            if str(type(value[i])) == "<type '_ordereddict.ordereddict'>":
                x = self.avoidBidInDict(value[i])
            elif isinstance(value[i], dict):
                x = self.avoidBidInDict(ordereddict(value[i], relax=True))
            elif isinstance(value[i], (list, tuple)):
                x = self.avoidBidInList(value[i])
            elif isinstance(value[i], float):
                x = Decimal(str(value[i]))
            else:
                x = value[i]
            newValue.append(x)
        return newValue
    
    
    
    def saveValue(self):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        self.__getattribute__("pushButton_" + currentTabNum + "_1").setDisabled(True)
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        curItemParent = curItem.parent()
        
        ### TODO ###
        valueString = str(self.__getattribute__("textBrowser_" + currentTabNum).toPlainText())
        
        try:
            pathData = eval(valueString, {"__builtins__" : None}, {"ordereddict" : ordereddict, "sorteddict" : sorteddict, "Decimal" : Decimal, "True" : True, "False" : False, "nan" : __nan__, "inf" : __inf__})
        except Exception, e:
            QtGui.QMessageBox.critical(self, "Error", "Couldn't eval value.\n\nReason: %s" % e.__str__())
            self.printit(curItem)
            return
        
#        if isinstance(pathData, dict):
#            if str(type(pathData)) == "<type '_ordereddict.ordereddict'>":
#                pathData = self.avoidBidInDict(pathData)
#            else:
#                pathData = self.avoidBidInDict(ordereddict(pathData, relax=True))
#        elif isinstance(pathData, (list, tuple)):
#            pathData = self.avoidBidInList(pathData)
#        elif isinstance(pathData, float):
#            pathData = Decimal(str(pathData))
#        else:
#            try:
#                self.combo_dict[str(type(pathData))]
#            except:
#                QtGui.QMessageBox.critical(self, "Wrong type", "Value type: %s,\n\nValue type should be one of the types:\n\n%r" % (str(type(pathData)), self.combo_dict.keys()))
#                self.printit(curItem)
#                return
            
        try:
            dumps = simplejson.dumps(pathData, encoding=self.jsonEncoding[currentTabNum], use_decimal=True)
        except Exception, f:
            QtGui.QMessageBox.critical(self, "Error", "<b>%s</b><br><br><u>Details:</u> <i>%s</i>" % (f.__class__.__name__, f.__str__()))
            self.printit(curItem)
            return
        
        try:
            pathData = simplejson.loads(dumps, encoding=self.jsonEncoding[currentTabNum], parse_constant=Decimal, object_pairs_hook=getODict, use_decimal=True)
        except Exception, g:
            QtGui.QMessageBox.critical(self, "Error", "<b>%s</b><br><br><u>Details:</u> <i>%s</i>" % (g.__class__.__name__, g.__str__()))
            self.printit(curItem)
            return
        ### TODO ###
        
        
        
        if curItemParent == None:
            if not isinstance(pathData, (dict, list)):
                QtGui.QMessageBox.critical(self, "Error", "A JSON payload should be a dict or list")
                self.printit(curItem)
                return
            pathParent, index, key, value = None, None, None, self.data[currentTabNum]
            self.data[currentTabNum] = pathData
        else:
            pathParent = self.getPath(currentTabNum, curItemParent)
            pathDataParent = self.getPathData(currentTabNum, pathParent)
            index = curItemParent.indexOfChild(curItem)
                
            if isinstance(pathDataParent, dict):
                key, value = pathDataParent.popitem(index)
                pathDataParent.insert(index, key, pathData)
    
            elif isinstance(pathDataParent, list):
                key, value = index, pathDataParent.pop(index)
                pathDataParent.insert(index, pathData)
            

        self.clearRedo(currentTabNum)
        self.undoDataDict[currentTabNum].insert(0, ("dataSaveValue", currentTabNum, pathParent, index, key, value, curItem))
    
        self.setTabDirty(currentTabNum, True)
        
        taken = curItem.takeChildren()
        self.undoDict[currentTabNum].insert(0, (curItem, "insertChildren", taken))
        
        if isinstance(pathData, dict):
            curItem.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(1))
            self.setCurStatus(currentTabNum, True)
            self.emit(QtCore.SIGNAL("makeChildrenFromValue(PyQt_PyObject)"), [currentTabNum, curItem, pathData])
        elif isinstance(pathData, list):
            curItem.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(2))
            self.setCurStatus(currentTabNum, True)
            self.emit(QtCore.SIGNAL("makeChildrenFromValue(PyQt_PyObject)"), [currentTabNum, curItem, pathData])
        else:
            curItem.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(3))
            self.__getattribute__("treeWidget_" + currentTabNum).update()
            self.printit(curItem)
            
        
        
    
    
    def process_saveValue(self, varList):
        tabNum = varList[0]
        
        try:
            self.tabNums.index(int(tabNum))
        except ValueError:
            return
        
        item = varList[1]
        children = varList[2]
        item.addChildren(children)
        self.setCurStatus(tabNum, False)
        self.__getattribute__("treeWidget_" + tabNum).update()
        self.printit(item)
    



    
    def save(self, currentTabNum=None):
        if currentTabNum == None:
            currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        filename = self.tabWidget.tabToolTip(self.getTabIndex(currentTabNum))
        filename = unicode(filename.toUtf8(), "utf-8")
        self.setCurStatus(currentTabNum, True)
        return self.saveToFile(currentTabNum, filename)
    
    
    
    def saveAs(self, currentTabNum=None, twinFileName=None):
        if currentTabNum == None:
            currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        curFile = unicode(self.tabWidget.tabToolTip(self.getTabIndex(currentTabNum)), "utf-8")
        if os.path.isfile(curFile):
            filename = QtGui.QFileDialog.getSaveFileName(self, "Save As", curFile)
        else:
            filename = QtGui.QFileDialog.getSaveFileName(self, "Save As", "")
            
        if filename:
            filename = unicode(filename.toUtf8(), "utf-8")
            if not filename == twinFileName:
                self.setCurStatus(currentTabNum, True)
                return self.saveToFile(currentTabNum, filename)
            else:
                return False
        else:
            return False
            
    
    
    def saveToFile(self, currentTabNum, filename):
        curItem = self.__getattribute__("treeWidget_" + currentTabNum).currentItem()
        
        tabIndex = self.getNewIndexOnOverWrite(self.getTabIndex(currentTabNum), filename)
                    
        try:
            f = codecs.open(filename, "w", self.jsonEncoding[currentTabNum])
            f.write(simplejson.dumps(self.data[currentTabNum], ensure_ascii=False, indent="  ", encoding=self.jsonEncoding[currentTabNum], use_decimal=True))
        except Exception, e:
            self.msg_from_worker(currentTabNum, u"<b>%s</b><br><br><u>Details:</u> <i>%s</i>" % (e.__class__.__name__, e.__str__()))
            return False
        finally:
            try:
                f.close()
            except:
                pass
            
        lastModified = str(os.path.getmtime(filename))
                
        self.tabWidget.setTabText(tabIndex, os.path.basename(filename))
        self.tabWidget.setTabToolTip(tabIndex, filename)
        self.tabWidget.setTabWhatsThis(tabIndex, lastModified)
        if unicode(self.tabWidget.tabToolTip(self.tabWidget.currentIndex()), "utf-8") == filename:
            self.setWindowTitle("pyJsonEditor - " + filename)
        self.fill_lineedit_completer(filename)
        
        self.statusbar.showMessage("Saved to: " + filename, 3000)

        self.setCurStatus(currentTabNum, False)
        self.applyEditRules(currentTabNum, curItem)
        return True

        

        
    
    
    
    def msg_from_worker(self, currentTabNum, msg):
        try:
            tabIndex = self.tabNums.index(int(currentTabNum))
        except ValueError:
            return
        
        self.tabWidget.setCurrentIndex(tabIndex)
        self.setCurStatus(currentTabNum, False)
        
        if isinstance(msg, list):
            reply = QtGui.QMessageBox.question(self, "Inspect Error?", msg[2], QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                dialog = Input_Dialog(self)
                dialog.editor.set_text(msg[0])
                dialog.editor.highlightLine(msg[1].lineno, msg[1].endlineno, msg[1].colno, msg[1].endcolno)
                if dialog.exec_():
                    self.process_input_json(unicode(dialog.editor.text().toUtf8(), "utf-8"))  
        else:
            QtGui.QMessageBox.critical(self, "Error", msg)


    
    def choosefile(self):
        f = QtGui.QFileDialog.getOpenFileName(self)
        if f:
            self.lineEdit_0.setText(f)
            QtCore.QTimer.singleShot(250, self.get_file)
    
 
    
    def get_file(self):
        if self.lineEdit_0.text() == "":
            return
        
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
                
        request = unicode(self.lineEdit_0.text().toUtf8(),"utf-8")
        
        if not self.dontLoseChanges(currentTabNum):
            return
        
        self.setCurStatus(currentTabNum, True)
        self.emit(QtCore.SIGNAL("handleUrl(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, request)
    
    
    def makeTree(self,vars):
        currentTabNum = vars[0]
        self.undoDict[currentTabNum] = []
        self.redoDict[currentTabNum] = []
        self.undoDataDict[currentTabNum] = []
        self.redoDataDict[currentTabNum] = []
        
        try:
            self.tabNums.index(int(currentTabNum))
        except ValueError:
            return
        
        curFile = vars[4]
        
        tabIndex = self.getNewIndexOnOverWrite(self.tabNums.index(int(currentTabNum)), curFile)
            

        self.__getattribute__("treeWidget_" + currentTabNum).clear()
        self.__getattribute__("textBrowser_" + currentTabNum).clear()
        self.__getattribute__("lineEdit_" + currentTabNum).clear()

        ############################################
        self.data[currentTabNum] = vars[2]
        self.jsonEncoding[currentTabNum] = vars[3]
        self.query[currentTabNum] = None
        self.findCase[currentTabNum] = None
        self.findWhole[currentTabNum] = None
        self.it[currentTabNum] = None
        self.found[currentTabNum] = False
        ############################################
        
        if not curFile == None:
            self.tabWidget.setTabText(tabIndex, os.path.basename(curFile))
            self.tabWidget.setTabToolTip(tabIndex, curFile)
            self.tabWidget.setTabWhatsThis(tabIndex, vars[5])
            if unicode(self.tabWidget.tabToolTip(self.tabWidget.currentIndex()), "utf-8") == curFile:
                self.setWindowTitle("pyJsonEditor - " + curFile)
            self.fill_lineedit_completer(curFile)
        elif curFile == None and self.isTabHoldsFile(currentTabNum):
            self.setTabDirty(currentTabNum, True)
        
        
        
        self.__getattribute__("label_" + currentTabNum + "_4").setText("Encoding: " + self.jsonEncoding[currentTabNum])
        self.__getattribute__("treeWidget_" + currentTabNum).addTopLevelItem(vars[1])
        self.__getattribute__("treeWidget_" + currentTabNum).setCurrentItem(vars[1])
        
        self.setCurStatus(currentTabNum, False)
        

    
    
    
    def applyEditRules(self, currentTabNum, item):
        isInput = self.isTabHoldsInput(currentTabNum)
        
        if isInput:
            self.actionReload.setEnabled(False)
            isFile = False
        else:
            self.actionReload.setEnabled(True)
            isFile = self.isTabHoldsFile(currentTabNum)
                
        self.actionSave.setEnabled(self.isTabDirty(currentTabNum) and isFile)
        
        for action in self.editToolBar.actions():
            action.setDisabled(True)
        self.copyItemAction.setDisabled(False)
        
        isUndoAvailable = len(self.undoDataDict[currentTabNum]) is not 0
        isRedoAvailable = len(self.redoDataDict[currentTabNum]) is not 0
        isValuePlural = item.data(0, QtCore.Qt.UserRole).toPyObject() in [1, 2]
        isNotRoot = item.parent() is not None
        isNotClipEmpty = self.itemClipBoard["item"] is not None
        
        if isNotRoot:
            isRenamable = item.parent().data(0, QtCore.Qt.UserRole).toPyObject() is not 2
            canGoUp = self.itemAbove(item).parent() is not None
            canGoDown = self.itemBelow(item) is not None
            isNotParentRoot = item.parent().parent() is not None
            isNotFirstChild = item.parent().indexOfChild(item) is not 0
            isNotLastChild = item.parent().indexOfChild(item) is not item.parent().childCount() - 1
            isAboveValuePlural = self.itemAbove(item).data(0, QtCore.Qt.UserRole).toPyObject() in [1, 2]
                
        else:
            isRenamable = False
            canGoUp = False
            canGoDown = False
            isNotParentRoot = False
            isNotFirstChild = False
            isNotLastChild = False
            isAboveValuePlural = False
            

        self.undoAction.setEnabled(isUndoAvailable)
        self.redoAction.setEnabled(isRedoAvailable)
        
        self.addChildFirstAction.setEnabled(isValuePlural)
        self.addChildLastAction.setEnabled(isValuePlural)
        self.addSiblingBeforeAction.setEnabled(isNotRoot)
        self.addSiblingAfterAction.setEnabled(isNotRoot)
        
        self.delItemAction.setEnabled(isNotRoot)
        self.renameItemAction.setEnabled(isRenamable and isNotRoot)
        self.cutItemAction.setEnabled(isNotRoot)
        self.pasteItemAsChildAction.setEnabled(isNotClipEmpty and isValuePlural)
        self.pasteItemAsSiblingAction.setEnabled(isNotClipEmpty and isNotRoot)
        
        self.moveItemTopAction.setEnabled(isNotFirstChild and canGoUp and isNotRoot)
        self.moveItemUpAction.setEnabled(isNotFirstChild and canGoUp and isNotRoot)
        self.moveItemDownAction.setEnabled(isNotLastChild and canGoDown and isNotRoot)
        self.moveItemBottomAction.setEnabled(isNotLastChild and canGoDown and isNotRoot)
        self.indentItemAction.setEnabled(isAboveValuePlural and isNotFirstChild and isNotRoot)
        self.unindentItemAction.setEnabled(isNotParentRoot and isNotRoot)
        self.sortItemAction.setEnabled(isValuePlural)
        
            
    
    
    
    def printit(self, item):
        if item == None:
            return

        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        self.__getattribute__("pushButton_" + currentTabNum + "_1").setDisabled(True)
        self.applyEditRules(currentTabNum, item)
        
        path = self.getPath(currentTabNum, item)
        pathData = self.getPathData(currentTabNum, path)
        
        self.__getattribute__("lineEdit_" + currentTabNum).setText("JSON" + path)
        
        self.__getattribute__("textBrowser_" + currentTabNum).blockSignals(True)
        valuePlainText = "%r" % pathData
        if len(valuePlainText) > 300000:
            self.__getattribute__("textBrowser_" + currentTabNum).setPlainText("Value too big, please select children.")
        else:
            self.__getattribute__("textBrowser_" + currentTabNum).setPlainText(valuePlainText)
        self.__getattribute__("textBrowser_" + currentTabNum).blockSignals(False)
        
        try:
            self.__getattribute__("comboBox_" + currentTabNum).setCurrentIndex(self.combo_dict[str(type(pathData))])
        except KeyError:
            QtGui.QMessageBox.critical(self, "Error", "Undefined value type\n\nType: %s" % str(type(pathData)))
            self.__getattribute__("comboBox_" + currentTabNum).setCurrentIndex(9)
        
        try:
            self.__getattribute__("label_" + currentTabNum + "_3").setText("Length: " + str(len(pathData)))
        except TypeError:
            self.__getattribute__("label_" + currentTabNum + "_3").setText("Length: " + "None")

        
        
    def input_json(self):
        dialog = Input_Dialog(self)
        if dialog.exec_():
            self.process_input_json(unicode(dialog.editor.text().toUtf8(), "utf-8"))
    
    def process_input_json(self, json_str):
        currentTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
        
        if not self.dontLoseChanges(currentTabNum):
            return

        jsonInput = cStringIO.StringIO()
        try:
            jsonInput.write(json_str)
        except Exception, e:
            QtGui.QMessageBox.critical(self, "Error", u"<b>%s</b><br><br><b>Reason:</b> %s" % e.__class__.__name__, e.__str__())
            jsonInput.close()
            return

        self.setCurStatus(currentTabNum, True)
        self.emit(QtCore.SIGNAL("handleUrl(PyQt_PyObject,PyQt_PyObject)"), currentTabNum, jsonInput)
            



    def search_tree(self):
        dialog = Find_Dialog(self)
        if dialog.exec_():
            query = dialog.lineedit.text() 
            if query.isEmpty():
                return
            self.searchTabNum = str(self.tabNums[self.tabWidget.currentIndex()])
            self.__getattribute__("treeWidget_" + self.searchTabNum).headerItem().setText(0,"Searching...")
            self.__getattribute__("treeWidget_" + self.searchTabNum).setHeaderHidden(False)
            self.query[self.searchTabNum] = query
            self.findCase[self.searchTabNum] = dialog.checkBox_case.isChecked()
            self.findWhole[self.searchTabNum] = dialog.checkBox_whole.isChecked()
            self.it[self.searchTabNum] = Iter(self.__getattribute__("treeWidget_" + self.searchTabNum))
            self.found[self.searchTabNum] = False
            QtCore.QTimer.singleShot(250, self.search_tree_iter)
        
    
    
    def search_tree_iter(self, next_prev="next"):
        while self.it[self.searchTabNum].value():
            try:
                if not self.it[self.searchTabNum].value().parent() == None:
                    if self.findCase[self.searchTabNum] == True and self.findWhole[self.searchTabNum] == True:
                        if self.it[self.searchTabNum].value().text(0) == self.query[self.searchTabNum]:
                            self.searchResult(self.it[self.searchTabNum].value())
                            break
                    elif self.findCase[self.searchTabNum] == True:
                        if self.it[self.searchTabNum].value().text(0).contains(self.query[self.searchTabNum], QtCore.Qt.CaseSensitive):
                            self.searchResult(self.it[self.searchTabNum].value())
                            break
                    elif self.findWhole[self.searchTabNum] == True:
                        if self.it[self.searchTabNum].value().text(0).toLower() == self.query[self.searchTabNum].toLower():
                            self.searchResult(self.it[self.searchTabNum].value())
                            break
                    else:
                        if self.it[self.searchTabNum].value().text(0).contains(self.query[self.searchTabNum], QtCore.Qt.CaseInsensitive):
                            self.searchResult(self.it[self.searchTabNum].value())
                            break
                self.it[self.searchTabNum].__getattribute__(next_prev)()
            except StopIteration:
                #print "search wrapped"
                if next_prev == "next":
                    self.find_next(True)
                elif next_prev == "previous":
                    self.find_previous(True)

                
                
    
    
    def find_next(self, stop=False):
        self.__getattribute__("treeWidget_" + self.searchTabNum).headerItem().setText(0,"Searching...")
        self.__getattribute__("treeWidget_" + self.searchTabNum).setHeaderHidden(False)
        try:
            if stop:
                raise StopIteration
            self.it[self.searchTabNum] = Iter(self.it[self.searchTabNum].next())
        except StopIteration:
            if self.found[self.searchTabNum] == True:
                #print "search wrapped"
                reply = QtGui.QMessageBox.question(self,"Search Wrapped","Reached end, continue?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    self.it[self.searchTabNum] = Iter(self.__getattribute__("treeWidget_" + self.searchTabNum))
                else:
                    self.__getattribute__("treeWidget_" + self.searchTabNum).setHeaderHidden(True)
                    self.__getattribute__("treeWidget_" + self.searchTabNum).headerItem().setText(0,"Working...")
                    return
            else:
                self.searchReturn()
                QtGui.QMessageBox.information(self, "Info", "No Match")
                return
        self.search_tree_iter("next")


    
    def find_previous(self, stop=False):
        self.__getattribute__("treeWidget_" + self.searchTabNum).headerItem().setText(0,"Searching...")
        self.__getattribute__("treeWidget_" + self.searchTabNum).setHeaderHidden(False)
        try:
            if stop:
                raise StopIteration
            self.it[self.searchTabNum] = Iter(self.it[self.searchTabNum].previous())
        except StopIteration:
            if self.found[self.searchTabNum] == True:
                #print "search wrapped"
                reply = QtGui.QMessageBox.question(self,"Search Wrapped","Reached start, continue?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    self.it[self.searchTabNum] = Iter(self.__getattribute__("treeWidget_" + self.searchTabNum))
                    #self.it[self.searchTabNum] = Iter(self.it[self.searchTabNum].next())
                    #self.it[self.searchTabNum] = Iter(self.it[self.searchTabNum].next())
                    self.find_next()
                    self.find_next()
                    return
                else:
                    self.__getattribute__("treeWidget_" + self.searchTabNum).setHeaderHidden(True)
                    self.__getattribute__("treeWidget_" + self.searchTabNum).headerItem().setText(0,"Working...")
                    return
            else:
                self.searchReturn()
                QtGui.QMessageBox.information(self, "Info", "No Match")
                return
        self.search_tree_iter("previous")
        
        
    
    def searchResult(self,item):
        self.found[self.searchTabNum] = True
        self.actionFind_Next.setEnabled(True)
        self.actionFind_Previous.setEnabled(True)
        self.__getattribute__("treeWidget_" + self.searchTabNum).setHeaderHidden(True)
        self.__getattribute__("treeWidget_" + self.searchTabNum).headerItem().setText(0,"Working...")
        self.__getattribute__("treeWidget_" + self.searchTabNum).scrollToItem(item)
        self.__getattribute__("treeWidget_" + self.searchTabNum).setCurrentItem(item)
        
    
    def searchReturn(self):
        self.found[self.searchTabNum] = False
        self.actionFind_Next.setEnabled(False)
        self.actionFind_Previous.setEnabled(False)
        self.__getattribute__("treeWidget_" + self.searchTabNum).setHeaderHidden(True)
        self.__getattribute__("treeWidget_" + self.searchTabNum).headerItem().setText(0,"Working...")
        
        
    def aboutqt(self):
        QtGui.QMessageBox.aboutQt(self)
    
    def about(self):
        QtGui.QMessageBox.about(self, "About",
                u"""<b>pyJsonEditor</b> v %s
                <p>Copyright &copy; 2009-2010 Volkan Çetin, All rights reserved.</p>
                <p>A simple PyQt4 application for viewing and editing JSON.</p>
                <p>Python %s - Qt %s - PyQt %s on %s</p>""" % (
                __version__, platform.python_version(),
                QtCore.QT_VERSION_STR, QtCore.PYQT_VERSION_STR, platform.system()))
            


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = JsonEditor()
    window.showMaximized()
    sys.exit(app.exec_())
    
    
    
    


