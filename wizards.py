# -*- coding: utf-8 -*-
"""
/***************************************************************************
 eafDialog
                                 A QGIS plugin
 Wizard that guides the users through the process of implementing the GIS functionality, within an EAF approach
                             -------------------
        begin                : 2013-10-02
        copyright            : (C) 2013 by FAO
        email                : joana.simoes@fao.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from wizard1 import Ui_Wizard1

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class wizard1(QtGui.QWizard):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Wizard1()
        self.ui.setupUi(self)
        
    def reset(self):
        self.ui.wizardPage1.ui.checkComplete.setChecked(False)
        self.ui.wizardPage2.ui.checkComplete.setChecked(False)       