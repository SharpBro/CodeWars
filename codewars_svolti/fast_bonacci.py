import time
from numpy import matrix

def fib_con_matrice(n):
    return (matrix(
        '0 1; 1 1' if n >= 0 else '-1 1; 1 0', object
        ) ** abs(n))[0, 1]

def fibonacci(n):#la funzione calcola anche l'ennesimo negativo mediante la formula F -n = (-1)^(n+1) F n dove Fn e' l'ennesimo numero positivo di fibonacci
    if n < 0:
        if (n+1)%2 != 0:
            return -1 * _fibspeed(abs(n))[0]
        else:
            return _fibspeed(abs(n))[0]
            
    return _fibspeed(n)[0]


def _fibspeed(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fibspeed(int(n / 2))
        c = a * (2 * b - a)
        d = a**2 + b**2
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

start_time = time.time()
a = fibonacci(20000)
print(a, len(str(a)))
print("--- %s seconds ---" % (time.time() - start_time))
