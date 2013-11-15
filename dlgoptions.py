# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgoptions.ui'
#
# Created: Thu Nov 14 11:10:56 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgOptions(object):
    def setupUi(self, DlgOptions):
        DlgOptions.setObjectName(_fromUtf8("DlgOptions"))
        DlgOptions.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(DlgOptions)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBox = QtGui.QToolBox(DlgOptions)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.fileoptions = QtGui.QWidget()
        self.fileoptions.setGeometry(QtCore.QRect(0, 0, 382, 199))
        self.fileoptions.setObjectName(_fromUtf8("fileoptions"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.fileoptions)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbData = QtGui.QLabel(self.fileoptions)
        self.lbData.setObjectName(_fromUtf8("lbData"))
        self.horizontalLayout.addWidget(self.lbData)
        self.lineData = QtGui.QLineEdit(self.fileoptions)
        self.lineData.setObjectName(_fromUtf8("lineData"))
        self.horizontalLayout.addWidget(self.lineData)
        self.toolData = QtGui.QToolButton(self.fileoptions)
        self.toolData.setObjectName(_fromUtf8("toolData"))
        self.horizontalLayout.addWidget(self.toolData)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.toolBox.addItem(self.fileoptions, _fromUtf8(""))
        self.miscoptions = QtGui.QWidget()
        self.miscoptions.setGeometry(QtCore.QRect(0, 0, 382, 199))
        self.miscoptions.setObjectName(_fromUtf8("miscoptions"))
        self.toolBox.addItem(self.miscoptions, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.buttonBox = QtGui.QDialogButtonBox(DlgOptions)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lbData.setBuddy(self.lineData)

        self.retranslateUi(DlgOptions)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgOptions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgOptions.reject)
        QtCore.QObject.connect(self.toolData, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgOptions.setDataPath)
        QtCore.QMetaObject.connectSlotsByName(DlgOptions)

    def retranslateUi(self, DlgOptions):
        DlgOptions.setWindowTitle(QtGui.QApplication.translate("DlgOptions", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lbData.setToolTip(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.lbData.setStatusTip(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.lbData.setWhatsThis(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.lbData.setText(QtGui.QApplication.translate("DlgOptions", "Data Path", None, QtGui.QApplication.UnicodeUTF8))
        self.lineData.setToolTip(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.lineData.setStatusTip(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.lineData.setWhatsThis(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.toolData.setToolTip(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.toolData.setStatusTip(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.toolData.setWhatsThis(QtGui.QApplication.translate("DlgOptions", "Set the folder for storing generated data", None, QtGui.QApplication.UnicodeUTF8))
        self.toolData.setText(QtGui.QApplication.translate("DlgOptions", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.fileoptions), QtGui.QApplication.translate("DlgOptions", "File Options", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.miscoptions), QtGui.QApplication.translate("DlgOptions", "Misc Options", None, QtGui.QApplication.UnicodeUTF8))

