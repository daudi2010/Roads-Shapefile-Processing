import os
import arcpy,os,sys,string,fnmatch,glob
import glob
from datetime import datetime
serverpath=r"D:\RICS2016\KAJIADOKRBSHAPEFILES"
filesMerge=[]
# Directories not to be looked at
dirlist=['Day123','Day2','Day3','Day4','Day5','Edited','KMLs','PHOTOS','KRBRICSDATA.gdb','CombinedshapeFilesByDate','Photos2','Days']

shapefiles_to_Match_merge=['Bridge.shp',
'Drift.shp',
'Facility.shp',
'Institut.shp',
'Pipe_Cul.shp',
'PosnPnt.shp',
'Railway_.shp',               
'River.shp',
'Road.shp',
'Slab_Cul.shp',
'Town.shp',
'Point_ge.shp'
]
arcpy.env.workspace=(os.path.join(serverpath, "CombinedshapeFilesByDate"))

for shapefile in shapefiles_to_Match_merge:
    matches = []
    counter=0
    merged_shapefile=shapefile.split(".")[0]+"_Merged_"+datetime.now().strftime('%d%m%Y')+".shp"
    
    for root,dirs,files in os.walk(serverpath):
        # print files
        # list shapefiles
        
        if dirs  not in dirlist:
               #print dirs
               print
               for filename in fnmatch.filter(files, shapefile):# look for only shapefiles inthe folders
                   match = (os.path.join(root, filename))#  Create file path
                   #print match
                   matches.append (match)  # append files to list
                   counter = counter + 1
    if len(matches)>0: # Avoid empty list error!!!!
        print  
        print " Merging " +str(counter)+" "+shapefile.split(".")[0]+"s files..\n"
        print matches
        arcpy.Merge_management(matches, merged_shapefile)
        print
        print merged_shapefile +" created successfully!"
        print "\n #############################################################################"
print
print "Success!"
