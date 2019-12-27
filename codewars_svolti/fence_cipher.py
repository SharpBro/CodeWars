import numpy as np
"""
Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string. You can optionally include or dis-include punctuation.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    

The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN

Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. Don't filter out the punctuation as they are a part of the string.

"""
def encode_fence_cipher(stringa,num_partizioni):
    
    lung = len(stringa)
    
    lista_partiz = [[] for elem in range(num_partizioni)]
    
    crescita = 1
    posiz = 0
    
    for i in range(lung):
        
        lista_partiz[posiz].append(stringa[i])
        
        if(crescita == 1):
            posiz += 1
        elif(crescita == 0):
            posiz -= 1
        
        if(posiz == num_partizioni - 1):
            crescita = 0
        elif(posiz == 0):
            crescita = 1
    
    cifrato = ""
    
    for elem in lista_partiz:
        cifrato += ''.join(elem)
        
    return(cifrato)

def decode_fence_cipher(messaggio, num_partizioni):
    
    lung = len(messaggio)
    matrice = np.zeros(shape =(num_partizioni, len(messaggio)), dtype = int)
    crescita = 1
    posiz = 0
    
    lista_partiz = [[] for elem in range(num_partizioni)]
    
    for i in range(lung):
        
        matrice[posiz][i] = 1
        
        if(crescita == 1):
            posiz += 1
        elif(crescita == 0):
            posiz -= 1
        
        if(posiz == num_partizioni - 1):
            crescita = 0
        elif(posiz == 0):
            crescita = 1
    
    posizione = 0
    for j in range(num_partizioni):
        messaggio = messaggio[posizione:]
        for i in range(lung):
            if(matrice[j][i] == 1):
                lista_partiz[j].append(messaggio[posizione])
                messaggio = messaggio[1:]
    
    
    crescita = 1
    posiz = 0
    decodifica = ""
    for i in range(lung):
        
        decodifica += str(lista_partiz[posiz].pop(0))
        
        if(crescita == 1):
            posiz += 1
        elif(crescita == 0):
            posiz -= 1
        
        if(posiz == num_partizioni - 1):
            crescita = 0
        elif(posiz == 0):
            crescita = 1
                
                
    return(decodifica)
    

print(encode_fence_cipher("messaggiosegretosupermega", 4))

print(decode_fence_cipher("mgrpaegigeuegsaoetsressom",4))
