"""
Introduction

The ragbaby cipher is a substitution cipher that encodes/decodes a text using a keyed alphabet and their position in the plaintext word they are a part of.

To encrypt the text This is an example. with the key cipher, first construct a keyed alphabet:

c    i    p    h    e    r    a    b    d    f    g    j    k    l    m    n    o    q    s    t    u    v    w    x    y    z

Then, number the letters in the text as follows:

T    h    i    s         i    s         a    n         e    x    a    m    p    l    e    .
1    2    3    4         1    2         1    2         1    2    3    4    5    6    7     

To obtain the encoded text, replace each character of the word with the letter in the keyed alphabet the corresponding number of places to the right of it (wrapping if necessary). Non-alphabetic characters are preserved to mark word boundaries.

Our ciphertext is then Urew pu bq rzfsbtj.
Task

Wirate functions encode and decode which accept 2 parameters:

    text - string - a text to encode/decode
    key - string - a key

Notes

    handle lower and upper case in text string
    key consists of only lowercase characters


"""
import string

def encode(text, key):
    alfab = list(string.ascii_lowercase) #alfabeto lettere minuscole
    temp = list(key)#conversione della chiave in lista
    
    new_alfa= []
    for elem in temp:   
                    
        if elem not in new_alfa:#se il carattere i-esimo della chiave non e' presente all'interno di new_alfa, viene salvato
            new_alfa.append(elem)
            
    for elem in alfab:
        if elem not in new_alfa:
            new_alfa.append(elem)#vengono aggiunti i restanti caratteri dell'alfabeto
    
    contatore = 1
    flag = 0
    stringa = ""
    
    for elem in text:
        flag = 0
        
        if elem.isupper() == True:#caso in cui il carattere sia in maiuscolo
            flag = 1
        if elem not in alfab and flag == 0:
            contatore = 1 #il contatore e' azzerato
            stringa += str(elem)#il carattere e'aggiunto alla stringa
        else:
            if(flag == 1):
                elem = elem.lower()#conversione del carattere in minuscolo
            pos = (new_alfa.index(elem) + contatore) % len(new_alfa)#la posizione sara data dall'indice dell'alfabeto new_alfa incrementato di contatore posti; per gestire parole piu lunghe dell'alfabeto e' utilizzato l'operatore modulo, che restituisce il primo carattere dell'alfabeto dopo lung_alfabeto caratteri
            
            if(flag == 1):
                stringa += str(new_alfa[pos]).upper() # alla string e' aggiunto il carattere cifrato convertito in maiuscolo
            
            else:
                stringa += str(new_alfa[pos])
            contatore += 1 #il contatore e' incrementato
    
    return(stringa)
            


def decode(text, key):
    
    alfab = list(string.ascii_lowercase)
    temp = list(key)
    
    new_alfa= []
    for elem in temp:
                   
        if elem not in new_alfa:
            new_alfa.append(elem)
            
    for elem in alfab:
        if elem not in new_alfa:
            new_alfa.append(elem)
    
    contatore = 1
    flag = 0
    stringa = ""
    
    for elem in text:
        flag = 0
        
        if elem.isupper() == True:
            flag = 1
        if elem not in alfab and flag == 0:
            contatore = 1
            stringa += str(elem)
        else:
            if(flag == 1):
                elem = elem.lower()
            pos = (new_alfa.index(elem) - contatore) % len(new_alfa)#l'unica differenza con la funzione di codifica e' che la posizione del carattere non cifrato sara data dalla differenza dell'indice del carattere all'interno dell'alfabeto e il contatore
            
            if(flag == 1):
                stringa += str(new_alfa[pos]).upper()
            
            else:
                stringa += str(new_alfa[pos])
                
            contatore += 1

    return stringa

    
