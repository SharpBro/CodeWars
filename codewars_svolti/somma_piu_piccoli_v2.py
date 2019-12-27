def sum_two_smallest_numbers(numbers):
    
    numeri_ordinati = sorted(numbers)
    
    somma = numeri_ordinati[0] + numeri_ordinati[1]
    
    return somma
    
    


array = [25, 42, 12, 18, 22]


print(sum_two_smallest_numbers(array))
