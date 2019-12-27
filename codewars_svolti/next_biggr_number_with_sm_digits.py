"""You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071

If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1

"""

import itertools


def next_bigger(n):
    num_lista = [int(cifra) for cifra in str(n)] 
    perm = list(itertools.permutations(num_lista))
    lista_nuova = []
    for elem in perm:
        if elem not in lista_nuova:
            lista_nuova.append(elem)
    
    lista_nuova = sorted(lista_nuova)
    lista_nuova = [int(''.join(map(str,elem))) for elem in lista_nuova]
    
    indice = lista_nuova.index(n)
    if(indice == len(lista_nuova) - 1):
        return -1
    else:
        return lista_nuova[indice + 1]
    



num = next_bigger(454646545)

print(num)
