# Check Schema  and  merge  point data

import arcpy,os,sys,string,fnmatch,glob
import glob
import os

# output directory
output_dir=r"\\GEODEV-SRV\\Kajiado\\MergedPointData22Nov"
arcpy.env.overwriteOutput = True
# list of  available .shp  files
#shapefiles=glob.glob(r"\\GEODEV-SRV\\Kajiado\\Day1-Day21Combined_UneditedPointData\\*.shp")
print "Merging point data..."

shapefiles_to_Match_merge=[
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
'Road_Hum.shp' ,
'Rumble_s.shp'
]
rootpath=r"\\GEODEV-SRV\\Kajiado\\EDITTED DATA"
#list of other .shp files in sserver
resultlist = [y for x in os.walk(rootpath) for y in glob.glob(os.path.join(x[0], '*.shp'))]

for  shapefile in shapefiles_to_Match_merge:
   
    matches = []
    counter=0
    #field_names2=[]
  
    print " Checking....."
    print shapefile

    for root, dirs, files in os.walk(rootpath):
        
        for filename in fnmatch.filter(files, shapefile):
           
               match = (os.path.join(root, filename))#  Create file path
               matches.append (match)  # append files
               counter = counter + 1
           
    if len(matches)>0:
        merged_shapefile=os.path.join(output_dir,shapefile) # name of output file
        print "Merging Files.............."
        #matches.append (feature) #  dont forget to include original file
        print "Merging {0} {1} files".format(len(matches),shapefile)
        arcpy.Merge_management(matches, merged_shapefile)
        print merged_shapefile +"  created"
    print "Done"
print "Success"

