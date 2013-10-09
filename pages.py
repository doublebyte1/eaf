import sys, os.path

from PyQt4 import QtCore, QtGui

from page0 import Ui_Page0
from page1 import Ui_Page1
from page2 import Ui_Page2
from page3 import Ui_Page3

from qgis.core import *
from qgis.gui import *

import eaf

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))

class page0dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page0()
        self.ui.setupUi(self)
        
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))
        

class page1dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.checkComplete, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.isComplete)
        QtCore.QObject.connect(self.ui.checkComplete, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.completeChanged)
        
    def isComplete(self):
        return self.ui.checkComplete.isChecked()
    
    def triggerMethod(self,index):
        if index==1:
            
            vl = QgsVectorLayer("Polygon?crs=epsg:4326",
                                 "selection_polygon", "memory")                        
            if not vl.isValid():
                print "Layer failed to create!"     
                
            #pr = vl.dataProvider()
            #ret = pr.addAttributes( [ QgsField("id", QtCore.QVariant.String) ] )                
                            
            QtCore.QObject.connect(vl, QtCore.SIGNAL(_fromUtf8("featureAdded(QgsFeatureId)")), self.proceed)
                                                         
            QgsMapLayerRegistry.instance().addMapLayer(vl)    
            
            #vl.beginEditCommand("Feature triangulation")

            vl.startEditing() 

            self.vl=vl
            
    def proceed(self):
            self.vl.blockSignals(True)
                    
            if not self.vl.isValid():
                print "Layer failed to create!"     


            #self.vl.endEditCommand()        
            b=self.vl.commitChanges()
            if not b:
                print "no changes"

            #self.vl.updateExtents()
            
            self.vl.blockSignals(False)
            
                    
class page2dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page2()
        self.ui.setupUi(self)
                
        QtCore.QObject.connect(self.ui.checkComplete, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.isComplete)
        QtCore.QObject.connect(self.ui.checkComplete, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.completeChanged)
        
    def isComplete(self):
        return self.ui.checkComplete.isChecked()

class page3dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page3()
        self.ui.setupUi(self)
        
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(":/plugins/eaf/eaf3.jpg"))
 