# Combine shapefiles in folders and subfolders
# Merging point data  only 
import arcpy,os,sys,string,fnmatch,glob
import arcpy.mapping
from arcpy import env
import fnmatch
from datetime import datetime
# set output workspace
arcpy.env.workspace =r"\\GEODEV-SRV\Kajiado\Day1-Day21Combined_UneditedPointData"

shapefiles_to_Match_merge=['Bridge.shp',
'Drift.shp',
'Facility.shp',
'Institut.shp',
'Pipe_Cul.shp',
'PosnPnt.shp',
'Railway_.shp',               
'River.shp',
'Box_Culv.shp',
'Slab_Cul.shp',
'Town.shp',
'MaintPro.shp',
'Point_ge.shp',
'Road_Hum.shp'                          
]

rootpath="D:\RAWFILES\Day1-Day21UneditedRaw"
for shapefile in shapefiles_to_Match_merge:
    print "Merging {0}s ............".format(shapefile.split(".")[0])
    matches = []
    counter=0
    #merged_shapefile=shapefile.split(".")[0]+"_Merged_"+datetime.now().strftime('%d%m%Y')+".shp"
    merged_shapefile=shapefile
    for root, dirs, files in os.walk(rootpath):
        
    
        for filename in fnmatch.filter(files, shapefile):# look for only shapefiles inthe folders
            match = (os.path.join(root, filename))#  Create file path
            #print match
            matches.append (match)  # append files
            counter = counter + 1
         
         
    #print matches
    print " Merging Files....."
    #Merge  files  here
   
    if len(matches)>0:
        arcpy.Merge_management(matches, merged_shapefile)
        print merged_shapefile +"  created"
    print "Done"    
    #print counter   
print "Success"
