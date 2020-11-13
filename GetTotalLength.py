import os
import arcpy
from arcpy import env  
env.workspace = r"D:\RICS2016\UTM\Surfacetypes"  
  
fc = "Earth_11112016.shp"  
  
list = []  
  
rows = arcpy.SearchCursor(fc)  
for row in rows:  
    ln = row.getValue("L_Length")  
    list.append(ln)  
  
print "Total Length is {0} km" .format(sum(list))  
