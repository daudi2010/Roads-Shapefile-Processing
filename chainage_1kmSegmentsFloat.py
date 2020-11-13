import numpy as np
import csv
#FID,RdNum,RdClass,Shape_Leng,RdName
with open('RevisedROUTESNOV25.csv') as csv_file:
    with open('Revised_Chainage_1km_segments_Nov25.csv', mode='w') as chainage_file:
        chainage_writer = csv.writer(chainage_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        chainage_writer.writerow(['CID', 'RdNum','Rd_Class',"chainageID",'Rdname',"FromM","ToM"])

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        lines = 0
        chainages=[]
        for row in csv_reader:
            #print row
            if line_count == 0:
                print('Columns \n'+ (", ".join(row)))
                line_count += 1
            else:
                b=float(row[3])
                #print float(row[3])
                chainageValue= b
                if b >= 2000:
                    chainages=np.arange(start=0, stop= float(round(b,2)), step=1000, dtype=float)
                elif float(row[3]) < 2000 and float(row[3])>=200:
                   
                    chainages=np.arange(start=0, stop=float(round(float(row[3]),3)), step=200, dtype=float)
                elif float(row[3]) < 200:
                   
                    chainages=np.arange(start=0, stop=float(round(float(row[3]),3)), step=int(float(row[3])), dtype=float)

                else:
                    
                    chainages=np.arange(start=0, stop=float(round(float(row[3]),3)), step=int(float(row[3])), dtype=float)
                for i in range(len( chainages)):
                      # intervals of 1000m=1km
                       try:
                             chainage_writer.writerow([lines, row[0],row[1], row[0]+"_"+str(chainages[i]/1000)+"-"+str(chainages[i+1]/1000),
                                                        row[2].upper(),chainages[i],chainages[i+1]])

                       except IndexError:
                             chainage_writer.writerow([lines, row[0],row[1], row[0]+"_"+str(chainages[i]/1000)+"-"+str(chainageValue),
                                                        row[2].upper(),chainages[i],chainageValue])

                       line_count += 1
                       lines += 1
        print('Processed ' +str(line_count)+' lines.')
