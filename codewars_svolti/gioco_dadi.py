"""
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
"""

from collections import Counter as ct

def score(dice):
   a = ct(dice)
   a1 = list(a)
   a2 = list(a.values())
   
   #print(a1,a2)
   somma = 0
   
   for index in range(0, len(a1)):
       if(a1[index] == 1 and a2[index] >= 3):
           somma += 1000
           a2[index] -= 3
       elif(a2[index] >= 3):
           somma += a1[index] * 100
           a2[index] -= 3
       
       if((a1[index] == 1 or a1[index] == 5) and a2[index] < 3):
           if(a1[index] == 1):
               somma += 100 * a2[index]
           else:
               somma += 50 * a2[index]
   
   return somma
 
      

      
          
   
   
   
rr = [2, 4, 4, 5, 4]

score(rr)
