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
#from ui_eaf import Ui_eaf

from eaf_dlg import Ui_Dialog
from dock import Ui_DockWidget
from wizards import wizard1
#from wizard import Ui_Wizard

#class eafdialog(QtGui.QDialog):
class eafdialog(QtGui.QDockWidget):    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        #self.ui = Ui_Dialog()
        self.ui = Ui_DockWidget()        
        self.ui.setupUi(self)
        

        self.ui.tabWidget.addTab(wizard1(),  "Initiation and Planning")
        self.ui.tabWidget.addTab(QtGui.QWidget(),  "Definition of Scope")
        self.ui.tabWidget.addTab(QtGui.QWidget(),  "Identify Issues and Indicators")
        self.ui.tabWidget.addTab(QtGui.QWidget(),  "Management Measures and Monitoring Systems")
        
        
     
        

