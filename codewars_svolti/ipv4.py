def int_to_bin_four_bytes(number):
    num = [None]*32 
    
    for i in range(0,32):
            num[i] = 0
    
    temp = number
       
    i = 0
    while temp > 0:
        resto = temp % 2
        num[32 - i - 1] = resto
        temp = int(temp / 2) #su Codewars castava temp come float nella divisione e si buggava
        i += 1
        
    return num
        

def int32_to_ip(int32):
    
    convers_to_bin = int_to_bin_four_bytes(int32)
    convers_to_bin = ''.join(str(elem) for elem in convers_to_bin)
    
    
    num_car = 8
    
    lista = []
    for i in range(0,32,num_car):
        lista.append(convers_to_bin[i:i+num_car])
    
    
    for i in range(0, len(lista)):
        lista[i] = (int(lista[i], 2))

    punto = "."
    stringa_ip = punto.join(str(elem) for elem in lista)
    print(stringa_ip)
    
    return stringa_ip
    

#print(int32_to_ip(0))

print(int_to_bin_four_bytes(1961541656))

