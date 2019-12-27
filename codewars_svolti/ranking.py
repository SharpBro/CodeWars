class User(object):
    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    def inc_progress(self,progresso):
        print(progresso, self.rank)
        ranked = [i for i in range(-8,8+1)]
        ranked.pop(8) #non esiste il livello 0, dunque e' eliminato
        
        if progresso not in ranked:
            try:
                raise ValueError
            except ValueError:
                print('progresso non valido')
        if self.rank > 8:
            try:
                raise ValueError
            except ValueError:
                print('non puoi andare oltre 8')
        
        pos_prog = ranked.index(progresso)
        pos_rank = ranked.index(self.rank)
        
        if pos_prog == pos_rank - 1:
            self.progress += 1
        elif pos_prog == pos_rank:
            self.progress += 3
        elif pos_prog > pos_rank:
            self.progress += 10*((abs(pos_prog-pos_rank))**2)
        
        
        if self.progress >= 100 and self.rank < 8:
            while(self.progress >= 100):
                self.progress -= 100
                self.rank += 1
                if self.rank == 0:
                    self.rank = 1
                elif self.rank == 8:
                    self.progress = 0
                    break
        elif self.rank == 8:
            self.progress = 0
            
utente = User()
utente.inc_progress(5)
print(utente.progress, utente.rank)
