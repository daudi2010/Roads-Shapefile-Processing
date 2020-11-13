###############################################################################################################
"""
This script  classifies roads according to SURFACE TYPE and ROAD RESERVE WIDTH Through selection by ATTRIBUTES
and computes  the TOTAL LENGTH per that criteria
Written by David Kanyari for Rics Project 2018 - SMEC
You just need to declare input folder with at least one well formatted  and finallized roads shapefile a
"""
#################################################################################################################
import arcpy, os
from datetime import datetime
arcpy.CheckOutExtension('Spatial')
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False

datestring=datetime.now().strftime('%d%m%Y')

#add length column
fieldName = "Shape_Leng"  #!!! This must be declared
# Define the folder paths

shapefile=r'E:\smec\smec_Both_Zones.gdb\ROADS\WESTERN_CENTRAL_RoadsV2_6_11'


# A dictionary to hold statistics
surf_dictionary={}
# Define your rationale

# Surface Type  .. Defines the cases
case_paved ="CW_Surf_Ty	IN('Alsphalt' ,'Aphalt', 'Aspalt', 'Asphalt', 'Asphat', 'Brick', 'Concrete BL', 'Concrete JT', 'Concrete REIN', 'Conrete BL', 'Jointed Concrete', 'Paved', 'Premix', 'Set/Cobble Stone', 'Stone', 'Suface Dressing', 'Surface Dreeing', 'Surface dressing', 'Surface Dressing') AND RdReserve >=9" # Paved
case_gravel="CW_Surf_Ty	IN('Gravel') AND RdReserve >=9 " # Gravel
case_earth= "CW_Surf_Ty	IN('Earth','Other','Track') AND RdReserve >=9" # Earth
case_other ="CW_Surf_Ty	IN('Other','Track','') AND RdReserve >=9" # Earth
case_narrowbelow6="RdReserve <= 6" # Narrow roads ! less than 9m in Road Reserve length with mixed surface types
case_narrowabove6to9="RdReserve > 6 AND RdReserve <= 9"

# Surface Condition
Poor="CW_Surf_Co IN('Poor','P')"
Good="CW_Surf_Co IN('Good','G')"
Fair="CW_Surf_Co IN('Fair','Far')"
under_construction= "CW_Surf_Co IN ('Under Construction', 'Under Constuction', 'Under Cosntruction')"
Other="CW_Surf_Co IN('')"

# Road reserve
casebelow6m="RdReserve <=6"
case6to9m="RdReserve > 6 AND RdReserve <= 9"
case9to25m="RdReserve > 9 AND RdReserve <= 25"
case25to40m="RdReserve > 25 AND RdReserve <= 40"
caseabove40m="RdReserve > 40"

Road_reserves={"below6m":casebelow6m,"btn6to9m":case6to9m,"btn9to25m":case9to25m,"btn25to40m":case25to40m,"above40m":case25to40m}
 #Surface type dictionary
cases={"Paved":case_paved,"Gravel":case_gravel,"Earth":case_earth,"Narrowabove6to9":case_narrowabove6to9,"Narrowbelow6":case_narrowbelow6,"other":case_other}
 # condition
condition={"Poor":Poor,"Good":Good,"Fair":Fair ,"under_construction":under_construction,"Other":Other}
 # Road Classes
classes={"A":"A","B":"B", "C" :"C","D":"D","E":"E","F":"F","G":"G","A_urb":"A_urb","B_urb":"B_urb","C_urb":"C_urb","NR":"NR"}


# Select by attributes and Export
Totalsum=0
arcpy.MakeFeatureLayer_management(shapefile, "lyr")

#  select By surface type
for key, value in cases.iteritems():

        name = key + "_" + datestring
        print name
        namefield = fieldName
        print
        print "Selecting " + key + " roads.."

        try:
           arcpy.SelectLayerByAttribute_management("lyr", "NEW_Selection", value)
           # Get lengths in kms of the selected
           someValue = sum([r[0] for r in arcpy.da.SearchCursor("lyr", [fieldName])])
           Totalsum = Totalsum + someValue
           print key + " Roads: \nTotal Length is {0} km".format(someValue)
           surf_dictionary.update({key + "_Total": someValue})

        except:
           print arcpy.GetMessages()


# select by condition
for keycon, valuecon in condition.iteritems():
    for key, value in cases.iteritems():
        try:

           arcpy.SelectLayerByAttribute_management("lyr2", "NEW_Selection", value + " AND " + valuecon)
           # Get lengths in kms of the selected
           someValue = sum([r[0] for r in arcpy.da.SearchCursor("lyr2", [fieldName])])

           surf_dictionary.update({key + "_" + keycon: someValue})

        except:
           print arcpy.GetMessages()


# Select by Road class

for keyclas, valueclas in classes.iteritems():

    for keycon, valuecon in condition.iteritems():
        for key, value in cases.iteritems():

            try:
                valcl = "AND Class IN ('{0}')".format(valueclas)
                arcpy.SelectLayerByAttribute_management("lyr2", "NEW_Selection",
                                                value + " AND " + valuecon + valcl)
                #print  value + " AND " + valuecon + valcl
                someValue = sum([r[0] for r in arcpy.da.SearchCursor("lyr2", [fieldName])])

                surf_dictionary.update({key + "_" + keycon + "_" + keyclas: someValue})

            except:
              print arcpy.GetMessages()

# By road Reserve
for keyresv, valueresv in Road_reserves.iteritems():
    try:

        arcpy.SelectLayerByAttribute_management("lyr2", "NEW_Selection", valueresv)
        someValue = sum([r[0] for r in arcpy.da.SearchCursor("lyr2", [fieldName])])
        surf_dictionary.update({keyresv: someValue})
    except:
        print arcpy.GetMessages()

print "###########################################################################################"

print "Detailed Statistics"
for key,value in surf_dictionary.iteritems():
    print key +":"+str(value)
print

print "###########################################################################################"

print "TOTAL LENGTH OF ALL ROADS: {0} Km".format(Totalsum)


print "###########################################################################################"
