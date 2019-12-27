import re
import time


def good(string):
    charRe = re.compile(r'[^01689]')
    string = charRe.search(string)
    return not bool(string)

def upside(start,end):
    
    contatore = 0
    cifre_valide = set([0,1,6,8,9])
    
    
    for i in range(start,end+1):
        temp = str(i)
        
        if good(temp) == False:
            continue
        else:
            nuovo_num = ""
            for car in temp:
                if car == '6':
                    nuovo_num += '9'
                elif car == '9':
                    nuovo_num += '6'
                else:
                    nuovo_num += car
            
            if nuovo_num == temp[::-1]:
                #print(nuovo_num)
                contatore += 1
                
    return(contatore)


start_time = time.time()

print(upside(0,300))

print("--- %s seconds ---" % (time.time() - start_time))
