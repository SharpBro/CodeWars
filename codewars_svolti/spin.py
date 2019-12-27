def spin_words(sentence):
        lista_parola = sentence.split()
    
        nuova_frase = ""
        for parola in lista_parola:
            if len(parola) >= 5:
                nuova_frase += ' ' + parola[::-1]
            else:
                nuova_frase += ' ' + parola
                flag = 1
        nuova_frase = nuova_frase[1:]
        return(nuova_frase)
                
            
    
print(spin_words("hey gay munz"))
