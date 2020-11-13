# Move folders form one folder to Another
import os
import shutil
#check if directory exists
#print os.path.isdir("/home/el")
#origin directory
rootpath="D:\\RAWFILES\\RICS DATA DOWNLOAD"
rootpath2="D:\\RICS2016\\KAJIADOKRBSHAPEFILES"
#Destination  path
dest_path="D:\\RICS2016\\Photo2"

paths=[rootpath,rootpath2]
# loop and move
for path in paths:
    print path
    for root, dirs, files in os.walk(path):
       for name in dirs:
        #print name
        if name.endswith(('~files', 'files')):
            #print name
            print os.path.join(root, name)
            dirx=os.path.join(root, name)
            dirx2=os.path.join(dest_path, name)
            if not os.path.exists(dirx2):
                shutil.move(dirx, dest_path)
                print "moved : "+dirx
