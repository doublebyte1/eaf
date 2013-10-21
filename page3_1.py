# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3_1.ui'
#
# Created: Fri Oct 18 09:40:05 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page3_1(object):
    def setupUi(self, Page3_1):
        Page3_1.setObjectName(_fromUtf8("Page3_1"))
        Page3_1.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page3_1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Page3_1)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(Page3_1)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Page3_1)
        QtCore.QMetaObject.connectSlotsByName(Page3_1)

    def retranslateUi(self, Page3_1):
        Page3_1.setWindowTitle(QtGui.QApplication.translate("Page3_1", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page3_1.setTitle(QtGui.QApplication.translate("Page3_1", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page3_1.setSubTitle(QtGui.QApplication.translate("Page3_1", "Initial Project Planning", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Page3_1", "<html><head/><body><p>Refine the definition of AoI using  free-hand interactive:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page3_1", "<html><head/><body><p>Please zoom in into your area of interest; press next when you are done.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

