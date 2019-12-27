def clever_validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''



def validBraces(string):
  
  contatore_tonde = 0
  contatore_quadre = 0
  contatore_graffe = 0
  
  previous_i = 'c'

  for i in string:
      
      if i == '(':
          contatore_tonde += 1
      if i == ')':
          contatore_tonde -= 1
      if i == '[':
          contatore_quadre += 1
          flag2 = 1
      if i == ']':
          contatore_quadre -= 1
      if i == '{':
          contatore_graffe += 1
          flag3  = 1
      if i == '}':
          contatore_graffe -= 1
          
      if(contatore_graffe < 0 or contatore_quadre < 0 or contatore_tonde < 0):
          print("undershit parentesi")
          return False
      
      if(previous_i == '(' and i == ']' or previous_i == '(' and i == '}' or previous_i == '[' and i == '}'):#casi in cui viene chiusa una parentesi in maniera non corretta
          return False
      
      previous_i = i
      

  #print(contatore_tonde,contatore_quadre,contatore_graffe)
  
  if(contatore_graffe != 0 or contatore_quadre != 0 or contatore_tonde != 0):#se i contatori non sono stati azzerati alla fine della sequenza
      return False
      
  return True #se supera tutti i test, e' una stringa ben formata
    
par = "[(])"  
 
print(validBraces(par))
      
      
