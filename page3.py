# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3.ui'
#
# Created: Mon Oct  7 11:54:21 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page3(object):
    def setupUi(self, Page3):
        Page3.setObjectName(_fromUtf8("Page3"))
        Page3.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Page3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page3)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Page3)
        QtCore.QMetaObject.connectSlotsByName(Page3)

    def retranslateUi(self, Page3):
        Page3.setWindowTitle(QtGui.QApplication.translate("Page3", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        Page3.setTitle(QtGui.QApplication.translate("Page3", "Conclusion", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Page3", "<html><head/><body><p>Congratulations: This step is complete!</p><p><br/></p><p>Please press &quot;finished&quot; to proceed to the next step.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

