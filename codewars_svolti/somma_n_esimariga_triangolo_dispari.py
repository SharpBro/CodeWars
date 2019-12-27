def row_sum_odd_numbers(n):
    num = 0
    a = ((n-1)*n)/2
    
    
    for i in range (0, n):
        num +=  2 * a + 1
        a += 1
    
    print(num)
        

row_sum_odd_numbers(5)
