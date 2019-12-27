from math import pi
def iter_pi(epsilon):
    calc_pi = 0
    k = 0
    while(abs(4*calc_pi - pi) > epsilon):
        calc_pi += (-1)**k/float(2*k + 1.0)
        k += 1
    return [k, round(4*calc_pi,10)]
    
    
    
    
    
print(iter_pi(0.0001))
