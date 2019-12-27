import itertools as it
 
def middle_permutation(string):
    lista = list(it.permutations(string))
       
    altra_lista = []
    
    for elem in lista:
        conversione = ''.join(elem)
        if not conversione in altra_lista:
            altra_lista.append(conversione)
    
    altra_lista = sorted(altra_lista)

    return altra_lista[int(len(altra_lista)/2) - 1]



print(middle_permutation("abcd"))
