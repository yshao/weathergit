# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, Qsci


class Editor(Qsci.QsciScintilla):
    def __init__(self):
        Qsci.QsciScintilla.__init__(self)
        self.EOL_MODES = {"\r\n": Qsci.QsciScintilla.EolWindows, "\n": Qsci.QsciScintilla.EolUnix, "\r": Qsci.QsciScintilla.EolMac}
        # Order is important:
        self.EOL_CHARS = (("\r\n", 'nt'), ("\n", 'posix'), ("\r", 'mac'))
        self.markerNum = self.markerDefine(self.Minus)

    
    def set_text(self, text):
        """Set the text of the editor"""
        self.setText(text)
        self.set_eol_mode(text)


    def get_eol_chars(self, text):
        """Get text EOL characters"""
        for eol_chars, _os_name in self.EOL_CHARS:
            if text.find(eol_chars) > -1:
                return eol_chars


    def set_eol_mode(self, text):
        """Set QScintilla widget EOL mode based on *text* EOL characters"""
        eol_chars = self.get_eol_chars(text)
        if eol_chars is not None:
            self.setEolMode(self.EOL_MODES[eol_chars])

        
    def get_line_separator(self):
        """Return line separator based on current EOL mode"""
        current_mode = self.eolMode()
        for eol_chars, mode in self.EOL_MODES.iteritems():
            if current_mode == mode:
                return eol_chars
        else:
            return ''


    def highlightLine(self, lineno, endlineno, colno, endcolno):
        if endlineno == None:
            endlineno = lineno
        if endcolno == None:
            endcolno = colno
        if lineno == 1 and endlineno == 1:
            self.setSelection(lineno-1, colno, endlineno-1, endcolno)
        elif lineno == 1:
            self.setSelection(lineno-1, colno, endlineno-1, endcolno-1)
        else:
            self.setSelection(lineno-1, colno-1, endlineno-1, endcolno-1)
        self.markerAdd(lineno-1, self.markerNum)
        self.ensureLineVisible(lineno-1)

        
    def paste(self):
        """
        Reimplement QsciScintilla's method to fix the following issue:
        on Windows, pasted text has only 'LF' EOL chars even if the original
        text has 'CRLF' EOL chars
        """
        clipboard = QtGui.QApplication.clipboard()
        text = unicode(clipboard.text().toUtf8(), "utf-8")
        if len(text.splitlines()) > 1:
            eol_chars = self.get_line_separator()
            clipboard.setText(eol_chars.join((text+eol_chars).splitlines()))
        # Standard paste
        Qsci.QsciScintilla.paste(self)





class Input_Dialog(QtGui.QDialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self,parent)
        self.parent = parent
        
        self.editor = Editor()
        self.editor.setUtf8(True)
        
        self.editor.setWrapMode(Qsci.QsciScintilla.WrapWord)
    
        ## define the font to use
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(10)
        # the font metrics here will help
        # building the margin width later
        fm = QtGui.QFontMetrics(font)
    
        ## set the default font of the self.editor
        ## and take the same font for line numbers
        self.editor.setFont(font)
        self.editor.setMarginsFont(font)
    
        ## Line numbers
        # conventionnaly, margin 0 is for line numbers
        self.editor.setMarginWidth(0, fm.width( "00000" ) + 5)
        self.editor.setMarginLineNumbers(0, True)
    
        ## Edge Mode shows a red vetical bar at 80 chars
        #self.editor.setEdgeMode(Qsci.QsciScintilla.EdgeLine)
        #self.editor.setEdgeColumn(80)
        #self.editor.setEdgeColor(QtGui.QColor("#FF0000"))
    
        ## Folding visual : we will use boxes
        self.editor.setFolding(Qsci.QsciScintilla.BoxedTreeFoldStyle)
    
        ## Braces matching
        self.editor.setBraceMatching(Qsci.QsciScintilla.SloppyBraceMatch)
    
        ## Editing line color
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QtGui.QColor("#CDA869"))
    
        ## Margins colors
        # line numbers margin
        self.editor.setMarginsBackgroundColor(QtGui.QColor("#333333"))
        self.editor.setMarginsForegroundColor(QtGui.QColor("#CCCCCC"))
    
        # folding margin colors (foreground,background)
        self.editor.setFoldMarginColors(QtGui.QColor("#99CC66"),QtGui.QColor("#333300"))
    
        ## Choose a lexer
        lexer = Qsci.QsciLexerJavaScript()
        lexer.setDefaultFont(font)
        self.editor.setLexer(lexer)
        
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self, QtCore.SLOT("accept()"))
        self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self, QtCore.SLOT("reject()"))
        
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.buttonBox)
        
        self.setLayout(self.layout)
        self.resize(600,400)
        self.setWindowTitle("Input JSON")
        
        
         
