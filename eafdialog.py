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

import sys, os.path

import json

from PyQt4 import QtCore, QtGui

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from dock import Ui_DockWidget
from wizard import Ui_Wizard

from dlgoptions import Ui_DlgOptions

from pages import  page0dialog
from pages import  page1dialog
from pages import  page1_1dialog
from pages import  page1_2dialog
from pages import  page1_3dialog
from pages import  page2dialog
from pages import  page3dialog
from pages import  page3_1dialog
from pages import  page3_2dialog
from pages import  page4dialog
from pages import  page4_1dialog
from pages import  page5dialog
from pages import  page6dialog
from pages import  page7dialog

from layers import LyrMngr

## wiz
#
#  Class that implements the wizard; 
#
################################################    
class wiz(QtGui.QWizard):
    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Wizard()
        self.ui.setupUi(self)
        self.eaf=eaf        
        self.lyrMngr=LyrMngr()
        
    def showHelp(self):
        #TODO: review this
        showPluginHelp("eaf", "/home/joana/git/eaf/help/build/html/index.html")
        
    def houseKeeping(self):
        self.lyrMngr.removeAll()
        self.eaf.dockWidget.ui.toolOptions.setVisible(False)
        self.eaf.dockWidget.ui.lbOptions.setVisible(False)
        
## dlgoptions
#
#  Class that implements the options dialogue; 
#
################################################    
class options(QtGui.QDialog):
    
    ok = QtCore.pyqtSignal()     
    undoText=""
    
    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_DlgOptions()
        self.ui.setupUi(self)
        self.eaf=eaf
                
    def validatePath(self,path):
        aDir=QtCore.QDir(path)
        return aDir.exists()        
                                               
    def setDataPath(self):
        dir = QtGui.QFileDialog.getExistingDirectory(self, unicode("Set Directory"),
            QtCore.QDir.tempPath(),
            QtGui.QFileDialog.ShowDirsOnly
            | QtGui.QFileDialog.DontResolveSymlinks);

        self.ui.lineData.setText(dir)
        
    def accept(self):
        if self.validatePath(self.ui.lineData.text()):
            self.ok.emit()
            self.hide()
        else:            
            self.eaf.iface.messageBar().pushMessage("Error", "Invalid Directory", level=QgsMessageBar.CRITICAL)
            self.ui.lineData.setText(self.undoText)
            
    def reject(self):
        self.ui.lineData.setText(self.undoText)
        self.hide()
        
    def showEvent(self, event):
        self.undoText=self.ui.lineData.text()        
       
