from math import *

#Lagrange's four-square theorem, also known as Bachet's conjecture, states that every natural number can be represented as the sum of four integer squares. 

def perf_square(n):
        sq = int(sqrt(n))
        return sq*sq == n

def numSquares(n):
        # Lagrange's four-square theorem
        if perf_square(n):
            return 1
        while (n & 3) == 0:
            n >>= 2
        if (n & 7) == 7:
            return 4
        sq = int(sqrt(n)) + 1
        for i in range(1,sq):
            if perf_square(n - i*i):
                return 2
        return 3


def somma_quad(num):
    
    x = num
    contatore = 0
    while(x >= 1):
        radice = sqrt(x)#calcola la radice quadrata di x
        radice = floor(radice)#acquisisce l'intero immediatamente piu grande
        radice = pow(radice,2)#il quadrato di radice
        print(int(radice))
        x = x - radice#sottrae radice alla x(ovvero un quadrato che lo costituisce)
        contatore += 1
        
    
    
    print(contatore)
    
#somma_quad(18)
print(numSquares(100))
