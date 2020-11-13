import numpy as np
import csv
#FID,RdNum,RdClass,Shape_Leng,RdName
with open('register_km2.csv') as csv_file:
    with open('Chainage_1km_segments.csv', mode='w') as chainage_file:
        chainage_writer = csv.writer(chainage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        chainage_writer.writerow(['CID', 'RdNum','Rd_Class',"chainageID",'Rdname',"FromM","ToM"])

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        lines = 0
        chainages=[]
        for row in csv_reader:
            #print row
            if line_count == 0:
                print('Columns  '+ (", ".join(row)))
                line_count += 1
            else:
                chainageValue= round (float(row[3]),2)
                if float(row[3]) >= 2:
                    chainages=np.arange(start=0, stop= float(round(float(row[3])*1000,3)), step=1000, dtype=float)
                elif float(row[3]) < 2:
                   
                    chainages=np.arange(start=0, stop=float(round(float(row[3])*1000,3)), step=200, dtype=float)
            
                else:
                    
                    chainages=np.arange(start=0, stop=float(round(float(row[3])*1000,3)), step=200, dtype=float)
                for i in range(len( chainages)):
                      # intervals of 1000m=1km
                       try:
                             chainage_writer.writerow([lines, row[0],row[1], row[0]+"_"+str(chainages[i]/1000)+"-"+str(chainages[i+1]/1000),
                                                        row[2].upper(),chainages[i]/1000,chainages[i+1]/1000])

                       except IndexError:
                             chainage_writer.writerow([lines, row[0],row[1], row[0]+"_"+str(chainages[i]/1000)+"-"+str(chainageValue),
                                                        row[2].upper(),chainages[i]/1000,chainageValue])

                       line_count += 1
                       lines += 1
        print('Processed ' +str(line_count)+' lines.')
