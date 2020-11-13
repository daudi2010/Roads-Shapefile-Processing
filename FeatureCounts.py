#List  feature counts to a text file
import arcpy

arcpy.env.workspace = r"C:\TEMP\LocalGovernment.gdb"
outFile = open(r"C:\TEMP\dbinventory.txt", "a")

dsList = arcpy.ListDatasets(feature_type="feature")

for ds in dsList:
    outFile.write("Dataset: {0}{1}".format(ds, "\n"))
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        # If you only want features with rows > 0, update as follows:
        # rowCount = int(arcpy.GetCount_management(fc).getOutput(0))
        # http://gis.stackexchange.com/questions/55246/casting-arcpy-result-as-integer-instead-arcpy-getcount-management#
        # http://pro.arcgis.com/en/pro-app/arcpy/classes/result.htm
        rowCount = arcpy.GetCount_management(fc)
        outFile.write("{0}{1} has {2} records {3}".format("\t", fc, rowCount,
                                                                        "\n"))

outFile.close()
