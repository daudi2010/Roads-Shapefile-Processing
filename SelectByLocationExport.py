# intersect polygons  with point data

import arcpy,os,glob

#  define  workspace

arcpy.env.overwriteOutput = True
out_cr= arcpy.SpatialReference(4326)# WGS84 DD
matches = [] # only polygons
counter=0
# point data
point_data=r"\\GEODEV-SRV\Kajiado\MergedPointData22Nov"
# define projection
workspace=r"\\GEODEV-SRV\Kajiado\PointDataPerCounty\\"
polygonfolders=r"D:\RICS2016\ProjectCountyData"

for root, dirs, files in os.walk(polygonfolders):
    for  filename in files:
        if filename.endswith(".shp"): # only shapefiles
            match = (os.path.join(root, filename))#  Create file path
            # check geometry type
            desc = arcpy.Describe(match)
            # Get the shape type (Polygon, Polyline) of the feature class
            #
            shapetype = desc.shapeType
            #print shapetype
            if shapetype == "Polygon": # only roads
                print "Defining proj for :"
                print match
                # define projection
                arcpy.DefineProjection_management(match, out_cr)
                matches.append (match)  # append files
                counter = counter + 1

print" Defined projection for {0} files".format(counter)

resultlist = [y for x in os.walk(point_data) for y in glob.glob(os.path.join(x[0], '*.shp'))]

# Select by location

for  poly in matches:
        
     for pt in resultlist:
         name2=os.path.basename(pt)
         arcpy.MakeFeatureLayer_management(pt, "layerfFeature") #selection is performed on a layer
         #polygon layer
         #arcpy.MakeFeatureLayer_management(poly, "polygonFeature") #selection is performed on a layer
         outfile=os.path.basename(poly).replace("Boundary.shp","")
         print workspace+outfile+"_"+name2
         # point data within  county  boundary layer"
         arcpy.SelectLayerByLocation_management('layerfFeature', 'intersect',poly ) #select based on geometry
         arcpy.CopyFeatures_management("layerfFeature", workspace+outfile+"_"+name2) # export the selected features in a new feature class
         print outfile +" done.."
         
print "Success!!"        


