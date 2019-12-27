#include <stdio.h>
#include <stdlib.h>

char *read_line( void );
int main(int argc, char** argv){
    
    char* s;
    s = read_line();
    if(s != NULL){
            printf("%s", s);
    }
    else
        printf("errore in read_line");
    
    
    
    return 0;
}
char *read_line( void ){
    char* stringa;
    int allocata = 20;
    int richiesta = 0;
    char carattere;
    stringa = malloc((allocata+1)*sizeof(char));
    
    if(!stringa)
        return NULL;
    
    while(1){
        scanf("%c", &carattere);
        if(carattere == '\n')
            break;
        else{
            richiesta +=1;
            if(richiesta > allocata){
                    allocata += 40;
                    stringa = realloc(stringa,allocata);
                    if(!stringa)
                        return NULL;
            }
            stringa[richiesta] = carattere;
        } 
    }
    return stringa;
    
}
