def check_colonna(board,size,q_pos):
        for i in range(size):
            if(board[i][q_pos[1]] != 0):
                return False
        return True

def check_riga(board,size,q_pos):
        for j in range(size):
            if(board[q_pos[0]][j] != 0):
                return False
        return True

def check_diag(board,size,q_pos):
        for i in range(size):
            for j in range(size):
                if(q_pos[0] + q_pos[1] == i+j and i != q_pos[0] and j != q_pos[1]):
                    if(board[i][j] != 0):
                        return False
        for i in range(size):
            for j in range(size):
                if(q_pos[1] - q_pos[0] == j-i and i != q_pos[0] and j != q_pos[1]):
                    if(board[i][j] != 0):
                        return False
           
        return True 

def posiz_valida(board,size,q_pos):
        
        return (check_colonna(board,size,q_pos) and check_riga(board,size,q_pos) and check_diag(board,size,q_pos))
    


def back_queens(board,size,num_regine):
    
    
    
    if num_regine == 0:
        for el in board:
            print(el)
        print("")
        return True
    
    for i in range(size):
        for j in range(size):
            if posiz_valida(board,size,(i,j)) and board[i][j] != 1:
                
                board[i][j] = 1
                
                if back_queens(board,size,num_regine - 1) == True:
                    return True
                
                board[i][j] = 0
    return False
    
    


size = 10

board = [[0 for elem in range(size)] for i in range(size)]

back_queens(board, size,size)






