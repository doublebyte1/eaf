import sys, os.path
import json
from PyQt4 import QtCore, QtGui

from page0 import Ui_Page0
from page1 import Ui_Page1
from page1_1 import Ui_Page1_1
from page1_2 import Ui_Page1_2
from page1_3 import Ui_Page1_3
from page2 import Ui_Page2
from page3 import Ui_Page3
from page3_1 import Ui_Page3_1
from page4 import Ui_Page4
from page5 import Ui_Page5
from page6 import Ui_Page6
from page7 import Ui_Page7

from qgis.core import *
from qgis.gui import *

import eaf
import layers

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))

## Generic Wizard Page
#
#  Base class for a wizard page. 
#  It provides all sorts of virtual methods, and it stores pointers to the eaf class and to the wizard.
################################################   
class myWizardPage(QtGui.QWizardPage):
    
    def __init__(self,eaf,mywiz):
        self.eaf=eaf
        self.mywiz=mywiz
            
    def readPageUI(self,strUI):
        #Please reimplement this in the relevant derived classes
        return None 

    def getPageUI(self):
        #Please reimplement this in the relevant derived classes        
        return None 
    
    def resetUI(self):
        return None
        
    def setLayers(self):
        print "set layers"

    def zoomFull(self):        
        canvas=self.eaf.iface.mapCanvas()
        canvas.zoomToFullExtent()
        
    def zoomIn(self):        
        canvas=self.eaf.iface.mapCanvas()
        canvas.zoomIn()        
        
    def showEvent(self, event):
        self.setLayers()
        return QtGui.QWizardPage.showEvent(self,event)
                        
class page0dialog(myWizardPage):
        
    def __init__(self,eaf,mywiz):        
        super(page0dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page0()
        self.ui.setupUi(self)
                
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))
                        
    def setLayers(self):
        self.mywiz.lyrMngr.setLayers(None)        
                                                
class page1dialog(myWizardPage):
    def __init__(self,eaf,mywiz):        
        super(page1dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1()
        self.ui.setupUi(self)

    def setPageId(self,index):
        self.nextId()
                        
    def nextId(self):
        ind=self.ui.cmbMethod.currentIndex()
        if ind==1:
            return 11
        elif ind==2:
            return 12
        elif ind==3:
            return 13                         
        else:
            return 10#current page

    def readPageUI(self,strUI):
        self.ui.cmbMethod.setCurrentIndex(strUI["cmbMethod"])
        
    def getPageUI(self):
        myUI={'cmbMethod': self.ui.cmbMethod.currentIndex()}
        return myUI
    
    def resetUI(self):
        self.ui.cmbMethod.setCurrentIndex(0)
        
    def setLayers(self):
        self.mywiz.lyrMngr.setLayers([layers.strCountries,layers.strEez,layers.strWpi])
        self.zoomFull()
                                                                                                   
class page1_1dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page1_1dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_1()
        self.ui.setupUi(self)                                
        
    def nextId(self):
        return 20

    
    def showEvent(self, event):
        super(page1_1dialog,self).showEvent(event)
        self.eaf.iface.actionZoomIn().trigger()        
        #TODO: store current maptool and come back to it later
            
    def validatePage(self):        
        return self.mywiz.lyrMngr.createLayerFromExtent(self.eaf)  and self.mywiz.lyrMngr.clipLayers() 
                        
    def setLayers(self):
        self.mywiz.lyrMngr.setLayers([layers.strCountries,layers.strEez,layers.strWpi])
        self.zoomFull()        
            
class page1_2dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page1_2dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_2()
        self.ui.setupUi(self)
        
        self.initCombo()

    def initCombo(self):
        list=self.mywiz.lyrMngr.readCountries()
        self.ui.cmbCountries.addItems(list)

    def validatePage(self):        
        return self.mywiz.lyrMngr.createLayerFromCountry(eaf,self.ui.cmbCountries.currentText()) 

    def nextId(self):
        return 20

class page1_3dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page1_3dialog,self).__init__(eaf,mywiz)                
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_3()
        self.ui.setupUi(self)

    def nextId(self):
        return 20
                    
class page2dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page2dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page2()
        self.ui.setupUi(self)
        
    def readPageUI(self,strUI):        
        self.ui.checkMaritime.setChecked(strUI["checkMaritime"])
        self.ui.checkCoastline.setChecked(strUI["checkCoastline"])
        self.ui.checkLandingSites.setChecked(strUI["checkLandingSites"])
        self.ui.checkOther.setChecked(strUI["checkOther"])
        self.ui.checkBathymetry.setChecked(strUI["checkBathymetry"])
        
        self.ui.cmbMaritime.setCurrentIndex(strUI["cmbMaritime"])
        self.ui.cmbCoastline.setCurrentIndex(strUI["cmbCoastline"])        
        self.ui.cmbLandingSites.setCurrentIndex(strUI["cmbLandingSites"])
        self.ui.cmbOther.setCurrentIndex(strUI["cmbOther"])                
        self.ui.cmbBathymetry.setCurrentIndex(strUI["cmbBathymetry"])

    def getPageUI(self):
        myUI={'checkMaritime': self.ui.checkMaritime.isChecked(),'checkCoastline': self.ui.checkCoastline.isChecked(),
              'checkLandingSites': self.ui.checkLandingSites.isChecked(),'checkOther': self.ui.checkOther.isChecked(),
              'checkBathymetry': self.ui.checkBathymetry.isChecked(),
              'cmbMaritime': self.ui.cmbMaritime.currentIndex(),
              'cmbCoastline': self.ui.cmbCoastline.currentIndex(),
              'cmbLandingSites': self.ui.cmbLandingSites.currentIndex(),
              'cmbOther': self.ui.cmbOther.currentIndex(),
              'cmbBathymetry': self.ui.cmbBathymetry.currentIndex()}
        return myUI 
                            
    def resetUI(self):
        self.ui.checkMaritime.setChecked(False)
        self.ui.checkCoastline.setChecked(False)
        self.ui.checkLandingSites.setChecked(False)
        self.ui.checkOther.setChecked(False)
        self.ui.checkBathymetry.setChecked(False)
        
        self.ui.cmbMaritime.setCurrentIndex(0)
        self.ui.cmbCoastline.setCurrentIndex(0)        
        self.ui.cmbLandingSites.setCurrentIndex(0)
        self.ui.cmbOther.setCurrentIndex(0)                
        self.ui.cmbBathymetry.setCurrentIndex(0)

    def nextId(self):
        return 30

    def setLayers(self):
        #self.mywiz.lyrMngr.setLayers([layers.strCountries,layers.strEez,layers.strWpi])
        self.mywiz.lyrMngr.setLayers([layers.strEezClp,layers.strWpiClp,layers.strCountriesClp])
        self.zoomFull()
                                                                                      
