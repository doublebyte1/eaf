# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created: Thu Oct 10 11:50:01 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page1(object):
    def setupUi(self, Page1):
        Page1.setObjectName(_fromUtf8("Page1"))
        Page1.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page1)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbMethod = QtGui.QLabel(Page1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbMethod.sizePolicy().hasHeightForWidth())
        self.lbMethod.setSizePolicy(sizePolicy)
        self.lbMethod.setScaledContents(False)
        self.lbMethod.setWordWrap(True)
        self.lbMethod.setObjectName(_fromUtf8("lbMethod"))
        self.horizontalLayout.addWidget(self.lbMethod)
        self.cmbMethod = QtGui.QComboBox(Page1)
        self.cmbMethod.setModelColumn(0)
        self.cmbMethod.setObjectName(_fromUtf8("cmbMethod"))
        self.cmbMethod.addItem(_fromUtf8(""))
        self.cmbMethod.addItem(_fromUtf8(""))
        self.cmbMethod.addItem(_fromUtf8(""))
        self.cmbMethod.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbMethod)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbMethod.setBuddy(self.cmbMethod)

        self.retranslateUi(Page1)
        QtCore.QMetaObject.connectSlotsByName(Page1)

    def retranslateUi(self, Page1):
        Page1.setWindowTitle(QtGui.QApplication.translate("Page1", "Broad Definition of AoI", None, QtGui.QApplication.UnicodeUTF8))
        Page1.setTitle(QtGui.QApplication.translate("Page1", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page1.setSubTitle(QtGui.QApplication.translate("Page1", "Initial Project Planning Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page1", "<html><head/><body><p>Broad Definition of AoI:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbMethod.setText(QtGui.QApplication.translate("Page1", "&Select a Method", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod.setItemText(0, QtGui.QApplication.translate("Page1", "Please Choose one...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod.setItemText(1, QtGui.QApplication.translate("Page1", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod.setItemText(2, QtGui.QApplication.translate("Page1", "From list of countries/regions", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod.setItemText(3, QtGui.QApplication.translate("Page1", "From list of water areas", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
