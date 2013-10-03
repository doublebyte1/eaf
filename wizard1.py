# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard1.ui'
#
# Created: Thu Oct  3 13:18:01 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Wizard1(object):
    def setupUi(self, Wizard1):
        Wizard1.setObjectName(_fromUtf8("Wizard1"))
        Wizard1.resize(400, 300)
        Wizard1.setWizardStyle(QtGui.QWizard.ClassicStyle)
        self.wizardPage1 = page1dialog()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        Wizard1.addPage(self.wizardPage1)
        self.wizardPage2 = page2dialog()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        Wizard1.addPage(self.wizardPage2)

        self.retranslateUi(Wizard1)
        QtCore.QMetaObject.connectSlotsByName(Wizard1)

    def retranslateUi(self, Wizard1):
        Wizard1.setWindowTitle(QtGui.QApplication.translate("Wizard1", "Wizard", None, QtGui.QApplication.UnicodeUTF8))

from pages import page1dialog, page2dialog
