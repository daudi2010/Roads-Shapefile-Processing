def computeClass(Rdnum2):
    
    st= Rdnum2[0].upper()
    c=""
    splitR= Rdnum2.split('_')
    
    if "N" in splitR:
        c="NEW"
    if "NEW" in Rdnum2:
         
         c="NEW"
    
    if "NR" in Rdnum2 :
         c="NR"
      
    elif "A2S" in Rdnum2 :
         c="S"
    else:
         if "N" in splitR:
             c="NEW"
         if "NEW" in Rdnum2:
         
             c="NEW"
            
         elif st =='H':
             c="Au"
         elif st =='H':
             c="Au"
         elif st =='J':
             c="Bu"
         elif st =='K':
             c="Cu"
         elif st =='L':
             c="Du"
         elif  st =='M':
             c="Eu"
         elif st =='N':
             c="Fu"
         elif "NR" in Rdnum2 :
              c="NR"
         elif st =='P':
             c="Gu"
         
         elif st =='U':
             if "UCB" in Rdnum2 :
                 c="Bu"
             elif "UCA" in Rdnum2 :
                 c="Au"
             else:
               c='Au'
         else:
             if "N" in splitR:
                 c="NEW"
             elif "NEW" in Rdnum2:
         
                 c="NEW"
    
             elif  "NR" in Rdnum2 :
                 c="NR"
             else :#st in['A','B','C','D','E','F','G']:
                 c=st
    return c     

for a in ["A4","k7_Nakuru","D_22_N_6075","UCB3_nakuru",
          "UCB10-Mombasa","G_NEW_788","NR_6_78","UUCB19",
          "C234","L23-Kisumu","A2S","E_N_3456"]:
  print computeClass(a)
  print a
  print a.split('_')
  print        
                            
