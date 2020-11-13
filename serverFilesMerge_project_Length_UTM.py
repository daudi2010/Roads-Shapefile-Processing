import os
import arcpy
import glob
from datetime import datetime
serverpath=r"\\GEODEV-SRV\Kajiado\EDITTED DATA"
filesMerge=[]
count=0
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False

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

#Project to UTM and save as new file (for in feature should be Feature Layer / Feature Dataset )
arcpy.Project_management(input_fc, output_fc, out_coordinate_system)
print "...Done \n"

# calculate length (geometry)
print "Updating  geoemtry and rewriting  \'Length\'field"
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
                 name=key
                 namefield=fieldName
                 print
                 print "Selecting and exporting "+name + " roads.."
                 
                 #arcpy.SelectLayerByAttribute_management ("lyr", "NEW_Selection", value)
                 try:    
                   arcpy.SelectLayerByAttribute_management ("lyr", "NEW_Selection", value)

                   rows = arcpy.SearchCursor("lyr")
                   row = rows.next()
                   sum_length=0
                   while row:        
                         #row.getValue(nameField)
                         sum_length+=row.getValue(nameField)
                         row = rows.next()
                   del row, rows
                   print name +" Roads:" +sum_length +"km\n"

                 except:
                     print arcpy.GetMessages()

                 arcpy.FeatureClassToFeatureClass_conversion("lyr", outDir, name)
                           
                 #arcpy.GetMessages() # empty
                 print "Done"
                 print "Successfully exported "+name + " roads.."
                 print "###########################################################################################"

print "Success"


























print "Success!"
print 
print "##################################################################"
