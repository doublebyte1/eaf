# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page6.ui'
#
# Created: Wed Nov 13 15:41:07 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page6(object):
    def setupUi(self, Page6):
        Page6.setObjectName(_fromUtf8("Page6"))
        Page6.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page6)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Page6)
        QtCore.QMetaObject.connectSlotsByName(Page6)

    def retranslateUi(self, Page6):
        Page6.setWindowTitle(QtGui.QApplication.translate("Page6", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page6.setTitle(QtGui.QApplication.translate("Page6", "Initiation and Planning", None, QtGui.QApplication.UnicodeUTF8))
        Page6.setSubTitle(QtGui.QApplication.translate("Page6", "Conclusion", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page6", "<html><head/><body><p>Congratulations: This step is complete!</p><p><br/></p><p>Please continue to proceed to the next step: &quot;Definition of Scope&quot;</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

