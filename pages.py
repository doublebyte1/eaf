import sys, os.path

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

#from processing.core.Processing import Processing
#from processing.core.ProcessingConfig import Setting, ProcessingConfig

import processing


import eaf

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))


class page0dialog(QtGui.QWizardPage):
    def __init__(self,eaf):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page0()
        self.ui.setupUi(self)
        self.eaf=eaf
                
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))
                
    def showEvent(self, event):
        self.LoadBaseData(self.eaf)
                        
    def LoadBaseData(self,eaf):          

        if len(QgsMapLayerRegistry.instance().mapLayersByName("World Countries")) ==0:                  
        
            world = QgsVectorLayer(os.path.join(datapath, "g0000_0.shp"), "World Countries", "ogr")
            
            if not world.isValid():
                print "Layer failed to load!"
                
            QgsMapLayerRegistry.instance().addMapLayer(world)        
            self.world=world
                  
        if len(QgsMapLayerRegistry.instance().mapLayersByName("EEZ")) ==0:                  
        
            eez = QgsVectorLayer(os.path.join(datapath, "World_EEZ_LR_v7_2012.shp"), "EEZ", "ogr")
            
            if not eez.isValid():
                print "Layer failed to load!"

            QgsMapLayerRegistry.instance().addMapLayer(eez)
            self.eez=eez
                        
        if len(QgsMapLayerRegistry.instance().mapLayersByName("World Ports")) ==0:                  
            wpi = QgsVectorLayer(os.path.join(datapath, "WPI.shp"), "World Ports", "ogr")
            
            if not wpi.isValid():
                print "Layer failed to load!"
                
            QgsMapLayerRegistry.instance().addMapLayer(wpi)
            self.wpi=wpi
                                  
        self.canvas = self.eaf.iface.mapCanvas()  
        

class page1dialog(QtGui.QWizardPage):
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
                                                                                           
class page1_1dialog(QtGui.QWizardPage):
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
        
        processing.runalg("qgis:clip","EEZ","selection_polygon",os.path.join(datapath, "clipped_eez.shp"))
        processing.runalg("qgis:clip","World Countries","selection_polygon",os.path.join(datapath, "clipped_countries.shp"))
        processing.runalg("qgis:clip","World Ports","selection_polygon",os.path.join(datapath, "clipped_ports.shp"))
        
        clip_eez = QgsVectorLayer(os.path.join(datapath, "clipped_eez.shp"), "clipped eez", "ogr")
        clip_cnt = QgsVectorLayer(os.path.join(datapath, "clipped_countries.shp"), "clipped countries", "ogr")
        clip_prt = QgsVectorLayer(os.path.join(datapath, "clipped_ports.shp"), "clipped ports", "ogr")
        
        QgsMapLayerRegistry.instance().addMapLayer(clip_eez)
        QgsMapLayerRegistry.instance().addMapLayer(clip_cnt)
        QgsMapLayerRegistry.instance().addMapLayer(clip_prt)
        
        self.clip_eez=clip_eez
        self.clip_cnt=clip_cnt
        self.clip_prt=clip_prt
        
        return True
        
            
class page1_2dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_2()
        self.ui.setupUi(self)

    def nextId(self):
        return 2

class page1_3dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1_3()
        self.ui.setupUi(self)
                    
class page2dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page2()
        self.ui.setupUi(self)
                
class page3dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page3()
        self.ui.setupUi(self)
         
class page4dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page4()
        self.ui.setupUi(self)

class page5dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page5()
        self.ui.setupUi(self)
 
class page6dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page6()
        self.ui.setupUi(self)

        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))
        
class page7dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page7()
        self.ui.setupUi(self)
