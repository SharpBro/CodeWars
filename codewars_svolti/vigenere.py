class VigenereCipher():
    def __init__(self,key,alphabet):
        self.key = key
        self.alphabet = alphabet
        
    def encode(self,stringa_da_codificare):
        chiave = ""
        
        stringa_da_codificare = stringa_da_codificare.decode('utf-8')
        
        flag = 0
        for car in stringa_da_codificare:
            if car.isupper() == True:
                flag = 1
                break
        
        stringa_da_codificare = stringa_da_codificare.lower()
        
        for l in range(0, len(stringa_da_codificare)):
            chiave += self.key[l % len(self.key)]
        
        cifrato = ""
        indice = 0
        for carattere in stringa_da_codificare:
            try:
                pos_alfabeto = self.alphabet.index(carattere)
                shift = self.alphabet.index(chiave[indice])
                cifrato += self.alphabet[(pos_alfabeto + shift) % len(self.alphabet)]
            except:
                cifrato += carattere
                
            indice += 1
        
        if flag == 1:
            cifrato = cifrato.upper()
        
        #stringa_da_codificare = stringa_da_codificare.encode('utf-8')
        
        return(cifrato)
    
    def decode(self,stringa_da_decriptare):
        chiave = ""
        
        stringa_da_decriptare = stringa_da_decriptare.decode('utf-8')
        flag = 0
        for car in stringa_da_decriptare:
            if car.isupper() == True:
                flag = 1
                break
            
        stringa_da_decriptare = stringa_da_decriptare.lower()
        
        for l in range(0, len(stringa_da_decriptare)):
            chiave += self.key[l % len(self.key)]
        
        decifrato = ""
        indice = 0
        for carattere in stringa_da_decriptare:
            try:
                pos_alfabeto = self.alphabet.index(carattere)
                shift = self.alphabet.index(chiave[indice])
                decifrato += self.alphabet[(pos_alfabeto - shift) % len(self.alphabet)]
            except:
                decifrato += carattere
            indice += 1
        
        if flag == 1:
            decifrato = decifrato.upper()
        
        #stringa_da_decriptare = stringa_da_decriptare.encode('utf-8')
        return(decifrato)  
                
                
c = VigenereCipher('verme','abcdefghijklmnopqrstuvwxyz')
codif = c.encode('CODE??WARS$4')
decodif = c.decode(codif)
print(codif,decodif)
