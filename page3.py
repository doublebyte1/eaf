# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3.ui'
#
# Created: Wed Nov 13 15:41:06 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page3(object):
    def setupUi(self, Page3):
        Page3.setObjectName(_fromUtf8("Page3"))
        Page3.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page3)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbMethod2 = QtGui.QLabel(Page3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbMethod2.sizePolicy().hasHeightForWidth())
        self.lbMethod2.setSizePolicy(sizePolicy)
        self.lbMethod2.setScaledContents(False)
        self.lbMethod2.setWordWrap(True)
        self.lbMethod2.setObjectName(_fromUtf8("lbMethod2"))
        self.horizontalLayout.addWidget(self.lbMethod2)
        self.cmbMethod2 = QtGui.QComboBox(Page3)
        self.cmbMethod2.setObjectName(_fromUtf8("cmbMethod2"))
        self.cmbMethod2.addItem(_fromUtf8(""))
        self.cmbMethod2.addItem(_fromUtf8(""))
        self.cmbMethod2.addItem(_fromUtf8(""))
        self.cmbMethod2.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbMethod2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbMethod2.setBuddy(self.cmbMethod2)

        self.retranslateUi(Page3)
        QtCore.QMetaObject.connectSlotsByName(Page3)

    def retranslateUi(self, Page3):
        Page3.setWindowTitle(QtGui.QApplication.translate("Page3", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page3.setTitle(QtGui.QApplication.translate("Page3", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page3.setSubTitle(QtGui.QApplication.translate("Page3", "Initial Project Planning", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page3", "Refine the AoI:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbMethod2.setText(QtGui.QApplication.translate("Page3", "&Select a Method", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod2.setItemText(0, QtGui.QApplication.translate("Page3", "Please choose one...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod2.setItemText(1, QtGui.QApplication.translate("Page3", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod2.setItemText(2, QtGui.QApplication.translate("Page3", "From list of countries/regions", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMethod2.setItemText(3, QtGui.QApplication.translate("Page3", "From list of water areas", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
