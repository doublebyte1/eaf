# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard.ui'
#
# Created: Wed Oct  2 15:40:15 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(400, 300)
        #Wizard.setWizardStyle(QtGui.QWizard.ClassicStyle)
#        self.wizardPage1 = Page1()
#        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        #Wizard.addPage(self.wizardPage1)
#        self.wizardPage2 = Page2()
#        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        #Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QtGui.QApplication.translate("Wizard", "Wizard", None, QtGui.QApplication.UnicodeUTF8))

#from page2 import Page2
#from page1 import Page1
