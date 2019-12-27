def not_primes(a, b):
    
    lsa = ['2', '3', '5', '7']#caratteri accettabili
    
    flag = 0
    
    num_non_primi = []
    
    for i in range(a, b):
        flag = 0
        if is_prime(i) == False:#se il numero non e' primo
            num_in_str = str(i)#converto in stringa
            for car in num_in_str:
                if car not in lsa:#se la cifra non e' accettabili
                    flag = 1#il flag e' portato a 1
                    break
            if flag == 0:
                num_non_primi.append(i)#altrimenti il numero va salvato in num_non_primi
    return num_non_primi


def is_prime(n):
    
    if (n == 2 or  n == 3):
        return True;
    if (n % 2 == 0 or n % 3 == 0):
        return False;

    i = 5;
    w = 2;

    while (i * i <= n):
        if (n % i == 0):
            return False;
        i += w;
        w = 6 - w;

    return True;
    


print(not_primes(2700,3500))
