def thirt(n):
    modul = [1, 10, 9, 12, 3, 4]
    
    
    nuovo_numero = n
    
    while True:
        num = str(nuovo_numero)
        num = num [::-1]#invert the number
    
        somma = 0
    
        i = 0
    
        for elem in num:
            somma += int(elem) * modul[i % 6]
            i += 1
        
        #print(somma)
        if(nuovo_numero != somma):
            nuovo_numero = somma
        else:
            break
        
    return somma
    


risultato = thirt(321)

print(risultato)
