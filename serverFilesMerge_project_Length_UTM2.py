import os
import arcpy
import glob
from datetime import datetime
serverpath=r"\\GEODEV-SRV\Kajiado\EDITTED DATA"
filesMerge=[]
count=0
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
datestring=datetime.now().strftime('%d%m%Y')

print "###################################################################"
print 
print "A script  for merging shapefiles in different folders.."
print
print "###################################################################"
print
print "Files To Merge.."

print "Selecting only line features"
for root, dirs, files in os.walk(serverpath):
    for  filename in files:
        if filename.endswith(".shp"): # only shapefiles
            match = (os.path.join(root, filename))#  Create file path
            # check geometry type
            desc = arcpy.Describe(match)
            # Get the shape type (Polygon, Polyline) of the feature class
            #
            shapetype = desc.shapeType
            #print shapetype
            #print "Selecting only line features"
            if shapetype == "Polyline": # only roads
                print match
                filesMerge.append (match)  # append files
                count = count + 1


   
#print filesMerge
merged_shapefile=os.path.join(r"D:\RICS2016\Edited","EditedCombined_"+datetime.now().strftime('%d%m%Y')+".shp")
print
print "###################################################################"
print "Merging files....."
# merge shapefiles
if len(filesMerge)>0 and not os.path.exists(merged_shapefile):
        arcpy.Merge_management(filesMerge, merged_shapefile)
        print merged_shapefile +" created!"
        

#Projection to UTM
input_fc=merged_shapefile
output_fc=os.path.join(r"D:\RICS2016\UTM","EditedCombined_UTM"+datetime.now().strftime('%d%m%Y')+".shp")

#UTM#
out_coordinate_system = arcpy.SpatialReference(21037)#Arc1960 UTM 37S

#add length column to input datasets
fieldName = "L_Length"
arcpy.AddField_management(input_fc, fieldName, "Double")

print "Reprojecting to UTM zone 37S"
print

#Project to UTM and save as new file (for infeature should be Feature Layer / Feature Dataset )
arcpy.Project_management(input_fc, output_fc, out_coordinate_system)
print "...Done \n"

# calculate length (geometry)
print "Updating  geometry and rewriting  \'Length\'field"
arcpy.CalculateField_management(output_fc, fieldName, "!shape.length@kilometers!","PYTHON_9.3")
print "Done.."
print

################################## Summaries #####################################################################################


# Required  select by Surfacetype attributes
# Rationale
case_paved ="CW_Surf_Ty	IN('Asphalt', 'Concrete BL', 'Concrete JT', 'Concrete REIN','Surface Dressing','Set Stone') AND R_Reserve >=9" # Paved
case_gravel="CW_Surf_Ty	IN('Gravel') AND R_Reserve >=9 " # Gravel
case_earth= "CW_Surf_Ty	IN('Earth','Other','Track') AND R_Reserve >=9" # Earth
case_narrow="R_Reserve < 9" # Narrow roads ! less than 9m in Road Reserve length with mixed surface types

# Create dictionary object
cases={"Paved":case_paved,"Gravel":case_gravel,"Earth":case_earth,"Narrow":case_narrow}

# Define the folder paths
folders=r'D:\RICS2016\UTM'
out=r'D:\RICS2016\UTM\Surfacetypes'

# Select by attributes and Export
Totallist=[]
if os.path.exists(folders):  # only folders (directories) in folders
        outDir = out         # keep track of where it's going
        #os.makedirs(outDir) # doesn't matter if it does or doesn't exist, make sure it's there

        arcpy.env.workspace=folders
        arcpy.AddMessage("Workspace is {0}, exporting to {1}".format(arcpy.env.workspace,outDir)) # follow the changing workspace
        print "Workspace is {0}, exporting to {1}".format(arcpy.env.workspace,outDir)
        arcpy.GetMessages()# empty
        shapefiles=arcpy.ListFeatureClasses('*.shp')
        for shape in shapefiles:
             arcpy.AddMessage("Shapefile {0}".format(shape))
             arcpy.MakeFeatureLayer_management(shape, "lyr")
             for key,value in cases.iteritems():
                 name=key+"_" + datestring
                 print name
                 namefield=fieldName
                 print
                 print "Selecting and exporting "+key + " roads.."
                 
                
                 try:    
                   arcpy.SelectLayerByAttribute_management ("lyr", "NEW_Selection", value)

                   
                 except:
                     print arcpy.GetMessages()

                 arcpy.FeatureClassToFeatureClass_conversion("lyr", outDir, name)
                 shapefilecursor=(os.path.join(outDir, name))+".shp"
                 
                 # Get lengths in kms
                 #arcpy.env.workspace=outDir # change environment
                 try:
                   list=[]
                   rows = arcpy.SearchCursor(shapefilecursor)
                   for row in rows:  
                       ln = row.getValue("L_Length")  
                       list.append(ln)
                       Totallist.append(ln)
                   
                   print key +" Roads: \nTotal Length is {0} km" .format(sum(list)) 
                 except:
                   arcpy.GetMessages()  
                 #arcpy.GetMessages() # empty
                 print "Done"
                 print "Successfully exported "+name + " roads.."
                 print "###########################################################################################"

print "###########################################################################################"

print "Success"
print "TOTAL LENGTH OF ALL ROADS: {0} Km".format(sum(Totallist))
print 
print "###########################################################################################"

