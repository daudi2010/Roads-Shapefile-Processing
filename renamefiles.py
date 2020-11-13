import os
import shutil
root="D:\\RICS2016\\KAJIADOKRBSHAPEFILES\\DAY1-DAY5-Combined\\reprojectedWGS84"
destination="D:\\RICS2016\\KAJIADOKRBSHAPEFILES\\DAY1-DAY5-Combined\\reprojectedWGS84\\allfiles"
for filename in os.listdir(root):
    name=filename.split(".")
    if len(name)>2:
        
       newfilename=name[0].replace('_merged_19102016', '')+"."+name[1]+"."+name[2]
       shutil.copy2(os.path.join(root,filename), os.path.join(destination,newfilename))
    if len(name)==2:
       newfilename=name[0].replace('_merged_19102016', '')+"."+name[1] 
       shutil.copy2(os.path.join(root,filename), os.path.join(destination,newfilename))
    else:
        print " no file to rename:"
    print name

    
    #print newfilename
    
os.listdir("D:\\RICS2016\\KAJIADOKRBSHAPEFILES\\DAY1-DAY5-Combined\\reprojectedWGS84\allfiles")
    
