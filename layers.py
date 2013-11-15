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
from PyQt4.QtCore import QObject, pyqtSignal 
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

strGrid=QtCore.QCoreApplication.translate("LyrMngr","grid")

basepath = os.path.dirname(__file__)

## Layer
#
#  This is a layer structure, that contains a name, a filename, a style filename, and a path. 
#  It is provided for convenience, as we can store these objects lightly in a container, and instantiate them at any moment.
################################################   
class aLayer:    
    ## Constructor
    #
    #  This is a constructor
    ##########################################################
    def __init__(self,filename,name,style,datapath):
        self.name=name
        self.filename=filename
        self.style=style
        self.datapath=datapath

## Layer Manager
#
#  This class implements the layer manager.    
#  Here we store a dictionary with all the layers we need, and we manage them, by adding them/ removing them from the map view.
#  We also perform operations that generate new layers (e.g.: clipping); in reality, all the GIS code is in this class.
################################################   
class LyrMngr(QtCore.QObject):
    
    #This is our internal datapath for storage (base layers)        
    datapath = os.path.abspath(os.path.join(basepath, ".", "./data"))
    userPath=datapath
    
    dataPathChanged = QtCore.pyqtSignal(str)  
    ## Constructor
    #
    #  This is a constructor
    ##########################################################
    def __init__(self):
        super(LyrMngr, self).__init__()
         
        self.initLayers()                

    ## Set User Data Path
    #
    #  Sets data path on generated layers, to a user defined value
    ##########################################################
    def setUserDataPath(self,aPath):
        for x in self.layerList.keys():
            if (x != strCountries) and (x != strEez) and (x !=  strWpi) :
                self.layerList[x].datapath=aPath

        self.userPath=aPath
        self.dataPathChanged.emit(aPath)
         
    def restart(self):
        self.setUserDataPath(self.datapath)

    def initVLayer(self,filename,name,datapath):
        return QgsVectorLayer(os.path.join(datapath, filename), name, "ogr")

    def initLayers(self):

        layerList=dict()
        
        layerList[strCountries]=aLayer("g0000_0.shp",strCountries,"g0000_0.qml",self.datapath)
        layerList[strEez]=aLayer("World_EEZ_LR_v7_2012.shp",strEez,"World_EEZ_LR_v7_2012.qml",self.datapath)
        layerList[strWpi]=aLayer("WPI.shp",strWpi,"WPI.qml",self.datapath)
                
        layerList[strSelection]=aLayer( None, strSelection,None,None) #memory layer
        
        layerList[strEezClp]=aLayer( "clipped_eez.shp", strEezClp,"World_EEZ_LR_v7_2012.qml",self.datapath)
        layerList[strCountriesClp]=aLayer( "clipped_countries.shp",  strCountriesClp ,"g0000_0.qml",self.datapath)
        layerList[strWpiClp]=aLayer("clipped_ports.shp",  strWpiClp, "WPI.qml",self.datapath)

        layerList[strEezRclp]=aLayer( "reclipped_eez.shp", strEezRclp,"World_EEZ_LR_v7_2012.qml",self.datapath)
        layerList[strCountriesRclp]=aLayer( "reclipped_countries.shp",  strCountriesRclp ,"g0000_0.qml",self.datapath)
        layerList[strWpiRclp]=aLayer("reclipped_ports.shp",  strWpiRclp, "WPI.qml",self.datapath)

        layerList[strGrid]=aLayer("grid.shp",  strGrid, None,self.datapath)
        
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
            
            vLayer=QgsVectorLayer(os.path.join(aLayer.datapath, aLayer.filename), aLayer.name, "ogr")
            if not vLayer.isValid():
                raise Exception("Invalid Layer: " + aLayer.name)
            
            #Setting the crs (in case the file does not have one!)  
            aCrs=vLayer.crs()
            if not aCrs.isValid():
                crs = QgsCoordinateReferenceSystem()
                crs.createFromProj4("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
                if not crs.isValid():
                    raise Exception ("invalid crs")
                
                aCrs=crs
                                                        
            if aLayer.style is not None:
                vLayer.loadNamedStyle(os.path.join(aLayer.datapath, aLayer.style))
                                                                  
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

    def createLayerFromCountry(self,eaf,layerName,names)    :            

        aLayer=self.layerList[layerName]# find countries layer
        cLayer=QgsVectorLayer(os.path.join(aLayer.datapath, aLayer.filename), aLayer.name, "ogr")
        
        if not cLayer.isValid():
            raise Exception("Invalid Layer: " + aLayer.name)

        vl = QgsVectorLayer("Polygon?crs=epsg:4326",
                     strSelection, "memory")
                                
        if not vl.isValid():
            print "Layer failed to create!"     
                                                    
        pr = vl.dataProvider() 
        pr.addAttributes([ QgsField("ID", QtCore.QVariant.String)])               

        request=QgsFeatureRequest()

        #Builds the feature        
        exp=""
        for name in names:
            exp= exp +"\"ADM0_NAME\" = '" + name + "' "  
            if names.index(name) < len(names)-1:
                exp= exp + "OR "
            
        request.setFilterExpression(exp)
        features=cLayer.getFeatures(request)
        l=[]
        for f in features:
            l.append(f.id())
            
        cLayer.select(l)

        pr.addFeatures(  cLayer.selectedFeatures() )
        vl.updateExtents()        
        
        QgsMapLayerRegistry.instance().addMapLayer(vl)
        
        return True;
                    
    def clipLayer(self,input_,clip,datapath,output):
        #TODO: change this to generate a memory layer?
        return processing.runalg("qgis:clip",input_,clip,os.path.join(datapath, output))

                    
    def clipLayers(self):
        ok=True
        if not self.clipLayer(self.layerList[strEez].name,strSelection,self.layerList[strEezClp].datapath,self.layerList[strEezClp].filename):
            ok=False        
        if not self.clipLayer(self.layerList[strCountries].name,strSelection,self.layerList[strCountriesClp].datapath,self.layerList[strCountriesClp].filename):
            ok=False
        if not self.clipLayer(self.layerList[strWpi].name,strSelection,self.layerList[strWpiClp].datapath,self.layerList[strWpiClp].filename):
            ok=True
                                        
        return ok

    def reclipLayers(self):
        ok=True
        if not self.clipLayer(self.layerList[strEezClp].name,strSelection,self.layerList[strEezRclp].datapath,self.layerList[strEezRclp].filename):
            ok=False        
        if not self.clipLayer(self.layerList[strCountriesClp].name,strSelection,self.layerList[strCountriesRclp].datapath,self.layerList[strCountriesRclp].filename):
            ok=False
        if not self.clipLayer(self.layerList[strWpiClp].name,strSelection,self.layerList[strWpiRclp].datapath,self.layerList[strWpiRclp].filename):
            ok=True
                                        
        return ok
    
    def readCountries(self,layerName):
        aLayer=self.layerList[layerName]# find countries layer
        vLayer=QgsVectorLayer(os.path.join(aLayer.datapath, aLayer.filename), aLayer.name, "ogr")
        
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
    
    def layerExists(self,layerName):
        aLayer=self.layerList[layerName]# find countries layer
        vLayer=QgsVectorLayer(os.path.join(aLayer.datapath, aLayer.filename), aLayer.name, "ogr")
        
        return vLayer.isValid()
        
    def createGrid(self):
        
        aLayer=self.layerList[strCountriesRclp]# find countries layer
        vLayer=QgsVectorLayer(os.path.join(aLayer.datapath, aLayer.filename), aLayer.name, "ogr")
        
        if not vLayer.isValid():
            return False        
        
        gLayer=self.layerList[strGrid]

        #TODO: There is a problem with the crs of the grid (it is not coming correctly!!!!)
                             
        processing.runalg("qgis:creategrid", vLayer.extent().height()/250, vLayer.extent().height()/250, vLayer.extent().width(), vLayer.extent().height(),
                           vLayer.extent().center().x(), vLayer.extent().center().y(), 1, vLayer.crs(),os.path.join(gLayer.datapath, gLayer.filename))
        
        return True
        
