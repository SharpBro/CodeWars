def sum_two_smallest_numbers(numbers):
    
    somma = 0
    temp = 0
    
    for i in range(0, len(numbers)):
        
        temp = 0
        
        for j in range (i + 1, len(numbers)):
            
            temp = numbers[i] + numbers[j]
            
            if(temp > somma):
                somma = temp
                
    
    somma_minima = somma
    
    for i in range(0, len(numbers)):
        
        temp = 0
        
        for j in range (i + 1, len(numbers)):
            
            temp = numbers[i] + numbers[j]
            
            if(temp < somma_minima):
                somma_minima = temp
    
    return somma_minima




array = [5, 8, 12, 18, 22]
array2 = [7, 15, 12, 18, 22]

print(sum_two_smallest_numbers(array2))
