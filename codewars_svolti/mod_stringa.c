/*scrivere la funzione LetterChanges, che riceve in ingresso una stringa e stampa una nuova stringa secondo queste regole:
 -se il carattere i-esimo della stringa passata e' alfabetico salva alla posizione i-esima della nuova stringa il carattere alfabetico successivo
  es. b -> c
  
-se inoltre il carattere alfabetico successivo e' una vocale, allora dovra' essere convertita in maiuscolo

-non modificare altrimenti il carattere*/




#include <stdio.h> 
#include <ctype.h>
#include <string.h>

int is_vowel(char car){
    char vowels[5] = {'a','e','i','o','u'};
    
    for(int i=0; i<5; i++){
        if(car == vowels[i])
            return 1;
    }
    return 0;
}

void LetterChanges(char str[]) { 
  
  int len = strlen(str);
  
  char new_str[len];
  
  char carac;
  
  for(int i=0; i<len; i++){
      
      if(isalpha(str[i] + 1) != 0){
          
        if(is_vowel(str[i] + 1) == 1){
            
            carac = toupper(str[i] + 1);
            
        }
        else
            carac = str[i] + 1;
            
        
        new_str[i] = carac;
      }
      else
        new_str[i] = str[i];
  }
  
  new_str[len] = '\0';
  
  printf("%s", new_str); 
            
}

int main(void) { 
  
  // keep this function call here
  LetterChanges(gets(stdin));
  return 0;
    
} 
