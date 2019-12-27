"""Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

"""


import re


def iq_test(numbers):
    
    list = map(int, re.findall(r'\d+', numbers))
    
    lung = len(list)
    
    pari = 0
    dispari = 0
    
    for i in range(0, lung):
            if(list[i] % 2 != 0):
                dispari += 1
            else:
                pari += 1
                
    if(pari > dispari):
        for i in range(0, lung):
            if(list[i] % 2 != 0):
                return (i+1)
    else:
         for i in range(0, lung):
            if(list[i] % 2 == 0):
                return (i+1)

    
a = iq_test("46 7 15 19 13 15 31 45 39 23 39 7 33 39 3 29 15 11 5 17 35 25 39 9 33 33 43 37 31 51 17 21 49 41 3 51 37")

print(a)


