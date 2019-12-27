def pratino(array):
    lung_arr = len(array)
    
    for i in range(lung_arr-1):
        if array[i] > array[i+1] and i+1 < lung_arr:
            array[i] -= array[i+1]
    
    return array

def solution(array):
    
    counter = 0
    while True:
        arr = array[:]
        
        arr = arr[::-1]
        arr = pratino(arr)
        
        counter += 1
        if(arr[::-1] == arr):
            break
        
        array = arr[:]
        
    print(counter)
    somma = 0
    
    for i in arr:
        somma += i
        
    return(somma)
    
    
            
            
solution([1,21,55])
