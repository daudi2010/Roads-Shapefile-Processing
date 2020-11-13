import numpy as np
import csv
#FID,RdNum,RdClass,Shape_Leng,RdName
with open('fullcomp.csv') as csv_file:
    with open('full_registerChainage.csv', mode='w') as chainage_file:
        chainage_writer = csv.writer(chainage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        chainage_writer.writerow(['CID', 'RdNum', 'Chainage'])

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        lines = 0
        chainages=[]
        for row in csv_reader:
            #print row
            if line_count == 0:
                print('Columns'+ (", ".join(row)))
                line_count += 1
            else:
                #print row[1]
                if row[2] in ["A","B","C"]:
                    chainages=np.arange(start=0, stop=float(row[3]), step=5, dtype=float)
                else :
                    chainages=np.arange(start=0, stop=float(row[3]), step=1, dtype=float)
                 
                for chainage in chainages:
                    # intervals of 1000m=1km
                    
                    chainage_writer.writerow([lines, row[1], chainage*1000])
                    
                    line_count += 1
                    lines += 1
        print('Processed ' +str(line_count)+' lines.')
