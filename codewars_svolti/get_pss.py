def mossa(comando,posiz):
    mov_su_griglia = ['left', 'right', 'up', 'down'] 
    acquisisci_da_pos = ['leftT', 'rightT', 'upT', 'downT']
    
    if comando in mov_su_griglia:
        if comando == 'left':
            return 1,[posiz[0],posiz[1]-1]
        elif comando == 'right':
            return 1,[posiz[0],posiz[1]+1]
        elif comando == 'up':
            return 1,[posiz[0]-1,posiz[1]]
        else:
            return 1,[posiz[0]+1,posiz[1]]
    else:
        if comando == 'leftT':
            return 2,[posiz[0],posiz[1]-1]
        elif comando == 'rightT':
            return 2,[posiz[0],posiz[1]+1]
        elif comando == 'upT':
            return 2,[posiz[0]-1,posiz[1]]
        else:
            return 2,[posiz[0]+1,posiz[1]]
        
    


def get_password(grid,directions):
    
    fnd_start_pos = False
    
    num_righe = len(grid)
    num_col = len(grid[0])
    
    pos_corrente = []
    
    for i in range(0, num_righe):
        for j in range(0, num_col):
            if(grid[i][j] == 'x'):
                pos_corrente = [i,j]
                break
        if True:
            continue
        else:
            break
        
    password = ""
    for spost in directions:
        istruz,nuova_pos = mossa(spost, pos_corrente)
        if(istruz == 2):
            password += grid[nuova_pos[0]][nuova_pos[1]]
            pos_corrente = nuova_pos[:]
        else:
            pos_corrente = nuova_pos[:]
    
    return(password)
        
grid = [
    ["x", "l", "m"],
    ["o", "f", "c"],
    ["k", "i", "t"]
  ]
directions = ["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"]
get_password(grid, directions)
