# Check Schema  and  merge  point data

import arcpy
import glob
import os

# output directory
output_dir=r"\\MergedPointData22Nov"
# list of  available .shp  files
shapefiles=glob.glob(r"\\Day1-Day21Combined_UneditedPointData\\*.shp")

rootpath=r"\\EDITTED DATA"
#list of other .shp files in sserver
resultlist = [y for x in os.walk(rootpath) for y in glob.glob(os.path.join(x[0], '*.shp'))]
#loop and check schema
#rootpath=r"\\EDITTED DATA"
for feature in shapefiles:
    print feature
    field_names=[]
    merged_shapefile=""
     
    matches = []
    counter=0
    field_names = [f.name for f in arcpy.ListFields(feature)] #  list field names
    
    field_names2=[]
    for files in resultlist:
        field_names2 = [f.name for f in arcpy.ListFields(files)] #  list field names
        #print field_names2
        if set(field_names2)==set(field_names):
           print files
           print " matched schema"
           # The features share same schema
           matches.append (files) # append to match list
           counter = counter + 1
           
    if len(matches)>0:
        merged_shapefile=os.path.join(output_dir,os.path.basename(feature)) # name of output file
        print " Merging Files.............."
        matches.append (feature) #  dont forget to include original file
        print "Merging {0} {1} files".format(len(matches),os.path.basename(feature))
        arcpy.Merge_management(matches, merged_shapefile)
        print merged_shapefile +"  created"
    print "Done"
print "Success"
