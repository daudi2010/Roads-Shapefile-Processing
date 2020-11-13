#CSV to shapefile
#Import Modules
import arcpy
from arcpy import env
import os
import csv

# folder with csv files
#set workspace parameter: ONLY USER DEFINED INPUT-

csvs_path = r"G:\SMEC\csvs"
#set workspace parameter: ONLY USER DEFINED INPUT-

arcpy.env.workspace =csvs_path

out_shapefiles=r"G:\SMEC\csvs\shapes"
template=r"G:\SMEC\csvs\shapes\videos.shp"
############SCRIPT###############################


def MakePoint(inputx, outpath, output):
    print "here"
    print inputx
    #environment settings
    env.overwriteOutput = True
    print "reading file"
    #Open File
    if os.path.exists(inputx):
        print "Starting"
        video = open(inputx, "rb")

        #create csvReader object to process the header
        csvReader = csv.reader(video,delimiter=',')
        print "read csv"
        has_m = "DISABLED"
        has_z = "DISABLED"
        print output
        print outpath
        spatialRef =arcpy.SpatialReference(4326) # Wgs 84
        print "creating feature class"
        output = arcpy.CreateFeatureclass_management(outpath, output, "POINT", template, has_m, has_z, spatialRef) 
        print(arcpy.GetMessages())
        
        with open(inputx, 'rb') as csvfile[1:]:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                lat = float(row[0])
                lon = float(row[1])
                #print ', '.join(row)
                pt = arcpy.Point(lon,lat)
                print [lat,lon]
                print "point updated"
                with arcpy.da.InsertCursor(output, ("SHAPE@",)) as cursor:
                    point = arcpy.Point(pt, spatialRef)
                    cursor.insertRow((point,)) 


  
    else:
         print "Not working"


###############End SCRIPT ########################
        
#environment settings
arcpy.env.overwriteOutput = True


#create list of CSV files in folder

csvs = arcpy.ListFiles("*.csv")
count=1
outpath=out_shapefiles
#Create for loop of CSV files
try:
   print "Working on"
   for csvd in csvs:
        #set parameters
       
        print str(count)+ ":"+csvd
        inputx = os.path.join(csvs_path,csvd)
        filename=csvd.split(".")[0].replace(" ","_")
       
        output = os.path.join(out_shapefiles,filename + ".shp")
        print "Making shapefile"
        #call in module
        MakePoint(inputx, outpath, output)
        print(arcpy.GetMessages())
        count=count+1

except:
   print(arcpy.GetMessages())
   print "There has been an error processing the module."
#retrieve all messages 
print(arcpy.GetMessages())
