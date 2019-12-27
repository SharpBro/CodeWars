"""
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

Note: there are no special characters used, only letters and spaces
"""


def decipher_this(string):
  stripped = string.split()
  
  decifra = []
  for el in stripped:
      
      primo_car = ""
      for carattere in el:
          if carattere.isdigit():
              primo_car += carattere
              
      primo_car = chr(int(primo_car))
      
      parola = ""
      parola += primo_car
      for car in el:
          if not car.isdigit():
              parola += car
              
      if len(parola) >= 2:
          parola = list(parola)
          parola[1], parola[len(parola)-1] = parola[len(parola)-1], parola[1]
      
      parola = ''.join(parola)
      
      decifra.append(parola)
 
  decifr = ' '.join(decifra)
  return(decifr)
          
          
  
decipher_this('84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp')
