def format_duration(valore):
    anno = 0
    giorno = 0
    ora = 0
    minu = 0
    sec = 0
    
    while(valore - 31536000 >= 31536000):
        valore -= 31536000
        anno += 1
    while(valore - 86400 >= 86400):
        valore -= 86400
        giorno += 1
    while(valore - 3600 >= 3600):
        valore -= 3600
        ora += 1
    while(valore - 60 >= 60):
        valore -= 60
        minu +=1
    
    sec = valore
    
    while(sec >= 60):
        sec -= 60
        minu += 1
    while(minu >= 60):
        minu -= 60
        ora += 1
    while(ora >= 24):
        ora -= 24
        giorno += 1
    while(giorno >= 365):
        giorno -= 365
        anno += 1
    
    
        
format_duration(365376642)
        
