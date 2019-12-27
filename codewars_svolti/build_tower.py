""" Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

    Python: return a list;
    JavaScript: returns an Array;
    C#: returns a string[];
    PHP: returns an array;
    C++: returns a vector<string>;
    Haskell: returns a [String];
    Ruby: returns an Array;

Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]

and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
"""

def tower_builder(n_floors):
    lista = []
    zero_floor_dim = 2 * n_floors - 1 #dimensione base triangolo
    
    stringa = ""
    dim = 1
    
    #riempimento lista con asterischi
    for j in range(0, n_floors):
        for i in range(0, dim):
            stringa += "*"
        dim += 2
        lista.append(stringa)
        stringa = ""
    
    lung_stringa = 2 * n_floors - 1
    
    #aggiunta giustificazione ai lati degli asterischi
    for i in range(0, n_floors):
        
        str_len = len(lista[i]) + int(lung_stringa/2)
    
        lista[i] = lista[i].ljust(str_len)
    
        str_len = len(lista[i]) + int(lung_stringa/2)
    
        lista[i] = lista[i].rjust(str_len)
        
        lung_stringa -= 2
    
    
    return lista

tower_builder(4)
