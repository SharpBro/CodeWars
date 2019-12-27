import string

def alphabet_position(text):
    #dictionaries
    lettere_minuscole = string.ascii_lowercase
    lettere_maiuscole =  string.ascii_uppercase
    
    stringa = ""
    
    for i in text:
        if i in lettere_maiuscole:
             stringa += " " + str(lettere_maiuscole.find(i) + 1)
        elif i in lettere_minuscole:
            stringa += " " + str(lettere_minuscole.find(i) + 1)
    
    stringa = stringa[1:] #to remove the first space character
    
    return stringa
        

stringa = "The sunset sets at twelve o' clock."

alphabet_position(stringa)
    
    
