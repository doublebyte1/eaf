# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock.ui'
#
# Created: Thu Oct  3 17:41:00 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(779, 346)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushOpen = QtGui.QPushButton(self.dockWidgetContents)
        self.pushOpen.setObjectName(_fromUtf8("pushOpen"))
        self.horizontalLayout.addWidget(self.pushOpen)
        self.pushSave = QtGui.QPushButton(self.dockWidgetContents)
        self.pushSave.setObjectName(_fromUtf8("pushSave"))
        self.horizontalLayout.addWidget(self.pushSave)
        self.pushClose = QtGui.QPushButton(self.dockWidgetContents)
        self.pushClose.setObjectName(_fromUtf8("pushClose"))
        self.horizontalLayout.addWidget(self.pushClose)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushDoc = QtGui.QPushButton(self.dockWidgetContents)
        self.pushDoc.setObjectName(_fromUtf8("pushDoc"))
        self.horizontalLayout.addWidget(self.pushDoc)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbOptions = QtGui.QLabel(self.dockWidgetContents)
        self.lbOptions.setObjectName(_fromUtf8("lbOptions"))
        self.horizontalLayout.addWidget(self.lbOptions)
        self.toolOptions = QtGui.QToolButton(self.dockWidgetContents)
        self.toolOptions.setObjectName(_fromUtf8("toolOptions"))
        self.horizontalLayout.addWidget(self.toolOptions)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtGui.QProgressBar(self.dockWidgetContents)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        DockWidget.setWidget(self.dockWidgetContents)
        self.lbOptions.setBuddy(self.toolOptions)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtGui.QApplication.translate("DockWidget", "EAF Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOpen.setText(QtGui.QApplication.translate("DockWidget", "&Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSave.setText(QtGui.QApplication.translate("DockWidget", "&Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushClose.setText(QtGui.QApplication.translate("DockWidget", "&Close Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushDoc.setText(QtGui.QApplication.translate("DockWidget", "&EAF Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.lbOptions.setText(QtGui.QApplication.translate("DockWidget", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.toolOptions.setText(QtGui.QApplication.translate("DockWidget", "...", None, QtGui.QApplication.UnicodeUTF8))

