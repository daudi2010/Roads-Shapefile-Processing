# merge shapefiles of same feature type in same folder
import arcpy,os,sys,string,fnmatch,glob
import arcpy.mapping
from arcpy import env
arcpy.env.workspace ="D:/RICS2016/KRBRoadsV1/"

print "Combining shapefiles in folder :" + arcpy.env.workspace
print "Files found....\n"
fcs = arcpy.ListFeatureClasses("*.shp", "")
matches = []
for shp in fcs:    
    print shp +"\n"
    matches.append (shp)
arcpy.Merge_management(matches, "KRB_ROADS_WGS84.shp")
print "Success"
