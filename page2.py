# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created: Thu Oct  3 14:45:11 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page2(object):
    def setupUi(self, Page2):
        Page2.setObjectName(_fromUtf8("Page2"))
        Page2.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Page2)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkLandingSites = QtGui.QCheckBox(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkLandingSites.sizePolicy().hasHeightForWidth())
        self.checkLandingSites.setSizePolicy(sizePolicy)
        self.checkLandingSites.setObjectName(_fromUtf8("checkLandingSites"))
        self.horizontalLayout.addWidget(self.checkLandingSites)
        self.cmbLandingSites = QtGui.QComboBox(self.tab1)
        self.cmbLandingSites.setEnabled(False)
        self.cmbLandingSites.setObjectName(_fromUtf8("cmbLandingSites"))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbLandingSites)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBathymetry = QtGui.QCheckBox(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBathymetry.sizePolicy().hasHeightForWidth())
        self.checkBathymetry.setSizePolicy(sizePolicy)
        self.checkBathymetry.setObjectName(_fromUtf8("checkBathymetry"))
        self.horizontalLayout_2.addWidget(self.checkBathymetry)
        self.cmbBathymetry = QtGui.QComboBox(self.tab1)
        self.cmbBathymetry.setEnabled(False)
        self.cmbBathymetry.setObjectName(_fromUtf8("cmbBathymetry"))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbBathymetry)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkFishingAreas = QtGui.QCheckBox(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkFishingAreas.sizePolicy().hasHeightForWidth())
        self.checkFishingAreas.setSizePolicy(sizePolicy)
        self.checkFishingAreas.setObjectName(_fromUtf8("checkFishingAreas"))
        self.horizontalLayout_3.addWidget(self.checkFishingAreas)
        self.cmbFishingAreas = QtGui.QComboBox(self.tab1)
        self.cmbFishingAreas.setEnabled(False)
        self.cmbFishingAreas.setObjectName(_fromUtf8("cmbFishingAreas"))
        self.cmbFishingAreas.addItem(_fromUtf8(""))
        self.cmbFishingAreas.addItem(_fromUtf8(""))
        self.cmbFishingAreas.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cmbFishingAreas)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Page2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.checkLandingSites, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cmbLandingSites.setEnabled)
        QtCore.QObject.connect(self.checkBathymetry, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cmbBathymetry.setEnabled)
        QtCore.QObject.connect(self.checkFishingAreas, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cmbFishingAreas.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Page2)

    def retranslateUi(self, Page2):
        Page2.setWindowTitle(QtGui.QApplication.translate("Page2", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page2.setTitle(QtGui.QApplication.translate("Page2", "Stakeholder Analysis and Engagement Step", None, QtGui.QApplication.UnicodeUTF8))
        self.checkLandingSites.setText(QtGui.QApplication.translate("Page2", "Landing Sites", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(0, QtGui.QApplication.translate("Page2", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(1, QtGui.QApplication.translate("Page2", "By grid-cell", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(2, QtGui.QApplication.translate("Page2", "Rule-based", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBathymetry.setText(QtGui.QApplication.translate("Page2", "Bathymetry", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(0, QtGui.QApplication.translate("Page2", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(1, QtGui.QApplication.translate("Page2", "By grid-cell", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(2, QtGui.QApplication.translate("Page2", "Rule-based", None, QtGui.QApplication.UnicodeUTF8))
        self.checkFishingAreas.setText(QtGui.QApplication.translate("Page2", "Fishing Areas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbFishingAreas.setItemText(0, QtGui.QApplication.translate("Page2", "Free-hand interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbFishingAreas.setItemText(1, QtGui.QApplication.translate("Page2", "By grid-cell", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbFishingAreas.setItemText(2, QtGui.QApplication.translate("Page2", "Rule-based", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtGui.QApplication.translate("Page2", "Participatory GIS Approach", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QtGui.QApplication.translate("Page2", "Expert Based Approach", None, QtGui.QApplication.UnicodeUTF8))

