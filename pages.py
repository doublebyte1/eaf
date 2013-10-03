from PyQt4 import QtCore, QtGui

from page1 import Ui_Page1
from page2 import Ui_Page2


class page1dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page1()
        self.ui.setupUi(self)
        
        #self.ui.lbName.setText(self.title())
        
class page2dialog(QtGui.QWizardPage):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Page2()
        self.ui.setupUi(self)   