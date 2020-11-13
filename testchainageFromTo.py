
import numpy as np
chainage=[0,1,2,4,5,5,8,9,12,90,145]
last=150
#chainage=np.arange(start=0, stop= float(round(float(100.3)*1000,3)), step=1000, dtype=float)
print (chainage)
for i in  range(len(chainage)):
      print (i)
     
      try:
             print (str(chainage[i] )+"-"+str(chainage[i+1]))
      except IndexError:
             print (str(chainage[i] )+"-"+str(last))
          
