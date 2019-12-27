"""
A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

"""

def range_extraction(lista):
    
    lunghezza = len(lista) #calcolo della lunghezza della lista passata come parametro
    
    i = 0 #inizializzazione indice
    contatore = 0
    flag = False
    
    stringa = "" #stringa finale
    while i < lunghezza:#ciclo per consumare la lista
        contatore = 0#reimpostazione delle variabili flag e contatore alla loro condizione iniziale
        flag = False
        if i+1 < lunghezza and lista[i+1] == lista[i] + 1:#se l'elemento successivo della lista e' pari all'elemento attuale incrementato di uno e l'indice i non eccede la lunghezza della lista, allora:
            primo_el = lista[i]#assegna il primo elemento che soddisfa la condizione a primo_el
            while(lista[i+1] == lista[i] + 1):#ciclo per acquisire i numeri contigui

                contatore += 1
                if(contatore >= 2):#quando vi sono almeno tre numeri contigui
                    flag = True   #il flag e' impostato a 1
                i += 1
                if(i == lunghezza - 1):#qualora venisse raggiunta la fine della lista, il ciclo e' interrotto
                    break
                   
            if(flag == True):
                rang = "%d-%d" % (primo_el,lista[i])
                stringa += rang + ',' #range seguito da una virgola e' aggiunto alla stringa
                i += 1
            else:
                stringa += str(primo_el) + ','#altimenti e' aggiunto soltanto un elemento
        else:
            stringa += str(lista[i]) + ','
            i += 1
            
    return(stringa[:-1])#la stringa e' restituita eliminando l'ultimo carattere, che per come e' stato implementata la funzione, sara' sempre una virgola
    
range_extraction([-3,-2,-1,2,10,15,16,18,19,20])
                
            
