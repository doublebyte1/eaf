# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_eaf.ui'
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

class Ui_eaf(object):
    def setupUi(self, eaf):
        eaf.setObjectName(_fromUtf8("eaf"))
        eaf.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(eaf)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(eaf)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), eaf.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), eaf.reject)
        QtCore.QMetaObject.connectSlotsByName(eaf)

    def retranslateUi(self, eaf):
        eaf.setWindowTitle(QtGui.QApplication.translate("eaf", "eaf", None, QtGui.QApplication.UnicodeUTF8))

