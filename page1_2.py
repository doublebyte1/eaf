# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1_2.ui'
#
# Created: Fri Oct 18 09:40:04 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page1_2(object):
    def setupUi(self, Page1_2):
        Page1_2.setObjectName(_fromUtf8("Page1_2"))
        Page1_2.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page1_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Page1_2)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Page1_2)
        QtCore.QMetaObject.connectSlotsByName(Page1_2)

    def retranslateUi(self, Page1_2):
        Page1_2.setWindowTitle(QtGui.QApplication.translate("Page1_2", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page1_2.setTitle(QtGui.QApplication.translate("Page1_2", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page1_2.setSubTitle(QtGui.QApplication.translate("Page1_2", "Initial Project Planning", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Page1_2", "<html><head/><body><p>Broad Definition of AoI using list of countries/regions:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

