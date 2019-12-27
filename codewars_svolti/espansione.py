"""
The purpose of this kata is to write a program that can do some algebra. Write a function expand that takes in an expresion with a single, one character variable, and expands it. The expresion is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any one character long variable, and n is a natural number. If a = 1, no coeficient will be placed in front of the variable. If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients of the term, x is the original one character variable that was passed in the original expression and b, d, and f, are the powers that x is being raised to in each term and are in decreasing order. If the coeficient of a term is zero, the term should not be included. If the coeficient of a term is one, the coeficient should not be included. If the coeficient of a term is -1, only the "-" should be included. If the power of the term is 0, only the coeficient should be included. If the power of the term is 1, the carrot and power should be excluded.
Examples:

expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
expand("(-2a-4)^0")    # returns "1"
expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
expand("(r+0)^203")    # returns "r^203"
expand("(-x-1)^2")     # returns "x^2+2x+1"
"""



import string


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def coeff_bin(n,k):
    coeff = int(factorial(n) / (factorial(k) * factorial(n-k)))
    return coeff
    

def expand(expr):
    mappa_caratteri = string.ascii_lowercase
    
    "acquisizione variabile espressione"
    variabile = 'x'
    for elem in expr:
        for variab in mappa_caratteri:
            if elem == variab:
                variabile = elem
                break
        else:
            continue
        break
    "acquisizione coefficiente della variabile"
    
    if(expr[expr.find(variabile) - 1] == '-'):
           coeff = -1
    else:
        try:
            coeff = int(expr[expr.find('(') + 1:expr.find(variabile)])
        except:
            coeff = 1
    
    "acquisizione costante"
    costante = int(expr[expr.find(variabile)+1:expr.find(')')])
    
    
    "acquisizione potenza a cui l'espr e' elevata"
    to_power = int(expr[expr.find('^')+1:])
    
    #print(variabile,coeff, to_power)
    
    
    if to_power == 0:
        return "1"
    
    espansione = ""
    
    for k in range(0, to_power + 1):
        
        nuovo_coeff = coeff_bin(to_power,k)*(coeff**(to_power - k)) * (costante ** k)
        
        #print(nuovo_coeff)
        if k < to_power:
            if(nuovo_coeff > 0):
                if to_power - k == 1:
                    espansione += '+' + str(nuovo_coeff) + variabile
                else:
                    espansione += '+' + str(nuovo_coeff) + variabile + '^' + str(to_power - k)
            else:
                if to_power - k == 1:
                    espansione += str(nuovo_coeff) + variabile
                else:
                    espansione += str(nuovo_coeff) + variabile + '^' + str(to_power - k)
        
        elif k == to_power:
            if nuovo_coeff > 0:
                espansione += '+' + str(nuovo_coeff)
            else:
                espansione += str(nuovo_coeff)
    
    if(espansione[0] == '+'): #rimuovo il segno se positivo
        espansione = espansione[1:]
    if(espansione[0] == '1' and espansione[1] == variabile): #rimuovo inoltre l'uno se compare come coefficiente della variabile piu' a sinistra
        espansione = espansione[1:]
    if(espansione[0] == '-' and espansione[1] == '1' and espansione[2] == variabile):#se la variabile piu a sinistra ha come coefficiente 1
        espansione = '-' + espansione[2:]
    
    return espansione
    
    
                

expand("(-5m+3)^4")

"8x^3-36x^2+54x-27"

     
