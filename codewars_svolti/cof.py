def is_prime(num):    
    if (num == 2 or num == 3):
        return True;
    if (num % 2 == 0 or num % 3 == 0):
        return False;

    i = 5;
    w = 2;

    while (i * i <= num):
        if (num % i == 0):
            return False;
        i += w
        w = 6 - w
    

    return True


print(is_prime(44))
    
