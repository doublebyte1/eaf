# -*- coding: utf-8 -*-
"""
/***************************************************************************
                 Class Layers
                              -------------------
        begin                : 2013-10-02
        copyright            : (C) 2013 by FAO
        email                : joana.simoes@fao.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This class implements a layer manager for the app;                    *
 *   For each page, we need to know which layers should be on              *
  *                                                                        *
 ***************************************************************************/
"""

import sys, os.path
import json

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QAbstractListModel
 
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

strEez=QtCore.QCoreApplication.translate("LyrMngr","200 Nautical Miles Arc Limits") 
strWpi=QtCore.QCoreApplication.translate("LyrMngr","World Port Index (zoom in to display)")
strCountries=QtCore.QCoreApplication.translate("LyrMngr","Global Administrative Units Layer")

strSelection=QtCore.QCoreApplication.translate("LyrMngr","selection_polygon")

strEezClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strEez) 
strWpiClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strWpi)
strCountriesClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strCountries)

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))

class aLayer:    
    def __init__(self,filename,name,style):
        self.name=name
        self.filename=filename
        self.style=style

class LyrMngr:

    def __init__(self):
        self.initLayers()                


    def initVLayer(self,filename,name):
        return QgsVectorLayer(os.path.join(datapath, filename), name, "ogr")

    def initLayers(self):

        layerList=dict()
        
        layerList[strCountries]=aLayer("g0000_0.shp",strCountries,"g0000_0.qml")
        layerList[strEez]=aLayer("World_EEZ_LR_v7_2012.shp",strEez,"World_EEZ_LR_v7_2012.qml")
        layerList[strWpi]=aLayer("WPI.shp",strWpi,"WPI.qml")
                
        layerList[strSelection]=aLayer( None, strSelection,None) #memory layer
        
        layerList[strEezClp]=aLayer( "clipped_eez.shp", strEezClp,"World_EEZ_LR_v7_2012.qml")
        layerList[strCountriesClp]=aLayer( "clipped_countries.shp",  strCountriesClp ,"g0000_0.qml")
        layerList[strWpiClp]=aLayer("clipped_ports.shp",  strWpiClp, "WPI.qml")
        
        self.layerList=layerList
                                      
    def removeAll(self):
        #removes our layers
        for x in self.layerList.keys():
            self.removeLayer(self.layerList[x])
  

    def setLayers(self,someLayers):
        if someLayers==None:
            self.removeAll()
        else:           
            found=False             
            for x in self.layerList.keys():
                for y in someLayers:
                    if x==y:
                        found=True
                        
                if found:                        
                    self.loadLayer(self.layerList[x])
                else:
                    self.removeLayer(self.layerList[x])
                    
                found=False
        
    def loadLayer(self,aLayer):
        if len(QgsMapLayerRegistry.instance().mapLayersByName(aLayer.name)) ==0:
            
            vLayer=QgsVectorLayer(os.path.join(datapath, aLayer.filename), aLayer.name, "ogr")
            if not vLayer.isValid():
                raise Exception("Invalid Layer: " + aLayer.name)
            
            #iface.messageBar().pushMessage("Error", "I'm sorry Dave, I'm afraid I can't \
             # do that", level=QgsMessageBar.CRITICAL)

            if aLayer.style is not None:
                vLayer.loadNamedStyle(os.path.join(datapath, aLayer.style))
                                                                  
            QgsMapLayerRegistry.instance().addMapLayer(vLayer)

    def removeLayer(self,aLayer):
        if len(QgsMapLayerRegistry.instance().mapLayersByName(aLayer.name)) >0:              
            for i in range(len(QgsMapLayerRegistry.instance().mapLayersByName(aLayer.name))):
                QgsMapLayerRegistry.instance().removeMapLayer(QgsMapLayerRegistry.instance().mapLayersByName(aLayer.name)[i].id())
                                             
                                            
    
