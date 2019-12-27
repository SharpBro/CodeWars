import hashlib
import itertools

"""
la funzione restituisce le permutazioni della stringa data in una lista
"""
def permutazioni(string):
    lista_perm = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [lista_perm.append(char + a) for a in permutazioni(string.replace(char, ""))]
    return lista_perm

"""
la funzione attacca la stringa chars e restituisce la stringa originaria
"""
def sha256_cracker(hash, chars):
    
    permut = permutazioni(chars)#calcola le permutazioni della stringa
    permut = set(permut)#i duplicati sono eliminati con set
    permut = list(permut)#riconversione a lista 
    
    hashes = []
    for elem in permut:
        elem = elem.encode('utf-8')#codifica in utf-8 dell elemento
        hashes.append(hashlib.sha256(elem).hexdigest())#calcolo lo sha256 dell elemento di permut
    
    for el in hashes:#ricerca di una corrispondenza tra gli hash generati
        if el == hash:
            return permut[hashes.index(el)]#restituisce la stringa nella lista permut trovata all'indice el-esimo
    
    return None#se la stringa non e' stata trovata, restituisce none
        
    
print(sha256_cracker('f58262c8005bb64b8f99ec6083faf050c502d099d9929ae37ffed2fe1bb954fb', 'abc'))
