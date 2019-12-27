"""
Implement the Polybius square cipher.

Replace every letter with a two digit number. The first digit is the row number, and the second digit is the column number of following square. Letters 'I' and 'J' are both 24 in this cipher:
	1	2	3	4	5
1	A	B	C	D	E
2	F	G	H	I/J	K
3	L	M	N	O	P
4	Q	R	S	T	U
5	V	W	X	Y	Z

Input will be valid (only spaces and uppercase letters from A to Z), so no need to validate them.
Examples

polybius('A')  # "11"
polybius('IJ') # "2424"
polybius('CODEWARS') # "1334141552114243"
polybius('POLYBIUS SQUARE CIPHER') # "3534315412244543 434145114215 132435231542"
"""


import string
def polybius(text):
    
    tab_car = string.ascii_uppercase
    matrice = {}
    i = 1
    j = 1
    for num in tab_car:
        if i == 6:
            j += 1
            i = 1
        if(num != 'J'):
            matrice[num] = int(str(j)+str(i))
            i += 1
    matrice['J'] = 24
    stringa = ""
    for car in text:
        if(car in matrice):
            stringa += str(matrice[car])
        else:
            stringa += car
    return(stringa)
    
polybius("POLYBIUS SQUARE CIPHER")
