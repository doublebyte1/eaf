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

#import sqlite3
import sys, os.path

from PyQt4 import QtCore, QtGui

from qgis.core import *
from qgis.gui import *

from dock import Ui_DockWidget
from wizard import Ui_Wizard

from pages import  page0dialog
from pages import  page1dialog
from pages import  page1_1dialog
from pages import  page1_2dialog
from pages import  page1_3dialog
from pages import  page2dialog
from pages import  page3dialog
from pages import  page4dialog
from pages import  page5dialog
from pages import  page6dialog
from pages import  page7dialog

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))

class wiz(QtGui.QWizard):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Wizard()
        self.ui.setupUi(self)
            
class eafdialog(QtGui.QDockWidget):    

    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        
        self.ui = Ui_DockWidget()        
        self.ui.setupUi(self)        
        self.mywiz=wiz()
        
        self.ui.verticalLayout.insertWidget(0,self.mywiz)
        self.mywiz.setVisible(False)
                
        QtCore.QObject.connect(self.mywiz, QtCore.SIGNAL("currentIdChanged(int)"), self.updateProgress)
     
        #try:
         #   conn = sqlite3.connect(os.path.join(datapath, "eaf.db"))
        #except sqlite3.Error as e:
         #   print "An error occurred:", e.args[0]  

        #self.conn = conn        
        
        self.eaf=eaf
        self.initPages()
     
    def initPages(self):
        self.mywiz.setPage(0, page0dialog(self.eaf))
        self.mywiz.setPage(1, page1dialog())
        self.mywiz.setPage(11, page1_1dialog())
        self.mywiz.setPage(12, page1_2dialog())
        self.mywiz.setPage(13, page1_3dialog())                                                        
        self.mywiz.setPage(2, page2dialog())                        
        self.mywiz.setPage(3, page3dialog())                        
        self.mywiz.setPage(4, page4dialog())                        
        self.mywiz.setPage(5, page5dialog())                        
        self.mywiz.setPage(6, page6dialog())                        
        self.mywiz.setPage(7, page7dialog())
                     
    def newProject(self):

        if not self.mywiz.isVisible():
            self.mywiz.setVisible(True)
            
        self.mywiz.restart()
                        
    def openProject(self):
        print "open project"

    def saveProject(self):
        
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save Project', "", "Project Files (*.json)")
        #fname = open(filename, 'w')
        #fname.write('test')
        #fname.close()        
        print filename
        #name = ('test')
        #page_id=self.mywiz.currentId()
        #values=(name,page_id)
        
        #c = self.conn.cursor()
        #c.execute('INSERT INTO projects(name,page) values(?,?)', values)
        
        #self.conn.commit()

    def updateProgress(self,index):
        if isinstance(self.sender(), QtGui.QWizard):
            wizard = self.sender()
            cnt=len(wizard.pageIds())
            val=(wizard.currentId()+1)*100/cnt
            self.ui.progressBar.setValue(val)
            
