/*Scrivete  una  funzione  con  prototipovoid split_time ( long int tot_sec, int *h, int *m, int *s )che,dato un orario fornito in numero di secondi dalla mezzanotte, calcoli l’orario equivalente in ore, minuti, secondi, e lomemorizzi nelle tre variabili puntate da (h), (m) e (s) rispettivamente.*/
#include <stdio.h>
#include <stdlib.h>

void split_time ( long int tot_sec, int *h, int *m, int *s );
int main(int argc, char** argv){
    
    int ore,minuti,secondi;
    long int tempo = 0;
    
    printf("inserisci i secondi da convertire: ");
    scanf("%ld", &tempo);
    split_time(tempo,&ore,&minuti,&secondi);
    
    printf("%ld secondi corrispondono a: %d ore %d minuti %d secondi\n",tempo,ore,minuti,secondi);
    
    return 0;
}
void split_time ( long int tot_sec, int *h, int *m, int *s ){
    
    *h = *m = *s = 0;
    
    while(tot_sec >= 3600){
        tot_sec -= 3600;
        *h += 1;        
    }
    while(tot_sec >= 60){
        tot_sec -= 60;
        *m += 1;
    }
    
    *s += tot_sec;
    
    while(*s >= 60){
        *m += 1;
        *s -= 60;
    }
    
    while(*m >= 60){
        *m -= 60;
        *h += 1;
    }
}
