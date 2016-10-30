# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 01:57:46 2016

@author: Mauricio
"""

import sys
from PyQt4 import QtGui, uic

uiFile = uic.loadUiType('main.ui')[0]
uiFile2 = uic.loadUiType('view_2.ui')[0]

class Window(QtGui.QMainWindow, uiFile):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)        
        self.bipBipCount = 0
        self.digamoCount = 0
        self.setupUi(self)
        self.pushButton_more_bip.clicked.connect(self.bip)  
        self.pushButton_more_digamo.clicked.connect(self.digamo)
        self.pushButton_reset.clicked.connect(self.reset) 
        self.pushButton_new_window.clicked.connect(self.secondWindow) 
        self.window2 = None         
         
    def bip(self):
        self.bipBipCount += 1 
        self.lcdNumber_bip.display(int(self.bipBipCount))  
        
    def digamo(self):
        self.digamoCount += 1 
        self.lcdNumber_digamo.display(int(self.digamoCount))
        
    def reset(self):
        self.bipBipCount = 0
        self.lcdNumber_bip.display(int(0)) 
        self.digamoCount = 0 
        self.lcdNumber_digamo.display(int(0))       
      
    def secondWindow(self): 
        print('nnnn')
        #if self.window2 is None:
        self.window2 = Window2(self)
        self.window2.show()
        
        
class Window2(QtGui.QMainWindow, uiFile2): 
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent) 
        self.setupUi(self)       
        self.pushButton_exit.clicked.connect(self.btnExit)      
           
    def btnExit(self):
        print('boton exit')       
        
        
#Ejecutar        
def main():
    app = QtGui.QApplication(sys.argv)
    
    window = Window(None)
    window.setWindowTitle('PyContador')
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()       