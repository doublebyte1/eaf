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
strWpi=QtCore.QCoreApplication.translate("LyrMngr","World Port Index")
strCountries=QtCore.QCoreApplication.translate("LyrMngr","Global Administrative Units Layer")

strSelection=QtCore.QCoreApplication.translate("LyrMngr","selection_polygon")

strEezClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strEez) 
strWpiClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strWpi)
strCountriesClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strCountries)

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))

class aLayer:    
    def __init__(self,filename,name):
        self.name=name
        self.filename=filename

class LyrMngr:

    def __init__(self):
        self.initLayers()                


    def initVLayer(self,filename,name):
        return QgsVectorLayer(os.path.join(datapath, filename), name, "ogr")

    def initLayers(self):

        layerList=dict()
        
        layerList[strCountries]=aLayer("g0000_0.shp",strCountries)
        layerList[strEez]=aLayer("World_EEZ_LR_v7_2012.shp",strEez)
        layerList[strWpi]=aLayer("WPI.shp",strWpi)
                
        layerList[strSelection]=aLayer( None, strSelection) #memory layer
        
        layerList[strEezClp]=aLayer( "clipped_eez.shp", strEezClp)
        layerList[strCountriesClp]=aLayer( "clipped_countries.shp",  strCountriesClp)
        layerList[strWpiClp]=aLayer("clipped_ports.shp",  strWpiClp)
        
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
                                                                  
            QgsMapLayerRegistry.instance().addMapLayer(vLayer)

    def removeLayer(self,aLayer):
        if len(QgsMapLayerRegistry.instance().mapLayersByName(aLayer.name)) >0:              
            for i in range(len(QgsMapLayerRegistry.instance().mapLayersByName(aLayer.name))):
                QgsMapLayerRegistry.instance().removeMapLayer(QgsMapLayerRegistry.instance().mapLayersByName(aLayer.name)[i].id())
                                             
                                            
    
