def comp(array1, array2):
    if(array1 == None or array2 == None):
        return False

    for i in array1:
        if i**2 in array2:
            array2.remove(i**2)
    
    if(len(array2) == 0):
        return True
    
    return False
	 

arr1 = [78, 26, 75, 42, 21, 42, 97]
arr2 = [6084, 676, 5625, 1764, 441, 1765, 9409]

print(comp(arr1,arr2))
