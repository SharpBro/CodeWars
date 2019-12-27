def likes(names):
    stringa_like = ""
    
    if len(names) == 0:
        return "no one likes this"
    
    elif len(names) == 1:
        stringa_like = names[0] + "likes this"
        return stringa_like
    elif len(names) == 2:
        stringa_like = names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        stringa_like = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        stringa_like = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others" + " like this"



    return stringa_like



lista = ['Mario','Giovanni','Antonio','Mattia','Mastaniello']

res = ""
res = likes(lista)

print(res)
