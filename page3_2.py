# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3_2.ui'
#
# Created: Wed Nov 13 15:41:07 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page3_2(object):
    def setupUi(self, Page3_2):
        Page3_2.setObjectName(_fromUtf8("Page3_2"))
        Page3_2.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page3_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Page3_2)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.listCountries = QtGui.QListView(Page3_2)
        self.listCountries.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listCountries.setAlternatingRowColors(True)
        self.listCountries.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listCountries.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listCountries.setWordWrap(True)
        self.listCountries.setSelectionRectVisible(False)
        self.listCountries.setObjectName(_fromUtf8("listCountries"))
        self.verticalLayout.addWidget(self.listCountries)

        self.retranslateUi(Page3_2)
        QtCore.QMetaObject.connectSlotsByName(Page3_2)

    def retranslateUi(self, Page3_2):
        Page3_2.setWindowTitle(QtGui.QApplication.translate("Page3_2", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page3_2.setTitle(QtGui.QApplication.translate("Page3_2", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page3_2.setSubTitle(QtGui.QApplication.translate("Page3_2", "Initial Project Planning", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Page3_2", "<html><head/><body><p>Refine the definition of AoI using list of countries/regions:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

