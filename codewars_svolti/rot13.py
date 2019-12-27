import string
def rot13(message):
    alfa_min = string.ascii_lowercase
    alfa_max = string.ascii_uppercase
    stringa = ""
    for car in message:
        if car not in alfa_min and car not in alfa_max:
            stringa += car
        else:
            if car in alfa_min:
                stringa += alfa_min[(alfa_min.index(car) + 13) % 26]
            else:
                stringa += alfa_max[(alfa_max.index(car) + 13) % 26]
    return(stringa)
    
    
rot13("Test")
            
     
