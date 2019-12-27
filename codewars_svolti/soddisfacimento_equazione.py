from itertools import permutations
"""
dati 4 valori, stabilire se e' possibile ottenere il numero 24 attraverso operazioni elementari e parentesizzazione: +,-,*,/
ad esempio dati 1,2,3,4 e' possibile ottere 24 come 1*2*3*4

"""

def prova(a,b,c,d):#protipo funzione; riceve in igresso 4 variabili intere 
    permut = list(permutations([a,b,c,d]))#calcolo di tutte le possibili permutazioni dei quattro numeri
    permut = set(permut)#si eliminano le copie
    oper = ['+','-','*', '/']#una lista contenente gli operatori 
    contatore = [0,0,0]#una lista per contenere gli indici che andranno ad indicare quale operatore deve essere selezionato
    array = []#una lista vuota per contenere una copia di contatore
    
    listatot = []#la lista finale contenente tutti gli indici da 0 a 4**i - 1 con i il numero di operatori
    for i in range(4**3 - 1):#3 operatori per un'operazione con 4 variabili
        contatore[0] += 1#si incrementa costantemente di 1 il contatore
        for j in range(3):
            if contatore[j] == 4:
                contatore[j+1] += 1
                contatore[j] = 0
    
        array = contatore[:]#copia del contatore
        listatot.append(array)#si aggiunge alla listatot il nuovo elemento
    
    for elem in permut:#ciclo per tutte le possibili permutazioni delle variabili in ingresso
     
     for j in range(len(listatot)):#ciclo per tutti i modi con i quali puo essere scritta l'operazioni
            stringa = "{}{}{}{}{}{}{}".format(float(elem[0]),oper[listatot[j][2]],float(elem[1]),oper[listatot[j][1]],float(elem[2]),oper[listatot[j][0]],float(elem[3]))
            try:
                res = eval(stringa)#si valuta l'espressione con la funzione eval()
                if res == 24:#se l'equazione e' verificata
                    stringa = stringa.replace('.0','')#elimino dalla stringa i decimali che si presentano dalla conversione attuata con format
                    return (stringa)
            except ZeroDivisionError:#qualora si divida per zero
                pass
            stringa = "({}{}{}){}({}{}{})".format(float(elem[0]),oper[listatot[j][2]],float(elem[1]),oper[listatot[j][1]],float(elem[2]),oper[listatot[j][0]],float(elem[3]))
            try:
                res = eval(stringa)
                if res == 24:
                    stringa = stringa.replace('.0','')
                    return (stringa)
            except ZeroDivisionError:
                pass
            stringa = "({}{}{}{}{}){}{}".format(float(elem[0]),oper[listatot[j][2]],float(elem[1]),oper[listatot[j][1]],float(elem[2]),oper[listatot[j][0]],float(elem[3]))
            try:
                res = eval(stringa)
                if res == 24:
                    stringa = stringa.replace('.0','')
                    return stringa
            except ZeroDivisionError:
                pass
            stringa = "{}{}({}{}{}{}{})".format(float(elem[0]),oper[listatot[j][2]],float(elem[1]),oper[listatot[j][1]],float(elem[2]),oper[listatot[j][0]],float(elem[3]))
            try:
                res = eval(stringa)
                if res == 24:
                    stringa = stringa.replace('.0','')
                    return stringa
            except ZeroDivisionError:
                pass
            
    #arrivati a questo punto non vi sono ulteriori controlli e si puo' concludere che non e' possibile ottenere 24 con le variabili assegnate
    return("It's not possible!")
for i in range(0,20):
    print(prova(i,i+2,i+4,i+7))
