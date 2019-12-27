#https://brilliant.org/wiki/finding-the-last-digit-of-a-power/


"""
define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6. Also, please take 0^0 to be 1.

You may assume that the input will always be valid.
Examples

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6

"""
def last_digit(n1, n2):
    
    if n2 == 0:
        return 1
    "grazie a brilliant per la tabella"
    table_of_modulo = [[1],[4,8,6,2],[9,7,1,3],[6,4],[5],[6],[9,3,1,7],[4,2,6,8],[1,9]]
    
    last_a = n1 % 10#calcolo la cifra finale di n1
    
    if last_a == 0:
        return last_a

    
    if len(table_of_modulo[last_a - 1]) == 1:#se la sottolista e' costituita da un solo elemento, l'ultima cifra e' proprio quell'elemento
        return last_a
    else:
        return table_of_modulo[last_a - 1][ n2 % len(table_of_modulo[last_a - 1]) - 2]#altrimenti se la sottolista in table_of_modulo ha piu elementi, calcolo il modulo dell'esponente e sottraggo 2 per ottenere l'ultima cifra desiderata
    
    
print(last_digit(454545543, 0))
                                           
    
    
