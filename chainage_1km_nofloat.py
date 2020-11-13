import numpy as np
import csv
#FID,RdNum,RdClass,Shape_Leng,RdName
with open('RegisterV2.csv') as csv_file:
    with open('NetworkChainagesFeb2020.csv', mode='w') as chainage_file:
        chainage_writer = csv.writer(chainage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        chainage_writer.writerow(['CID', 'RdNum','Rd_Class',"chainageID",'Rdname','Chainage','CName'])

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
                               
                if float(row[3]) >= 2000:
                    chainages=np.arange(start=0, stop= float(round(float(row[3]),2)), step=1000, dtype=float)
                elif float(row[3]) < 2000:
                    #print (row[1]+" : "+str(row[3]))
                    chainages=np.arange(start=0, stop=float(round(float(row[3]),3)), step=200, dtype=float)
            
                else:
                    #print (row[1]+" : "+str(row[3]))
                    chainages=np.arange(start=0, stop=float(round(float(row[3]),3)), step=200, dtype=float)
                for chainage in chainages:
                    # intervals of 1000m=1km
                    if chainage !=0:# eliminate zero chainage
                       chainage_writer.writerow([lines, row[0],row[1], row[0]+"_0+"+str(chainage/1000),row[2].upper(),chainage,chainage/1000])
                       line_count += 1
                       lines += 1
        print('Processed ' +str(line_count)+' lines.')
