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
from page4 import Ui_Page4
from page5 import Ui_Page5
from page6 import Ui_Page6
from page7 import Ui_Page7

from qgis.core import *
from qgis.gui import *

import processing


import eaf

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))

strEez=QtCore.QCoreApplication.translate("page0dialog","200 Nautical Miles Arc Limits") 
strWpi=QtCore.QCoreApplication.translate("page0dialog","World Port Index")
strCountries=QtCore.QCoreApplication.translate("page0dialog","Global Administrative Units Layer")

strEezClp=QtCore.QCoreApplication.translate("page0dialog","clipped " + strEez) 
strWpiClp=QtCore.QCoreApplication.translate("page0dialog","clipped " + strWpi)
strCountriesClp=QtCore.QCoreApplication.translate("page0dialog","clipped " + strCountries)

class myWizardPage(QtGui.QWizardPage):
    
    def readPageUI(self,strUI):
        #Please reimplement this in the relevant derived classes
        return None 

    def getPageUI(self):
        #Please reimplement this in the relevant derived classes        
        return None 
    
    def resetUI(self):
        print "reset UI"
        
class page0dialog(myWizardPage):
        
    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page0()
        self.ui.setupUi(self)
        self.eaf=eaf
                
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))
                
    def showEvent(self, event):
        self.LoadBaseData(self.eaf)
                        
    def LoadBaseData(self,eaf):          

        if len(QgsMapLayerRegistry.instance().mapLayersByName(strCountries)) ==0:                  
        
            vCountries = QgsVectorLayer(os.path.join(datapath, "g0000_0.shp"), strCountries, "ogr")
            
            if not vCountries.isValid():
                print "Layer failed to load!"
                
            QgsMapLayerRegistry.instance().addMapLayer(vCountries)        
            self.vCountries=vCountries
                  
        if len(QgsMapLayerRegistry.instance().mapLayersByName(strEez)) ==0:                  
        
            vEez = QgsVectorLayer(os.path.join(datapath, "World_EEZ_LR_v7_2012.shp"), strEez, "ogr")
            
            if not vEez.isValid():
                print "Layer failed to load!"

            QgsMapLayerRegistry.instance().addMapLayer(vEez)
            self.vEez=vEez
                        
        if len(QgsMapLayerRegistry.instance().mapLayersByName(strWpi)) ==0:                  
            vWpi = QgsVectorLayer(os.path.join(datapath, "WPI.shp"), strWpi, "ogr")
            
            if not vWpi.isValid():
                print "Layer failed to load!"
                
            QgsMapLayerRegistry.instance().addMapLayer(vWpi)
            self.vWpi=vWpi
                                  
        self.canvas = self.eaf.iface.mapCanvas()  
        
class page1dialog(myWizardPage):
    def __init__(self):
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
            return 1#current page

    def readPageUI(self,strUI):
        self.ui.cmbMethod.setCurrentIndex(strUI["cmbMethod"])
        
    def getPageUI(self):
        myUI={'cmbMethod': self.ui.cmbMethod.currentIndex()}
        return myUI
    
    def resetUI(self):
        self.ui.cmbMethod.setCurrentIndex(0)
                                                                                           
class page1_1dialog(myWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_1()
        self.ui.setupUi(self)
        
    def nextId(self):
        return 2

    def initializePage(self):
        self.startInteraction()
        
    def validatePage(self):        
        return self.stopInteraction(True)
                        
    def cleanupPage(self):               
        self.stopInteraction(False)
                
    def startInteraction(self):
        
        vl = QgsVectorLayer("Polygon?crs=epsg:4326",
                     "selection_polygon", "memory")                        
        if not vl.isValid():
            print "Layer failed to create!"     
                                                     
        QgsMapLayerRegistry.instance().addMapLayer(vl)    
                
        vl.startEditing() 
        
        self.vl=vl        
    
    def stopInteraction(self,save):
        ok=True
                                 
        if not self.vl.isValid():
            print "Layer failed to create!"     

        else:
            self.vl.endEditCommand()     
            if save:
                self.layerData = self.vl.dataProvider() 
                self.layerData.addAttributes([ QgsField("ID", QtCore.QVariant.String)])               
                ok=self.vl.commitChanges() and self.clipLayers()
            else:
                ok=self.vl.rollBack()
                QgsMapLayerRegistry.instance().removeMapLayer(self.vl.id())                
            
            if not ok:
                print "oops! something went wrong!"
            
        return ok    
    
    def clipLayers(self):
        
        processing.runalg("qgis:clip",strEez,"selection_polygon",os.path.join(datapath, "clipped_eez.shp"))
        processing.runalg("qgis:clip",strCountries,"selection_polygon",os.path.join(datapath, "clipped_countries.shp"))
        processing.runalg("qgis:clip",strWpi,"selection_polygon",os.path.join(datapath, "clipped_ports.shp"))
        
        clip_eez = QgsVectorLayer(os.path.join(datapath, "clipped_eez.shp"), strEezClp, "ogr")
        clip_cnt = QgsVectorLayer(os.path.join(datapath, "clipped_countries.shp"), strCountriesClp, "ogr")
        clip_prt = QgsVectorLayer(os.path.join(datapath, "clipped_ports.shp"), "clipped " + strWpi, "ogr")
        
        QgsMapLayerRegistry.instance().addMapLayer(clip_eez)
        QgsMapLayerRegistry.instance().addMapLayer(clip_cnt)
        QgsMapLayerRegistry.instance().addMapLayer(clip_prt)
        
        self.clip_eez=clip_eez
        self.clip_cnt=clip_cnt
        self.clip_prt=clip_prt
        
        return True
        
            
class page1_2dialog(myWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_2()
        self.ui.setupUi(self)

    def nextId(self):
        return 2

class page1_3dialog(myWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_3()
        self.ui.setupUi(self)
                    
class page2dialog(myWizardPage):
    def __init__(self):
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
                                                                        
class page3dialog(myWizardPage):
    def __init__(self):
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
         
class page4dialog(myWizardPage):
    def __init__(self):
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

class page5dialog(myWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page5()
        self.ui.setupUi(self)
 
class page6dialog(myWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page6()
        self.ui.setupUi(self)

        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))
        
class page7dialog(myWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page7()
        self.ui.setupUi(self)
