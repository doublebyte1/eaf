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

import processing

strEez=QtCore.QCoreApplication.translate("LyrMngr","200 Nautical Miles Arc Limits") 
strWpi=QtCore.QCoreApplication.translate("LyrMngr","World Port Index (zoom in to display)")
strCountries=QtCore.QCoreApplication.translate("LyrMngr","Global Administrative Units Layer")

strSelection=QtCore.QCoreApplication.translate("LyrMngr","selection_polygon")

strEezClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strEez) 
strWpiClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strWpi)
strCountriesClp=QtCore.QCoreApplication.translate("LyrMngr","clipped " + strCountries)

strEezRclp=QtCore.QCoreApplication.translate("LyrMngr","reclipped " + strEez) 
strWpiRclp=QtCore.QCoreApplication.translate("LyrMngr","reclipped " + strWpi)
strCountriesRclp=QtCore.QCoreApplication.translate("LyrMngr","reclipped " + strCountries)

basepath = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(basepath, "..", "eaf/data"))

## Layer
#
#  This is a layer structure, that contains a name, a filename, and a style filename. 
#  It is provided for convenience, as we can store these objects lightly in a container, and instantiate them at any moment.
################################################   
class aLayer:
    ## Constructor
    #
    #  This is a constructor
    ##########################################################
    def __init__(self,filename,name,style):
        self.name=name
        self.filename=filename
        self.style=style

## Layer Manager
#
#  This class implements the layer manager.    
#  Here we store a dictionary with all the layers we need, and we manage them, by adding them/ removing them from the map view.
#  We also perform operations that generate new layers (e.g.: clipping); in reality, all the GIS code is in this class.
################################################   
class LyrMngr:
    ## Constructor
    #
    #  This is a constructor
    ##########################################################
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

        layerList[strEezRclp]=aLayer( "reclipped_eez.shp", strEezRclp,"World_EEZ_LR_v7_2012.qml")
        layerList[strCountriesRclp]=aLayer( "reclipped_countries.shp",  strCountriesRclp ,"g0000_0.qml")
        layerList[strWpiRclp]=aLayer("reclipped_ports.shp",  strWpiRclp, "WPI.qml")
        
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
                                             
                                            
    def createLayerFromExtent(self,eaf)    :            

        vl = QgsVectorLayer("Polygon?crs=epsg:4326",
                     strSelection, "memory")
                                
        if not vl.isValid():
            print "Layer failed to create!"     
                                            

        canvas=eaf.iface.mapCanvas()
        rect=canvas.extent()
        
        pr = vl.dataProvider() 
        pr.addAttributes([ QgsField("ID", QtCore.QVariant.String)])               
        
        seg = QgsFeature()
        aGeometry=QgsGeometry.fromRect(rect)
        if  aGeometry.isGeosEmpty() or not aGeometry.isGeosValid():
            print "invalid geometry"
            return False
            
        seg.setGeometry(aGeometry)
        
        if not seg.isValid:
            print "invalid feature"
            return False
        
        seg.setAttributes(["1"])#who cares about this?
        
        pr.addFeatures([seg])
         
        vl.updateExtents()                       
        QgsMapLayerRegistry.instance().addMapLayer(vl)
        
        return True;

    def createLayerFromCountry(self,eaf,name)    :            

        aLayer=self.layerList[strCountries]# find countries layer
        cLayer=QgsVectorLayer(os.path.join(datapath, aLayer.filename), aLayer.name, "ogr")
        
        if not cLayer.isValid():
            raise Exception("Invalid Layer: " + aLayer.name)

        #vl = QgsVectorLayer("Polygon?crs=epsg:4326",
         #            strSelection, "memory")
                                
        #if not vl.isValid():
         #   print "Layer failed to create!"     
                                                    
        #pr = vl.dataProvider() 
        #pr.addAttributes([ QgsField("ID", QtCore.QVariant.String)])               


        cLayer.select([1])

        aLayer=self.layerList[strSelection]# find selection layer        
        error = QgsVectorFileWriter.writeAsVectorFormat(cLayer, aLayer.filename, 
                                                        "CP1250", None, "memory",True)
        
        #cLayer.selectAll()
        #print cLayer.selectedFeatureCount()
        
        
        #QgsMapLayerRegistry.instance().addMapLayer(vl)
        
        return True;
                    
    def clipLayer(self,input,clip,output):
        #TODO: change this to generate a memory layer?
        return processing.runalg("qgis:clip",input,clip,os.path.join(datapath, output))

                    
    def clipLayers(self):
        ok=True
        if not self.clipLayer(self.layerList[strEez].name,strSelection,self.layerList[strEezClp].filename):
            ok=False        
        if not self.clipLayer(self.layerList[strCountries].name,strSelection,self.layerList[strCountriesClp].filename):
            ok=False
        if not self.clipLayer(self.layerList[strWpi].name,strSelection,self.layerList[strWpiClp].filename):
            ok=True
                                        
        return ok

    def reclipLayers(self):
        ok=True
        if not self.clipLayer(self.layerList[strEezClp].name,strSelection,self.layerList[strEezRclp].filename):
            ok=False        
        if not self.clipLayer(self.layerList[strCountriesClp].name,strSelection,self.layerList[strCountriesRclp].filename):
            ok=False
        if not self.clipLayer(self.layerList[strWpiClp].name,strSelection,self.layerList[strWpiRclp].filename):
            ok=True
                                        
        return ok
    
    def readCountries(self):
        aLayer=self.layerList[strCountries]# find countries layer
        vLayer=QgsVectorLayer(os.path.join(datapath, aLayer.filename), aLayer.name, "ogr")
        
        if not vLayer.isValid():
            raise Exception("Invalid Layer: " + aLayer.name)
        
        aList=[]
        iter = vLayer.getFeatures()
        for feat in iter:
            attrs = feat.attributes()
            idx = vLayer.fieldNameIndex('ADM0_Name')
            #print feat.attributes()[idx]            
            aList.append(feat.attributes()[idx])
               
        #remove duplicates
        noDups=list(set(aList))
        sorted=noDups.sort()
                                            
        return noDups
    