## EAF Dialogue
#
#  This is the main plugin dialogue; 
#
#  Here we initialize a wizard; we store a pointer to eaf (where the QGIS interface is) and to the wizard.
#  This class owns the progress bar.
################################################            
class eafdialog(QtGui.QDockWidget):    

    ## Constructor
    #
    #  This is a constructor
    ##########################################################
    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        
        self.ui = Ui_DockWidget()        
        self.ui.setupUi(self)        
        self.mywiz=wiz(eaf)
        self.options = options(eaf)
        self.options.ui.lineData.setText(self.mywiz.lyrMngr.datapath)
                
        self.ui.verticalLayout.insertWidget(0,self.mywiz)
        self.mywiz.setVisible(False)
        
        self.ui.toolOptions.setVisible(False)
        self.ui.lbOptions.setVisible(False)            
                        
        QtCore.QObject.connect(self.mywiz, QtCore.SIGNAL("currentIdChanged(int)"), self.updateProgress)
        QtCore.QObject.connect(self.mywiz, QtCore.SIGNAL("currentIdChanged(int)"), self.enableDataPath)
        QtCore.QObject.connect(self.options, QtCore.SIGNAL("ok()"),self.setUserDataPathFromLine)
        QtCore.QObject.connect(self.mywiz.lyrMngr, QtCore.SIGNAL("dataPathChanged(QString)"),self.updateLineEdit)
        
        self.eaf=eaf
        self.initPages()
        self.countPages()

    def updateLineEdit(self,path):
        if (self.options.ui.lineData.text()!=path):
            self.options.ui.lineData.setText(path)
        
    def setUserDataPathFromLine(self):
        self.setUserDataPath(self.options.ui.lineData.text())

    def setUserDataPath(self,aPath):
        self.mywiz.lyrMngr.setUserDataPath(aPath)
     
    ## Counts the number of pages in the Wizard
    #
    #  This function counts the number of pages in the wizard, for calculating the percentage in the progress bar.
    #  Since it is a non-linear wizard, and to keep it simple, we ignore the pages that implement branches, and stick to the major ID's only (10,20,etc).    
    ##########################################################     
    def countPages(self):
        #We have to do this, to take in account he non-linear structure 

        cnt=0
        #ok=True
        for i in self.mywiz.pageIds():
            #if self.mywiz.page(i).objectName().find('_')!= -1 and ok==True: #for now we dont count the sub-pages                 
                #cnt=cnt+1
                #ok=False
            if self.mywiz.page(i).objectName().find('_')== -1:
                cnt=cnt+1
                #ok=True

        self.cnt=cnt
        
    ## Init Pages
    #
    #  Inserts the pages in the wizard, forcing them to a specific ID.
    #  The jumps in ID's between major pages are of 10, so that we are able to insert more pages later without refactoring the whole thing.
    #  This forces to a discipline of reimplementing nextID() in the page classes.      
    ##########################################################             
    def initPages(self):
        self.mywiz.setPage(0, page0dialog(self.eaf,self.mywiz))
        self.mywiz.setPage(10, page1dialog(self.eaf,self.mywiz))
        self.mywiz.setPage(11, page1_1dialog(self.eaf,self.mywiz))
        self.mywiz.setPage(12, page1_2dialog(self.eaf,self.mywiz))
        self.mywiz.setPage(13, page1_3dialog(self.eaf,self.mywiz))                                                       
        self.mywiz.setPage(20, page2dialog(self.eaf,self.mywiz))                        
        self.mywiz.setPage(30, page3dialog(self.eaf,self.mywiz))                        
        self.mywiz.setPage(31, page3_1dialog(self.eaf,self.mywiz))
        self.mywiz.setPage(32, page3_2dialog(self.eaf,self.mywiz))                                                        
        self.mywiz.setPage(40, page4dialog(self.eaf,self.mywiz))
        self.mywiz.setPage(41, page4_1dialog(self.eaf,self.mywiz))                                                        
        self.mywiz.setPage(50, page5dialog(self.eaf,self.mywiz))                        
        self.mywiz.setPage(60, page6dialog(self.eaf,self.mywiz))                        
        self.mywiz.setPage(70, page7dialog(self.eaf,self.mywiz))

    ## New Project
    #
    #  Initializes a project by restarting the wizard, making it visible, setting the first ID to 0 and resetting the UI.
    ##########################################################                                  
    def newProject(self):

        self.mywiz.setStartId(0)
        
        if not self.mywiz.isVisible():
            self.mywiz.setVisible(True)
            self.ui.toolOptions.setVisible(True)
            self.ui.lbOptions.setVisible(True)            
            
        self.mywiz.restart()
                
        for i in self.mywiz.pageIds():
            self.mywiz.page(i).resetUI() 
            
        self.mywiz.lyrMngr.restart()
              
    ## Open Project
    #
    #  Reads project from JSON file.
    #  In this implementation we set the start ID to the one saved on the project, which means you cannot go back on the wizard
    # , once you save something (it makes sense). Thus, we only save the ID of the current page and the current state of the UI on this page. 
    #  The data belonging to this page will be automatically loaded.
    ##########################################################                                                          
    def openProject(self):
                
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open Project', "", "Project Files (*.json)")        
        
        if filename:
            try:
                json_data=open(filename)
            except IOError as e:
                print 'Error reading file:', e
                raise
    
            try:            
                data = json.load(json_data)
                json_data.close()
            except Exception as e:
                print 'Error parsing json:', e
                raise
    
            try:            
                self.readDataPath(data["dataPath"])
            except Exception as e:
                print 'Error setting data path:', e
                raise

            #Remove any existing layers before loading new ones
            self.mywiz.lyrMngr.removeAll()
            
            curPage=data["curPage"]                        
            try:
                self.setCurPage(curPage)
            except Exception as e:
                print 'Error setting current page:', e
                raise
            
            try:            
                self.readPageUI(curPage,data["curUI"])
            except Exception as e:
                print 'Error setting current page UI:', e
                raise                          
             
            
             
    ## Show Options
    #
    #  Calls the dlgOptions dialogue.
    ##########################################################                                  
    def showOptions(self):
                
        if not self.options.isVisible():
            self.options.show()        

    def readDataPath(self,path):
        
        if self.options.validatePath(path):
            self.setUserDataPath(path)            
        else:
            #self.eaf.iface.messageBar().pushMessage("Error", "Invalid Data Path", level=QgsMessageBar.CRITICAL)
            raise Exception('Invalid Data Path')
                         
    ## Set Current Page
    #
    #  This function is used by OpenProject.     
    # It sets the startID from the current page, makes sure the wizard is visible and restarts it.
    ##########################################################          
    def setCurPage(self,ID):        
        self.mywiz.setStartId(ID)

        if not self.mywiz.isVisible():
            self.mywiz.setVisible(True)
            self.ui.toolOptions.setVisible(True)
            self.ui.lbOptions.setVisible(True)                        
            
        self.mywiz.restart()

    ## Read Page UI
    #
    #  This function is used by openProject.     
    # It sets the state of the UI on the relevant page, from a JSON string.
    ##########################################################    
    def readPageUI(self,ID,strUI):
        myPage=self.mywiz.page(ID)
        myPage.readPageUI(strUI)
        
    ## Save Project
    #
    #  Saves project on JSON file.
    # We only save the ID of the current page and the current state of the UI on this page. 
    ##########################################################          
    def saveProject(self):
        
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save Project', "", "Project Files (*.json)")
        
        if filename:            
            ID=self.getCurPage()
            UI=self.getPageUI()
            datapath=self.mywiz.lyrMngr.userPath
    
            data = {"curPage": ID, "curUI": UI, "dataPath": datapath}
    
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
                
            outfile.close()            

    ## Get Current Page
    #
    #  Convenience function to retrieve the current's page ID.
    ##########################################################  
    def getCurPage(self):
        return self.mywiz.currentId()

    ## Get Page UI
    #
    #  This function is used by saveProject.     
    # It asks the relevant page to provide a JSON string, with the current state of the UI.
    ##########################################################                        
    def getPageUI(self):         
        myPage=self.mywiz.currentPage()
        strJSON=myPage.getPageUI()        
        return strJSON        

    ## Update Progress Bar
    #
    #  This function is called by a signal, emitted every time we change page.
    # It updates the progress bar, based on the current iD and the self.cnt variable, calculated by countPages()
    ##########################################################                                   
    def updateProgress(self,index):
        if isinstance(self.sender(), QtGui.QWizard):
            wizard = self.sender()

            #val=(wizard.currentId()+1)*100/self.cnt
            cid=wizard.currentId()
            total=self.cnt
            val=(cid/10+1)*100/total
            self.ui.progressBar.setValue(val)
            
    ## Enable Data Path
    #
    #  This function is called by a signal, emitted every time we change page.
    # It enables/disables the data path lineEdit, according to the current page ID
    ##########################################################                                   
    def enableDataPath(self,index):
        cut=20
        self.options.ui.lineData.setEnabled(index < cut)
        self.options.ui.toolData.setEnabled(index < cut)
