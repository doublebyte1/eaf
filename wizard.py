# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard.ui'
#
# Created: Wed Oct 16 17:07:28 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(400, 300)
        Wizard.setWizardStyle(QtGui.QWizard.ClassicStyle)
        Wizard.setOptions(QtGui.QWizard.HaveHelpButton|QtGui.QWizard.NoCancelButton)
        Wizard.setTitleFormat(QtCore.Qt.RichText)
        Wizard.setSubTitleFormat(QtCore.Qt.RichText)

        self.retranslateUi(Wizard)
        QtCore.QObject.connect(Wizard, QtCore.SIGNAL(_fromUtf8("helpRequested()")), Wizard.showHelp)
        QtCore.QObject.connect(Wizard, QtCore.SIGNAL(_fromUtf8("finished(int)")), Wizard.houseKeeping)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QtGui.QApplication.translate("Wizard", "Wizard", None, QtGui.QApplication.UnicodeUTF8))

