from sys import argv
#script, input_file, EPSG_code, delimiter, export_shp = argv
import arcpy
from arcpy import env
import os
import csv
import osgeo.ogr, osgeo.osr #we will need some packages
from osgeo import ogr #and one more for the creation of a new field

EPSG_code="4326"

#CSV folder
csvs_path = r"G:\SMEC\csvs"

arcpy.env.workspace =csvs_path

out_shapefiles=r"G:\SMEC\csvs\shapes"

#create list of CSV files in folder
csvs = arcpy.ListFiles("*.csv")
count=1
outpath=out_shapefiles
#Create for loop of CSV files
try:
   print "Working on"
   for csvd in csvs:
        #set parameters
       
        print str(count)+ ":"+csvd
        inputx = os.path.join(csvs_path,csvd)
        filename=csvd.split(".")[0].replace(" ","_")
       
        output = os.path.join(out_shapefiles,filename + ".shp")
        print "Making shapefile"
        #call in module
        
        count=count+1

        export_shp =output
        delimiter=","
        input_file= inputx
        spatialReference = osgeo.osr.SpatialReference() #will create a spatial reference locally to tell the system what the reference will be
        spatialReference.ImportFromEPSG(int(EPSG_code)) # wgs84..
        driver = osgeo.ogr.GetDriverByName('ESRI Shapefile') # will select the driver for our shp-file creation.
        shapeData = driver.CreateDataSource(export_shp) #so there we will store our data
        layer = shapeData.CreateLayer('layer', spatialReference, osgeo.ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
        layer_defn = layer.GetLayerDefn() # gets parameters of the current shapefile
        index = 0

        with open(input_file, 'rb') as csvfile:
                readerDict = csv.DictReader(csvfile, delimiter=delimiter)
                for field in readerDict.fieldnames:
                        new_field = ogr.FieldDefn(field, ogr.OFTString) #we will create a new field called latl,lon
                        layer.CreateField(new_field)
                for row in readerDict:
                        #print(row['Latitude'], row['Longitude'])
                        point = osgeo.ogr.Geometry(osgeo.ogr.wkbPoint)
                        point.AddPoint(float(row['Longitude']), float(row['Latitude'])) #we do have LATs and LONs as Strings, so we convert them
                        feature = osgeo.ogr.Feature(layer_defn) 
                        feature.SetGeometry(point) #set the coordinates
                        feature.SetFID(index)
                        for field in readerDict.fieldnames:
                                i = feature.GetFieldIndex(field)
                                feature.SetField(i, row[field])
                        layer.CreateFeature(feature)
                        index += 1
        shapeData.Destroy() #lets close the shapefile
        print "Done"
except:
   print "There has been an error processing the module."
   
print "Finished"
