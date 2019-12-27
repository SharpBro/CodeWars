def prova(ext_inf, ext_sup):
     
    contatore = 0
    
    for i in range (ext_inf, ext_sup+1): 
        stringa =  "{0:b}".format(i)
        contatore += stringa.count('1')
    
    return contatore



print(prova(0,16))
