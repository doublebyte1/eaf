# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page0.ui'
#
# Created: Mon Oct  7 11:44:33 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page0(object):
    def setupUi(self, Page0):
        Page0.setObjectName(_fromUtf8("Page0"))
        Page0.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page0)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Page0)
        QtCore.QMetaObject.connectSlotsByName(Page0)

    def retranslateUi(self, Page0):
        Page0.setWindowTitle(QtGui.QApplication.translate("Page0", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page0.setTitle(QtGui.QApplication.translate("Page0", "Introduction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page0", "<html><head/><body><p>This wizard will guide you through the &quot;Initiation and Planning&quot; Step,</p><p><br/></p><p>Please press &quot;next&quot;, to start adding data.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc