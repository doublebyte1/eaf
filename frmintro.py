# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmintro.ui'
#
# Created: Mon Oct  7 09:23:38 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmIntro(object):
    def setupUi(self, frmIntro):
        frmIntro.setObjectName(_fromUtf8("frmIntro"))
        frmIntro.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(frmIntro)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(frmIntro)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(frmIntro)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/eaf/eaf1.jpg")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(frmIntro)
        QtCore.QMetaObject.connectSlotsByName(frmIntro)

    def retranslateUi(self, frmIntro):
        frmIntro.setWindowTitle(QtGui.QApplication.translate("frmIntro", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmIntro", "<html><head/><body><p>Welcome to the EAF wizard!</p><p>This plugin will guide you through an Ecosystem\'s approach to Fisheries, using GIS.</p><p>Please Press &quot;New Project&quot; to start adding data, or &quot;Open Project&quot; to load a previously saved project.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
