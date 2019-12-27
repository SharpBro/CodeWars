"""
The Caesar cipher is a notorious (and notoriously simple) algorithm for encrypting a message: each letter is shifted a certain constant number of places in the alphabet. For example, applying a shift of 5 to the string "Hello, world!" yields "Mjqqt, btwqi!", which is jibberish.

In this kata, your task is to decrypt Caesar-encrypted messages using nothing but your wits, your computer, and a set of the 1000 (plus a few) most common words in English in lowercase (made available to you as a preloaded variable named WORDS, which you may use in your code as if you had defined it yourself).
Given a message, your function must return the most likely shift value as an integer.

A few hints:

    Be wary of punctuation
    Shift values may not be higher than 25


"""




import string
def cesare(messaggio, shift):
    alfa_min = string.ascii_lowercase
    alfa_max = string.ascii_uppercase
    
    stringa = ""
    
    for elem in messaggio:
        if elem in alfa_min:
            stringa += alfa_min[(alfa_min.index(elem) + shift) % 26]
        elif elem in alfa_max:
            stringa += alfa_max[(alfa_max.index(elem) + shift) % 26]
        else:
            stringa += elem
            
    return stringa

def test_trans(s):
    table = str.maketrans({key: None for key in string.punctuation})
    new_s = s.translate(table) 
    return new_s

def break_caesar(message):
    
    #with open("parole.txt") as f:
        #WORDS = f.read().split()
        
    
    
    message = test_trans(message)
    
    lista_parole = message.split()
    shift_value = 0
    probabilita = 0.0
    parole_in_testo = len(lista_parole)
    parole_riconosciute = 0
    massimo = 0
    temp_shift = 0
    flag = 0
    
    for i in range(0, 26):
        
        probabilita = 0.0
        parole_riconosciute = 0
        
        for parola in lista_parole:
            parola_cifrata = cesare(parola, i)
            parola_cifrata = parola_cifrata.lower()
            #print(parola_cifrata, end = ' ')
            if parola_cifrata in WORDS:
                parole_riconosciute += 1
        
        probabilita = parole_riconosciute/parole_in_testo
        
        #print(parole_riconosciute, parole_in_testo, probabilita)
        
        if probabilita >= 0.5:
            shift_value = i
            flag = 1
            break 
        elif probabilita < 0.5 and probabilita > 0:
            massimo = probabilita
            temp_shift = i
            
    if flag == 0:
        shift_value = temp_shift
    
    if shift_value == 0:
        return 0
    
    return 26 - shift_value
    
print(break_caesar("Mjqqt, btwqi!"))
