# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard.ui'
#
# Created: Thu Oct 10 11:54:24 2013
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
        Wizard.setWizardStyle(QtGui.QWizard.ClassicStyle)
        Wizard.setOptions(QtGui.QWizard.HaveHelpButton|QtGui.QWizard.NoCancelButton)
        Wizard.setTitleFormat(QtCore.Qt.RichText)
        Wizard.setSubTitleFormat(QtCore.Qt.RichText)
        self.wizardPage0 = page0dialog()
        self.wizardPage0.setObjectName(_fromUtf8("wizardPage0"))
        Wizard.addPage(self.wizardPage0)
        self.wizardPage1 = page1dialog()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = page2dialog()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        Wizard.addPage(self.wizardPage2)
        self.wizardPage3 = page3dialog()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        Wizard.addPage(self.wizardPage3)
        self.wizardPage4 = page4dialog()
        self.wizardPage4.setObjectName(_fromUtf8("wizardPage4"))
        Wizard.addPage(self.wizardPage4)
        self.wizardPage5 = page5dialog()
        self.wizardPage5.setObjectName(_fromUtf8("wizardPage5"))
        Wizard.addPage(self.wizardPage5)
        self.wizardPage6 = page6dialog()
        self.wizardPage6.setObjectName(_fromUtf8("wizardPage6"))
        Wizard.addPage(self.wizardPage6)
        self.wizardPage7 = page7dialog()
        self.wizardPage7.setObjectName(_fromUtf8("wizardPage7"))
        Wizard.addPage(self.wizardPage7)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QtGui.QApplication.translate("Wizard", "Wizard", None, QtGui.QApplication.UnicodeUTF8))

from pages import page4dialog, page1dialog, page5dialog, page2dialog, page7dialog, page0dialog, page3dialog, page6dialog