class page3dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page3dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page3()
        self.ui.setupUi(self)
        
    def readPageUI(self,strUI):
        self.ui.cmbMethod2.setCurrentIndex(strUI["cmbMethod2"])        
        
    def getPageUI(self):
        myUI={'cmbMethod2': self.ui.cmbMethod2.currentIndex()}
        return myUI                
         
    def resetUI(self):
        self.ui.cmbMethod2.setCurrentIndex(0)
        
    def nextId(self):
        ind=self.ui.cmbMethod2.currentIndex()
        if ind==1:
            return 31
        #elif ind==2:
         #   return 3
        #elif ind==3:
         #   return 4                          
        else:
            return 30#current page
                                                
    def setLayers(self):
        self.mywiz.lyrMngr.setLayers([layers.strEezClp,layers.strWpiClp,layers.strCountriesClp])
        self.zoomFull()
        
class page3_1dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page3_1dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page3_1()
        self.ui.setupUi(self)                                
        
    def nextId(self):
        return 40
    
    def showEvent(self, event):
        super(page3_1dialog,self).showEvent(event)
        self.eaf.iface.actionZoomIn().trigger()        
        #TODO: store current maptool and come back to it later
            
    def validatePage(self):        
        return self.mywiz.lyrMngr.createLayerFromExtent(self.eaf)  and self.mywiz.lyrMngr.reclipLayers() 
                
    def setLayers(self):
        self.mywiz.lyrMngr.setLayers([layers.strEezClp,layers.strWpiClp,layers.strCountriesClp])
        self.zoomFull()        
                         
class page4dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page4dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page4()
        self.ui.setupUi(self)

    def readPageUI(self,strUI):        
        self.ui.checkFishingAreas.setChecked(strUI["checkFishingAreas"])
        self.ui.checkLandingSites.setChecked(strUI["checkLandingSites"])
        self.ui.checkBathymetry.setChecked(strUI["checkBathymetry"])
        
        self.ui.cmbFishingAreas.setCurrentIndex(strUI["cmbFishingAreas"])
        self.ui.cmbLandingSites.setCurrentIndex(strUI["cmbLandingSites"])
        self.ui.cmbBathymetry.setCurrentIndex(strUI["cmbBathymetry"])
        
    def getPageUI(self):
        myUI={'checkFishingAreas': self.ui.checkFishingAreas.isChecked(),
              'checkLandingSites': self.ui.checkLandingSites.isChecked(),
              'checkBathymetry': self.ui.checkBathymetry.isChecked(),              
              'cmbLandingSites': self.ui.cmbLandingSites.currentIndex(),
              'cmbFishingAreas': self.ui.cmbFishingAreas.currentIndex(),
              'cmbBathymetry': self.ui.cmbBathymetry.currentIndex()}
        return myUI 

    def resetUI(self):
        self.ui.checkFishingAreas.setChecked(False)
        self.ui.checkLandingSites.setChecked(False)
        self.ui.checkBathymetry.setChecked(False)
        
        self.ui.cmbFishingAreas.setCurrentIndex(0)
        self.ui.cmbLandingSites.setCurrentIndex(0)
        self.ui.cmbBathymetry.setCurrentIndex(0)

    def nextId(self):
        return 50

    def setLayers(self):
        self.mywiz.lyrMngr.setLayers([layers.strEezRclp,layers.strWpiRclp,layers.strCountriesRclp])
        self.zoomFull()

class page5dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page5dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page5()
        self.ui.setupUi(self)

    def nextId(self):
        return 60

    def setLayers(self):
        self.mywiz.lyrMngr.setLayers([layers.strEezRclp,layers.strWpiRclp,layers.strCountriesRclp])
        self.zoomFull()
 
class page6dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page6dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page6()
        self.ui.setupUi(self)
        
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))

    def nextId(self):
        return 70

    def setLayers(self):
        self.mywiz.lyrMngr.setLayers(None)
        self.zoomFull()
        
class page7dialog(myWizardPage):
    def __init__(self,eaf,mywiz):
        super(page7dialog,self).__init__(eaf,mywiz)        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page7()
        self.ui.setupUi(self)
                
    def nextId(self):
        return -1 # for the moment, this is the last page

    def setLayers(self):    
        self.mywiz.lyrMngr.setLayers([layers.strCountries,layers.strEez,layers.strWpi])
        self.zoomFull()
