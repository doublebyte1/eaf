# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page4.ui'
#
# Created: Thu Oct 10 11:50:02 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page4(object):
    def setupUi(self, Page4):
        Page4.setObjectName(_fromUtf8("Page4"))
        Page4.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page4)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBathymetry = QtGui.QCheckBox(Page4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBathymetry.sizePolicy().hasHeightForWidth())
        self.checkBathymetry.setSizePolicy(sizePolicy)
        self.checkBathymetry.setObjectName(_fromUtf8("checkBathymetry"))
        self.horizontalLayout_2.addWidget(self.checkBathymetry)
        self.cmbBathymetry = QtGui.QComboBox(Page4)
        self.cmbBathymetry.setEnabled(False)
        self.cmbBathymetry.setObjectName(_fromUtf8("cmbBathymetry"))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbBathymetry)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkLandingSites = QtGui.QCheckBox(Page4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkLandingSites.sizePolicy().hasHeightForWidth())
        self.checkLandingSites.setSizePolicy(sizePolicy)
        self.checkLandingSites.setObjectName(_fromUtf8("checkLandingSites"))
        self.horizontalLayout.addWidget(self.checkLandingSites)
        self.cmbLandingSites = QtGui.QComboBox(Page4)
        self.cmbLandingSites.setEnabled(False)
        self.cmbLandingSites.setObjectName(_fromUtf8("cmbLandingSites"))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbLandingSites)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkFishingAreas = QtGui.QCheckBox(Page4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkFishingAreas.sizePolicy().hasHeightForWidth())
        self.checkFishingAreas.setSizePolicy(sizePolicy)
        self.checkFishingAreas.setObjectName(_fromUtf8("checkFishingAreas"))
        self.horizontalLayout_3.addWidget(self.checkFishingAreas)
        self.cmbFishingAreas = QtGui.QComboBox(Page4)
        self.cmbFishingAreas.setEnabled(False)
        self.cmbFishingAreas.setObjectName(_fromUtf8("cmbFishingAreas"))
        self.cmbFishingAreas.addItem(_fromUtf8(""))
        self.cmbFishingAreas.addItem(_fromUtf8(""))
        self.cmbFishingAreas.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cmbFishingAreas)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Page4)
        QtCore.QMetaObject.connectSlotsByName(Page4)

    def retranslateUi(self, Page4):
        Page4.setWindowTitle(QtGui.QApplication.translate("Page4", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page4.setTitle(QtGui.QApplication.translate("Page4", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page4.setSubTitle(QtGui.QApplication.translate("Page4", "Stakeholder Analysis and Engagement Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page4", "PPGIS Approach:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBathymetry.setText(QtGui.QApplication.translate("Page4", "Bathymetry", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(0, QtGui.QApplication.translate("Page4", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(1, QtGui.QApplication.translate("Page4", "By grid-cell", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(2, QtGui.QApplication.translate("Page4", "Rule-based", None, QtGui.QApplication.UnicodeUTF8))
        self.checkLandingSites.setText(QtGui.QApplication.translate("Page4", "Landing Sites", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(0, QtGui.QApplication.translate("Page4", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(1, QtGui.QApplication.translate("Page4", "By grid-cell", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(2, QtGui.QApplication.translate("Page4", "Rule-based", None, QtGui.QApplication.UnicodeUTF8))
        self.checkFishingAreas.setText(QtGui.QApplication.translate("Page4", "Fishing Areas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbFishingAreas.setItemText(0, QtGui.QApplication.translate("Page4", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbFishingAreas.setItemText(1, QtGui.QApplication.translate("Page4", "By grid-cell", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbFishingAreas.setItemText(2, QtGui.QApplication.translate("Page4", "Rule-based", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
