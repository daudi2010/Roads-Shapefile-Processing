import os
import arcpy
import glob
from datetime import datetime
serverpath=r"\\GEODEV-SRV\Kajiado\EDITTED DATA"
filesMerge=[]
count=0
print "###################################################################"
print 
print "A script  for merging shapefiles in different folders.."
print
print "###################################################################"
print
print "Files To Merge.."
for root,dirs,files in os.walk(serverpath):
    # print files
    # list shapefiles
        
    for filex in files:
        if filex.endswith(".shp"):
             count=count+1
             print
             print str(count)+":" +os.path.join(root, filex)
             filesMerge.append(os.path.join(root, filex))
    
#print filesMerge
merged_shapefile=os.path.join(r"D:\RICS2016\Edited","EditedCombined_"+datetime.now().strftime('%d%m%Y')+".shp")
print
print "###################################################################"
print "Merging files....."
# merge shapefiles
if len(filesMerge)>0:
        arcpy.Merge_management(filesMerge, merged_shapefile)
        print merged_shapefile +" created!"
print        
print "Success!"
print 
print "##################################################################"
