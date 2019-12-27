

def Kapracane(num):
    
    iterazioni = 0
    
    while(num != 6174):
    
        stringa_1 = str(num)
        stringa_2 = str(num)
    
        stringa_1 = sorted(stringa_1, reverse = True)
        stringa_2 = sorted(stringa_2)
        
        stringa_1 = ''.join(stringa_1)
        stringa_2 = ''.join(stringa_2)
   
        num = int(stringa_1) - int(stringa_2)
        
        print(num)
        
        iterazioni += 1
        
    
    return iterazioni


ingresso = raw_input("inserisci il cazzo di capracane: ")

try:
    ingresso = int(ingresso)
except:
    print("coglione, inserisci un dato valido")
    exit(1)
    
cazz = Kapracane(ingresso)

print("num. iterazioni: %d" %(cazz))

