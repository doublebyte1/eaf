from PyQt4 import QtCore, QtGui

from page0 import Ui_Page0
from page1 import Ui_Page1
from page2 import Ui_Page2
from page3 import Ui_Page3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
 