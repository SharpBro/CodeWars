def flatten(array):
    res = []
    for elem in array:
        for i in elem:
            res.append(i)
    res = sorted([int(elem) for elem in res])
    return(res)
        
    
    
array =  [[3, 2, 1,1299], [4, 6, 5], [], [9, 7, 8]]

flatten(array)
