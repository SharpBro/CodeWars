from string import *
def missing(array):
    stringa = ascii_letters
    inizio = stringa.index(array[0])
    fine = stringa.index(array[len(array) - 1])
    
    j = 0
    for i in range(inizio, fine + 1):
        if(array[j] != stringa[i]):
            return(stringa[i])
            break
        j += 1
        
    
    
missing(['a','b','c','d','f'])
missing(['O','Q','R','S'])
        
        
