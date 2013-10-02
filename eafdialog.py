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
#from ui_eaf import Ui_eaf

from eaf_dlg import Ui_Dialog
from wizarddialog import wizarddialog
# create the dialog for zoom to point


class eafdialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        #self.ui = Ui_eaf()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        wiz=wizarddialog()

        layout = QtGui.QVBoxLayout()
        
        layout.addWidget(wiz) 
        #form_widget has its own main_widget where I put all other widgets onto

        self.ui.tabWidget.setLayout(layout)




