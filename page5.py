# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page5.ui'
#
# Created: Fri Oct 11 10:26:10 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page5(object):
    def setupUi(self, Page5):
        Page5.setObjectName(_fromUtf8("Page5"))
        Page5.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page5)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Page5)
        QtCore.QMetaObject.connectSlotsByName(Page5)

    def retranslateUi(self, Page5):
        Page5.setWindowTitle(QtGui.QApplication.translate("Page5", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page5", "Expert-based Approach:", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
