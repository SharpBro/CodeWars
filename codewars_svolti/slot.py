"""
You will be given three reels of different images and told at which index the reels stop. From this information your job is to return the score of the resulted reels. 

1. There are always exactly three reels
2. Each reel has 10 different items.
3. The three reel inputs may be different.
4. The spin array represents the index of where the reels finish.
5. The three spin inputs may be different
6. Three of the same is worth more than two of the same
7. Two of the same plus one "Wild" is double the score.
8. No matching items returns 0.
"""
def tab_riferimento(nome):
    valore = 0
    if nome == 'Wild': valore = 10
    elif nome == 'Star': valore = 9
    elif nome == 'Bell':valore = 8
    elif nome == 'Shell':valore = 7
    elif nome == 'Seven':valore = 6
    elif nome == 'Cherry': valore = 5
    elif nome == 'Bar':valore = 4
    elif nome == 'King': valore = 3
    elif nome == 'Queen':valore = 2
    elif nome == 'Jack': valore = 1
    
    return valore
        
def fruit(reels, spins):
     #3 ruote; reels
     
     risultato = [reels[i][spins[i]] for i in range(0,3)]
     conta_num = {}
     for elem in risultato:
         if elem in conta_num:
             conta_num[elem]+= 1
         else:
             conta_num[elem] = 1
    
    
     conta_num = sorted(conta_num.items() ,  key=lambda x: x[1], reverse = True)#creo una lista ordinata per valori
     #print(conta_num)
     
     if len(conta_num) == 1:
         return (10 * tab_riferimento(conta_num[0][0]))
     if len(conta_num) == 2:
         if(conta_num[1][0] == 'Wild'):
             return (2 * tab_riferimento(conta_num[0][0]))
         return tab_riferimento(conta_num[0][0])
     
     return 0
             
reel1 = ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"]
reel2 = ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"]
reel3 = ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"]
print(fruit([reel1,reel2,reel3], [0,0,1]))
         
