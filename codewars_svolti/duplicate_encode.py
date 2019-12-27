"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

"""
def duplicate_encode(stringa):
    diz = {} #a blank dictionary
    stringa = stringa.lower() #case insensitive
    for carattere in stringa:
        if carattere in diz:
            diz[carattere] += 1 #add one if the element is in the dictionary
        else:
            diz[carattere] = 1#create a new key
    
    nuova = ""
    for carattere in stringa:
        if diz[carattere] > 1:#if the occurrence of the char is more than one
            nuova += ')'#add a closed parenthesis
        else:
            nuova += '('#add an open parenthesis
    return nuova
        
    
miao("(( @")
