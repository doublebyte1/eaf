# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created: Tue Oct 15 12:02:14 2013
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
        Page2.resize(400, 299)
        self.verticalLayout = QtGui.QVBoxLayout(Page2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page2)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkMaritime = QtGui.QCheckBox(Page2)
        self.checkMaritime.setObjectName(_fromUtf8("checkMaritime"))
        self.horizontalLayout_6.addWidget(self.checkMaritime)
        self.cmbMaritime = QtGui.QComboBox(Page2)
        self.cmbMaritime.setEnabled(False)
        self.cmbMaritime.setObjectName(_fromUtf8("cmbMaritime"))
        self.cmbMaritime.addItem(_fromUtf8(""))
        self.cmbMaritime.addItem(_fromUtf8(""))
        self.cmbMaritime.addItem(_fromUtf8(""))
        self.cmbMaritime.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.cmbMaritime)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkCoastline = QtGui.QCheckBox(Page2)
        self.checkCoastline.setObjectName(_fromUtf8("checkCoastline"))
        self.horizontalLayout_3.addWidget(self.checkCoastline)
        self.cmbCoastline = QtGui.QComboBox(Page2)
        self.cmbCoastline.setEnabled(False)
        self.cmbCoastline.setObjectName(_fromUtf8("cmbCoastline"))
        self.cmbCoastline.addItem(_fromUtf8(""))
        self.cmbCoastline.addItem(_fromUtf8(""))
        self.cmbCoastline.addItem(_fromUtf8(""))
        self.cmbCoastline.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cmbCoastline)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.checkLandingSites = QtGui.QCheckBox(Page2)
        self.checkLandingSites.setObjectName(_fromUtf8("checkLandingSites"))
        self.horizontalLayout_5.addWidget(self.checkLandingSites)
        self.cmbLandingSites = QtGui.QComboBox(Page2)
        self.cmbLandingSites.setEnabled(False)
        self.cmbLandingSites.setObjectName(_fromUtf8("cmbLandingSites"))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.cmbLandingSites.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cmbLandingSites)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.checkOther = QtGui.QCheckBox(Page2)
        self.checkOther.setObjectName(_fromUtf8("checkOther"))
        self.horizontalLayout_7.addWidget(self.checkOther)
        self.cmbOther = QtGui.QComboBox(Page2)
        self.cmbOther.setEnabled(False)
        self.cmbOther.setObjectName(_fromUtf8("cmbOther"))
        self.cmbOther.addItem(_fromUtf8(""))
        self.cmbOther.addItem(_fromUtf8(""))
        self.cmbOther.addItem(_fromUtf8(""))
        self.cmbOther.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cmbOther)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBathymetry = QtGui.QCheckBox(Page2)
        self.checkBathymetry.setObjectName(_fromUtf8("checkBathymetry"))
        self.horizontalLayout_4.addWidget(self.checkBathymetry)
        self.cmbBathymetry = QtGui.QComboBox(Page2)
        self.cmbBathymetry.setEnabled(False)
        self.cmbBathymetry.setObjectName(_fromUtf8("cmbBathymetry"))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.cmbBathymetry.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.cmbBathymetry)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Page2)
        QtCore.QObject.connect(self.checkBathymetry, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cmbBathymetry.setEnabled)
        QtCore.QObject.connect(self.checkCoastline, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cmbCoastline.setEnabled)
        QtCore.QObject.connect(self.checkLandingSites, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cmbLandingSites.setEnabled)
        QtCore.QObject.connect(self.checkMaritime, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cmbMaritime.setEnabled)
        QtCore.QObject.connect(self.checkOther, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cmbOther.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Page2)

    def retranslateUi(self, Page2):
        Page2.setWindowTitle(QtGui.QApplication.translate("Page2", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page2.setTitle(QtGui.QApplication.translate("Page2", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page2.setSubTitle(QtGui.QApplication.translate("Page2", "Stakeholder Analysis and Engagement Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page2", "Compilation of Base Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkMaritime.setText(QtGui.QApplication.translate("Page2", "Maritime Boundaries", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaritime.setItemText(0, QtGui.QApplication.translate("Page2", "Please choose one...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaritime.setItemText(1, QtGui.QApplication.translate("Page2", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaritime.setItemText(2, QtGui.QApplication.translate("Page2", "Digitize", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaritime.setItemText(3, QtGui.QApplication.translate("Page2", "Get from plugin/web repositories", None, QtGui.QApplication.UnicodeUTF8))
        self.checkCoastline.setText(QtGui.QApplication.translate("Page2", "Coastline", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCoastline.setItemText(0, QtGui.QApplication.translate("Page2", "Please choose one...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCoastline.setItemText(1, QtGui.QApplication.translate("Page2", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCoastline.setItemText(2, QtGui.QApplication.translate("Page2", "Digitize", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCoastline.setItemText(3, QtGui.QApplication.translate("Page2", "Get from plugin/web repositories", None, QtGui.QApplication.UnicodeUTF8))
        self.checkLandingSites.setText(QtGui.QApplication.translate("Page2", "Landing Sites", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(0, QtGui.QApplication.translate("Page2", "Please choose one...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(1, QtGui.QApplication.translate("Page2", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(2, QtGui.QApplication.translate("Page2", "Digitize", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbLandingSites.setItemText(3, QtGui.QApplication.translate("Page2", "Get from plugin/web repositories", None, QtGui.QApplication.UnicodeUTF8))
        self.checkOther.setText(QtGui.QApplication.translate("Page2", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOther.setItemText(0, QtGui.QApplication.translate("Page2", "Please choose one...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOther.setItemText(1, QtGui.QApplication.translate("Page2", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOther.setItemText(2, QtGui.QApplication.translate("Page2", "Digitize", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOther.setItemText(3, QtGui.QApplication.translate("Page2", "Get from plugin/web repositories", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBathymetry.setText(QtGui.QApplication.translate("Page2", "Bathymetry", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(0, QtGui.QApplication.translate("Page2", "Please choose one...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(1, QtGui.QApplication.translate("Page2", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(2, QtGui.QApplication.translate("Page2", "Digitize", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBathymetry.setItemText(3, QtGui.QApplication.translate("Page2", "Get from plugin/web repositories", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
