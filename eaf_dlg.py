# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eaf_dlg.ui'
#
# Created: Thu Oct  3 13:18:00 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(659, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/eaf/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushOpen = QtGui.QPushButton(Dialog)
        self.pushOpen.setObjectName(_fromUtf8("pushOpen"))
        self.horizontalLayout.addWidget(self.pushOpen)
        self.pushSave = QtGui.QPushButton(Dialog)
        self.pushSave.setObjectName(_fromUtf8("pushSave"))
        self.horizontalLayout.addWidget(self.pushSave)
        self.pushClose = QtGui.QPushButton(Dialog)
        self.pushClose.setObjectName(_fromUtf8("pushClose"))
        self.horizontalLayout.addWidget(self.pushClose)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushDoc = QtGui.QPushButton(Dialog)
        self.pushDoc.setObjectName(_fromUtf8("pushDoc"))
        self.horizontalLayout.addWidget(self.pushDoc)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbOptions = QtGui.QLabel(Dialog)
        self.lbOptions.setObjectName(_fromUtf8("lbOptions"))
        self.horizontalLayout.addWidget(self.lbOptions)
        self.toolOptions = QtGui.QToolButton(Dialog)
        self.toolOptions.setObjectName(_fromUtf8("toolOptions"))
        self.horizontalLayout.addWidget(self.toolOptions)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.lbOptions.setBuddy(self.toolOptions)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOpen.setText(QtGui.QApplication.translate("Dialog", "&Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSave.setText(QtGui.QApplication.translate("Dialog", "&Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushClose.setText(QtGui.QApplication.translate("Dialog", "&Close Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushDoc.setText(QtGui.QApplication.translate("Dialog", "&EAF Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.lbOptions.setText(QtGui.QApplication.translate("Dialog", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.toolOptions.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
