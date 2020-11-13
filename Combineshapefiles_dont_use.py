# Combine shapefiles in folders and subfolders
import arcpy,os,sys,string,fnmatch,glob
import arcpy.mapping
from arcpy import env
import fnmatch
from datetime import datetime
# set  workspace for days work

#arcpy.env.workspace ="D:\\RICS2016\\KAJIADOKRBSHAPEFILES\Day6"

# batch project from UTM to WGS84
arcpy.env.workspace ="D:\\RICS2016\\KAJIADOKRBSHAPEFILES"
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
out_cs = 'GCS_WGS_1984'
transformation="Arc_1960_To_WGS_1984_2"
template="C:\\Users\hp\\Desktop\\DAY6\\Road_merged_19102016.shp" #wgs84
rootpath="D:\\RICS2016\\KAJIADOKRBSHAPEFILES\\DAY1-DAY5-Combined"
res=""
for shapefile in shapefiles_to_Match_merge:
    matches = []
    counter=0
    merged_shapefile=os.path.join(rootpath,shapefile.split(".")[0]+"_merged_"+datetime.now().strftime('%d%m%Y')+".shp")
    merged_shapefile_project=os.path.join(rootpath,shapefile.split(".")[0]+"_merged_proj"+datetime.now().strftime('%d%m%Y')+".shp")
    
    for root, dirs, files in os.walk(arcpy.env.workspace):
        
    
        for filename in fnmatch.filter(files, shapefile):# look for only shapefiles inthe folders
            match = (os.path.join(root, filename))#  Create file path
            #print match
            matches.append (match)  # append files
            counter = counter + 1
         
         
    #print matches
    print " Merging Files....."+str(counter) +" Files:..."
    #Merge  files  here
   
    if len(matches)>0:
        arcpy.Merge_management(matches, merged_shapefile)
        # merge
        print merged_shapefile +"  created"
        print " Reprojecting from UTM to WGS84"
        #projection

        try:
             res = arcpy.BatchProject(merged_shapefile, rootpath, out_cs, template, transformation)
             if res.maxSeverity == 0:
                print "projection of all datasets successful"
             else:
                print "failed to project one or more datasets"
        except:
             #print res.getMessages()
             print " no projection done"
