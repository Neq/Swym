#!/usr/bin/env python

""" First draft
    Planned for 0.0.1: Syntax Highlighting and basic editor actions
"""

import sys
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
     
        self.setupFileMenu()
        self.setupEditor()
    
        self.setCentralWidget(self.editor)
        self.setWindowTitle(self.tr("Swym - Untitled"))
    
    def newFile(self):
        self.editor.clear()
        self.setWindowTitle(self.tr("Swym - Untitled"))
    
    def openFile(self, path=""):
        fileName = QtCore.QString(path)
    
        if fileName.isEmpty():
            fileName = QtGui.QFileDialog.getOpenFileName(self, self.tr("Open File"), "","")
                                                         
        if not fileName.isEmpty():
            inFile = QtCore.QFile(fileName)
            if inFile.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
                self.editor.setPlainText(QtCore.QString(inFile.readAll()))
    
    def setupEditor(self):    
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(10)
    
        self.editor = QtGui.QTextEdit()
        self.editor.setFont(font)

        if not self.editor:
            self.setWindowTitle(self.tr("Swym - Untitled *"))
    
    def setupFileMenu(self):
        fileMenu = QtGui.QMenu(self.tr("&File"), self)
        self.menuBar().addMenu(fileMenu)
        
        newFileAct = QtGui.QAction(self.tr("&New File"), self)
        newFileAct.setShortcut(QtGui.QKeySequence(self.tr("Ctrl+N", "File|New File")))
        self.connect(newFileAct, QtCore.SIGNAL("triggered()"), self.newFile)
        fileMenu.addAction(newFileAct)
        
        openFileAct = QtGui.QAction(self.tr("&Open..."), self)
        openFileAct.setShortcut(QtGui.QKeySequence(self.tr("Ctrl+O", "File|Open")))
        self.connect(openFileAct, QtCore.SIGNAL("triggered()"), self.openFile)
        fileMenu.addAction(openFileAct)
    
        fileMenu.addAction(self.tr("E&xit"), QtGui.qApp, QtCore.SLOT("quit()"),
                           QtGui.QKeySequence(self.tr("Ctrl+Q", "File|Exit")))           
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    #window.resize(640, 512)
    window.resize(1024,768);
    window.show()
    #window.openFile(":/examples/example")
    sys.exit(app.exec_())
