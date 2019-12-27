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

print(best_phi(33500000000))
