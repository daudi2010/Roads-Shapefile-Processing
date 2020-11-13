###############################################################################################################
"""
This script  classifies Bridges,culverts, drifts Through selection by various ATTRIBUTES
and computes  the TOTAL SUM  per that criteria per type

Written by David Kanyari 
Email: daudi2010[at]gmail.com
You just need to declare  the input shapefiles 


November 2018
daudi2010@gmail.com
"""
#################################################################################################################
import arcpy, os
from datetime import datetime
arcpy.CheckOutExtension('Spatial')
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False

datestring=datetime.now().strftime('%d%m%Y')



#  Workspace
folders=r'E:\smec\smec_Both_Zones.gdb'
outDir=r'E:\smec\smec_Both_Zones.gdb'

# Define the feature classes to process
arch_culverts=os.path.join(folders,"DRAINAGE_STRUCTURES\Arch_Culvert")
bridges=os.path.join(folders,"DRAINAGE_STRUCTURES\Bridges")
pipe_culverts=os.path.join(folders,"DRAINAGE_STRUCTURES\Pipe_Culvert")
box_culverts=os.path.join(folders,"DRAINAGE_STRUCTURES\Box_Culvert")
drifts=os.path.join(folders,"DRAINAGE_STRUCTURES\Drifts")



# A dictionary to hold statistics
stat_dictionary={}
# Define your rationale

# Conditions
Poor=" IN('Poor')"
Good=" IN('Good')"
Fair=" IN('Fair')"
under_construction= "IN ('Under Construction', 'Under Constuction', 'Under Cosntruction')"

# Pipe culvert diameter in mm
casebelow600mm="Cul_Dia_mm <600"
case6to9m="Cul_Dia_mm >= 600 AND Cul_Dia_mm <= 900"
caseabove9m="Cul_Dia_mm > 900"

#Pipe culver diameter
CulSize_mm={"below600mm":casebelow600mm,"btn600to900mm":case6to9m,"above900mm":caseabove9m}

 # condition
condition={"Poor":Poor,"Good":Good,"Fair":Fair ,"under_construction":under_construction}

# Select by attributes and Export
Totalsum=0

print "Computing......."
if os.path.exists(folders):  # only folders (directories) in folders

             arcpy.env.workspace=folders
             arcpy.GetMessages()# empty

            # bridges

             print "###################  Bridges ##################################################"
             #  select By condition
             arcpy.MakeFeatureLayer_management(bridges, "lyr")
             result = arcpy.GetCount_management("lyr")
             count = int(result.getOutput(0))
             for key,value in condition.iteritems():

                 try:
                   valueb="SupStrCond  " +value
                   arcpy.SelectLayerByAttribute_management ("lyr", "NEW_Selection", valueb)
                   # Get count of the selected
                   result = int(arcpy.GetCount_management("lyr").getOutput(0))
                   Totalsum=Totalsum+result
                   print key + " Briges: {0} ".format(result)
                   stat_dictionary.update({"Bridges_"+key: result})

                 except:
                   print arcpy.GetMessages()
             print "Bridges Total :" + str(count)
                  # Pipe culverts
             print "###################  Pipe Culverts ##################################################"
             arcpy.MakeFeatureLayer_management(pipe_culverts, "lyr2")
             result = arcpy.GetCount_management("lyr2")
             count = int(result.getOutput(0))
             for keysize, valuesize in CulSize_mm.iteritems():
                    for keycon, valuecon in condition.iteritems():

                       try:
                           valueb = "Cul_Cond  " + valuecon

                           arcpy.SelectLayerByAttribute_management("lyr2", "NEW_Selection", valuesize + " AND " + valueb)
                           # Get count of the selected
                           result = int(arcpy.GetCount_management("lyr2").getOutput(0))
                           print keysize+"_"+keycon+ " Pipe culverts: {0} ".format(result)
                           stat_dictionary.update({"Pipe_Culverts_"+keysize + "_" + keycon: result})

                       except:
                           print arcpy.GetMessages()
             print "Pipe Culverts Total :" + str(count)
             # Box culverts
             print "###################  Box Culverts ##################################################"
             arcpy.MakeFeatureLayer_management(box_culverts, "lyr3")
             result = arcpy.GetCount_management("lyr3")
             count = int(result.getOutput(0))
             for keycon, valuecon in condition.iteritems():
                 try:
                     valueb = "Cul_Cond " + valuecon

                     arcpy.SelectLayerByAttribute_management("lyr3", "NEW_Selection", valueb)
                     # Get count of the selected
                     result = int(arcpy.GetCount_management("lyr3").getOutput(0))
                     print keycon + " Box culverts: {0} ".format(result)
                     stat_dictionary.update({"Box_Culverts_"+keycon: result})

                 except:
                     print arcpy.GetMessages()
             print "Box Culverts Total :" + str(count)
             # Drifts
             print "###################  Drifts ##################################################"
             arcpy.MakeFeatureLayer_management(drifts, "lyr4")
             result = arcpy.GetCount_management("lyr4")
             count = int(result.getOutput(0))

             for keycon, valuecon in condition.iteritems():
                 try:
                     valueb = "DriftCond " + valuecon

                     arcpy.SelectLayerByAttribute_management("lyr4", "NEW_Selection", valueb)
                     # Get count of the selected
                     result = int(arcpy.GetCount_management("lyr4").getOutput(0))
                     print keycon + " Drifts: {0} ".format(result)
                     stat_dictionary.update({"Drifts_"+keycon: result})

                 except:
                     print arcpy.GetMessages()
             print "Drifts Total :" + str(count)
             #Arch Culverts             
             print "###################  Arch Culverts ##################################################"
             arcpy.MakeFeatureLayer_management(arch_culverts, "lyr5")
             result = arcpy.GetCount_management("lyr5")
             count = int(result.getOutput(0))

             for keycon, valuecon in condition.iteritems():
                 try:
                     valueb = "Cul_Cond " + valuecon  

                     arcpy.SelectLayerByAttribute_management("lyr5", "NEW_Selection", valueb)
                     # Get count of the selected
                     result = int(arcpy.GetCount_management("lyr5").getOutput(0))
                     print keycon + " Arch Culverts: {0} ".format(result)
                     stat_dictionary.update({"Arch_Culverts_"+keycon: result})

                 except:
                     print arcpy.GetMessages()
             print "Arch Culverts Total :" + str(count)




                           
print "###########################################################################################"

print "Detailed Statistics"
for key,value in stat_dictionary.iteritems():
    print key +":"+str(value)
print

print "###########################################################################################"

print "Done"
