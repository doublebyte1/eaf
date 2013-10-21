# -*- coding: utf-8 -*-
"""
/***************************************************************************
 eaf
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


import sys, os.path
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
import eafdialog

#sys.path.append('/home/joana/.eclipse/org.eclipse.platform_3.8_155965261/plugins/org.python.pydev_2.8.2.2013090511/pysrc')

#from pydevd import *

## @package eaf
#  This package implements a EAF wizard.  
################################################


basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))


## eaf
#
#  This is the main QGIS Plugin class; 
#
#  It is pretty standard for all plugins; It contains a pointer to the QGIS UI, and it initializes the  plugin dialogue (eafdialog).
################################################
class eaf:

    ## Constructor
    #
    #  This is a constructor
    ##########################################################
    def __init__(self, iface):
        #Debug VERSION: REMOVE THIS FOR RELEASE!!! /////////////7
        #settrace()        
        
        # Save reference to the QGIS interface
        self.iface = iface

        self.qgsVersion = unicode(QGis.QGIS_VERSION_INT)

        # For i18n support
        userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/DiagLeg"
        systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/DiagLeg"

        overrideLocale = QSettings().value("locale/overrideFlag", False)
        if not overrideLocale:
            localeFullName = QLocale.system().name()
        else:
            localeFullName = QSettings().value("locale/userLocale", "")

        if QFileInfo(userPluginPath).exists():
            translationPath = userPluginPath + "/i18n/DiagLeg" + localeFullName + ".qm"
        else:
            translationPath = systemPluginPath + "/i18n/DiagLeg" + localeFullName + ".qm"

        self.localePath = translationPath
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
            QCoreApplication.installTranslator(self.translator)


    ## Initializes GUI
    #
    #  In this function we create an icon in the toobar and an entry on the plugin menu.
    # We also instantiate the eaf dialogue as a dock widget.
    ##############################################################
    def initGui(self):
        self.action = QAction(QIcon(":/plugins/eaf/icon.png"),  "eaf", self.iface.mainWindow())           
        QObject.connect(self.action, SIGNAL("triggered()"), self.showHideDockWidget)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&GISforEAF", self.action)
        self.dockWidget = eafdialog.eafdialog(self)
        

    ## Unload Plugin
    #
    #  It removes the plugin from the toolbar, and from the plugin menu.
    ##############################################################
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&GISforEAF",self.action)
        self.iface.removeToolBarIcon(self.action)

    ## Show/Hide dock widget
    #
    #  This function switches the state of the plugin window (visible or invisible).
    ##############################################################
    def showHideDockWidget(self):
        if self.dockWidget.isVisible():
            self.dockWidget.hide()
        else:
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)            
            self.dockWidget.show()
        