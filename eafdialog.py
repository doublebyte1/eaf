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

from dock import Ui_DockWidget
from wizard import Ui_Wizard

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class wiz(QtGui.QWizard):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Wizard()
        self.ui.setupUi(self)
        
        #self.setPixmap(QtGui.QWizard.LogoPixmap, QtGui.QPixmap(":/plugins/eaf/eaf1.jpg"))

    
class eafdialog(QtGui.QDockWidget):    

    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        
        self.ui = Ui_DockWidget()        
        self.ui.setupUi(self)        
        self.mywiz=wiz()
        
        self.ui.verticalLayout.insertWidget(0,self.mywiz)
                
        QtCore.QObject.connect(self.mywiz, QtCore.SIGNAL(_fromUtf8("currentIdChanged(int)")), self.updateProgress)
     
    def newProject(self):

        if not self.mywiz.isVisible():
            self.mywiz.setVisible(True)
            
        self.mywiz.restart()
        
    def openProject(self):
        print "open project"

    def saveProject(self):
        print "save project"        

    def updateProgress(self,index):
        if isinstance(self.sender(), QtGui.QWizard):
            wizard = self.sender()
            cnt=len(wizard.pageIds())
            val=(wizard.currentId()+1)*100/cnt
            self.ui.progressBar.setValue(val)
            
        
