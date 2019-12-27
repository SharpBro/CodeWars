def snail(array):
    k = 0; l = 0
    
    m = len(array)
    n = len(array)
    
    if len(array) == 1 and array[0] == []:
        return []
    
    sas = []
  
    while (k < m and l < n) : 
          
       
        for i in range(l, n) : 
            sas.append(array[k][i])
        k += 1
        for i in range(k, m) : 
            sas.append(array[i][n - 1])
        n -= 1
        if ( k < m) : 
            for i in range(n - 1, (l - 1), -1) : 
                sas.append(array[m - 1][i])
            m -= 1
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                sas.append(array[i][l])
            l += 1
    return sas
    
    
array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]

array2 = [[]]

print(len(array2))
        
