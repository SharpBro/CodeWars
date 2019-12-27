"""
Let be n an integer prime with 10 e.g. 7.

1/7 = 0.142857 142857 142857 ....

We see that the decimal part has a cycle: 142857. The length of this cycle is 6. In the same way:

1/11 = 0.09 09 09 .... Cycle length is 2.
Task

Given an integer n (n > 1), the function cycle(n) returns the length of the cycle if n and 10 are coprimes, otherwise returns -1.
Exemples:

cycle(5) = -1
cycle(13) = 6 -> 0.076923 076923 0769
cycle(21) = 6 -> 0.047619 047619 0476
cycle(27) = 3 -> 0.037 037 037 037 0370
cycle(33) = 2 -> 0.03 03 03 03 03 03 03 03
cycle(37) = 3 -> 0.027 027 027 027 027 0
cycle(94) = -1 

cycle(22) = -1 since 1/22 ~ 0.0 45 45 45 45 ...
"""
    
def gcd(a,b):
    while a % b != 0:
        a, b = b, a % b
    return b



"""
dalla pagina http://mathworld.wolfram.com/FullReptendPrime.html

 A prime p for which 1/p has a maximal period decimal expansion of p-1 digits. Full reptend primes are sometimes also called long primes (Conway and Guy 1996, pp. 157-163 and 166-171). There is a surprising connection between full reptend primes and Fermat primes.

A prime p is full reptend iff 10 is a primitive root modulo p, which means that
10^k=1 (mod p) 	
(1)

for k=p-1 and no k less than this. In other words, the multiplicative order of p (mod 10) is p-1. For example, 7 is a full reptend prime since (10^1,10^2,10^3,10^4,10^5,10^6)=(3,2,6,4,5,1) (mod 7).

The full reptend primes are 7, 17, 19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 167, ... (OEIS A001913). 
ad es:
1/7 = 0.142857 142857
e phi(7) = 6
"""

def best_phi(n): 
      
    # inizializzazione di phi
    phi = n;  
  
    # tutti i fattori primi di n 
    # e sottrazione dei suoi multipli
    # da phi
    p = 2;  
    while(p * p <= n): 
          
        # verifica che p sia coprimo con n
        if (n % p == 0):  
            # se si, aggiorna il valore di n e phi
            while (n % p == 0): 
                n = n // p; 
            phi -= phi // p; 
        p += 1; 
  
    # se n possiede un fattore primo maggiore della sua radice quadrata
    # (al massimo 1) 
    if (n > 1): 
        phi -= phi // n; 
    return phi; 


def cycle(n) :
    if n % 2 == 0 or n % 5 ==0:
        return -1
    k = 1
    while pow(10,k,n) != 1:
        k += 1
    return k


