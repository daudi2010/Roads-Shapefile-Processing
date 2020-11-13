###############################################################################################################
"""
This script  classifies roads acording to SURFACE TYPE and ROAD RESERVE WIDTH Through selection by ATTRIBUTES
Written by David Kanyari for Rics Project 2016
You just need to declare input folder with one roads shapefile and an output folder where new shapefile will be exported to
"""
#################################################################################################################
import arcpy, os
arcpy.CheckOutExtension('Spatial')
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False

# Required  select by Surfacetype attributes
# Rationale
case_paved ="CW_Surf_Ty	IN('Asphalt', 'Concrete BL', 'Concrete JT', 'Concrete REIN','Surface Dressing','Set Stone') AND R_Reserve >=9" # Paved
case_gravel="CW_Surf_Ty	IN('Gravel') AND R_Reserve >=9 " # Gravel
case_earth= "CW_Surf_Ty	IN('Earth','Other','Track') AND R_Reserve >=9" # Earth
case_narrow="R_Reserve < 9" # Narrow roads ! less than 9m in Road Reserve length with mixed surface types

# Create dictionary object
cases={"Paved":case_paved,"Gravel":case_gravel,"Earth":case_earth,"Narrow":case_narrow}

# Define the folder paths
folders=r'D:\RICS2016\Edited'
out=r'D:\RICS2016\Edited\Surfacetypes'

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
             for key,value in cases.iteritems():
                 name=key
                 print
                 print "Selecting and exporting "+name + " roads.."
                 arcpy.AddMessage("Shapefile {0}".format(shape))
                 arcpy.MakeFeatureLayer_management(shape, "lyr")
                 arcpy.SelectLayerByAttribute_management ("lyr", "NEW_Selection", value)
                 arcpy.FeatureClassToFeatureClass_conversion("lyr", outDir, name)
                 #arcpy.GetMessages() # empty
                 print "Done"
                 print "Successfully exported "+name + " roads.."
                 print "###########################################################################################"
