# -*- coding: utf-8 -*-
"""
/***************************************************************************
 eafDialog
                                 A QGIS plugin
 Wizard that guides the users through the process of implementing the GIS functionality, within an EAF approach
                             -------------------
        begin                : 2013-10-02
        copyright            : (C) 2013 by FAO
        email                : joana.simoes@fao.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui

from qgis.core import *
from qgis.gui import *

from eaf_dlg import Ui_Dialog
from dock import Ui_DockWidget
from wizards import wizard1
from frmintro import Ui_frmIntro



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class frmIntro(QtGui.QWidget):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmIntro()
        self.ui.setupUi(self)   

#class eafdialog(QtGui.QDialog):
class eafdialog(QtGui.QDockWidget, Ui_Dialog):    

    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        #self.ui = Ui_Dialog()
        
        self.ui = Ui_DockWidget()        
        self.ui.setupUi(self)
        
        self.ui.tabWidget.addTab(frmIntro(),  "Welcome")

        self.ui.wiz1=wizard1(eaf)        
        #self.wiz1_count=sum(self.ui.wiz1.pageIds())
            
        QtCore.QObject.connect(self.ui.wiz1, QtCore.SIGNAL(_fromUtf8("finished(int)")), self.nextTab)        
        QtCore.QObject.connect(self.ui.wiz1, QtCore.SIGNAL(_fromUtf8("currentIdChanged(int)")), self.updateProgress)

    def removeAllTabs(self):
        i= self.ui.tabWidget.count()-1
        while i >= 0:
            self.ui.tabWidget.removeTab(i)
            i=i-1
     
    def newProject(self):

        self.removeAllTabs()
        self.ui.wiz1.restart()
        self.ui.wiz1.reset()
                            
        self.ui.tabWidget.addTab(self.ui.wiz1,  "Initiation and Planning")
        self.ui.tabWidget.addTab(QtGui.QWidget(),  "Definition of Scope")
        self.ui.tabWidget.addTab(QtGui.QWidget(),  "Identify Issues and Indicators")
        self.ui.tabWidget.addTab(QtGui.QWidget(),  "Management Measures and Monitoring Systems")
                        
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.progressBar.setValue(0)        
        
    def openProject(self):
        print "open project"

    def saveProject(self):
        print "save project"        

    def nextTab(self):
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.currentIndex()+1)      
        self.ui.progressBar.setValue(100/self.ui.tabWidget.count()*self.ui.tabWidget.currentIndex())          

    def updateProgress(self,index):
        if isinstance(self.sender(), QtGui.QWizard):
            wizard = self.sender()
            if wizard.currentId()>0:
                self.ui.progressBar.setValue(100/self.ui.tabWidget.count()*self.ui.tabWidget.currentIndex()+
                                             (100/self.ui.tabWidget.count()*wizard.currentId()/sum(wizard.pageIds())))
            else:
                self.ui.progressBar.setValue(0)
            #print sum(wizard.pageIds())
            
        
