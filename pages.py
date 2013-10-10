import sys, os.path

from PyQt4 import QtCore, QtGui

from page0 import Ui_Page0
from page1 import Ui_Page1
from page2 import Ui_Page2
from page3 import Ui_Page3
from page4 import Ui_Page4
from page5 import Ui_Page5
from page6 import Ui_Page6
from page7 import Ui_Page7

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
