# auto increment in arcpy
red=0 
def Auto_Increment(): 
 global r 
 Start = 1  
 Interval = 1 
 if (r == 0):  
  r = Start  
 else:  
  r += Interval  
 return r
