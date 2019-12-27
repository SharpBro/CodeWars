 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <math.h>
 
void swap(char *, char *);
void permute(char *a, int l, int r, char**, int*);
long permutazioni(int n,int k);
long fattoriale(int);
unsigned long long next_smaller_number(unsigned long long n);
int numero_piu_piccolo_cercato(char*, char*);

int main() 
{ 
    
    long long responso;
    unsigned long long sos;
    
    printf("inserisci il sas: ");
    scanf("%llu", &sos);
        
    responso = next_smaller_number(sos);
    
    printf("%lld", responso);
    
    return 0; 
} 

/*swap the characters*/
void swap(char *a, char *b) 
{ 
    char temp; 
    
    temp = *a; 
    *a = *b; 
    *b= temp; 
} 
  
/* Function to get all permutation of the string a*/
void permute(char *a, int iniz_index, int last_index, char** array_str, int* num_stringhe) 
{ 
   int i; 
   if (iniz_index == last_index){ 
     //printf("%s\n", a);
       for(int i=0; i<*num_stringhe; i++){ //check se la cazz di stringa e' gia presente nell'array
           if(strcmp(a, array_str[i]) == 0)
               return;
       }
       strncpy(array_str[*num_stringhe], a, strlen(a)); //copio la stringa nell'array
       *num_stringhe += 1; //incremento il numero di stringhe
   }
   else
   { 
       for (i = iniz_index; i <= last_index; i++) 
       { 
          swap((a+iniz_index), (a+i)); 
          permute(a, iniz_index+1, last_index, array_str,num_stringhe); 
          swap((a+iniz_index), (a+i)); //backtrack 
       } 
   } 
} 



unsigned long long next_smaller_number(unsigned long long n){
    
    char num_conv[40];
    
    sprintf(num_conv, "%llu", n);
    
    int dim_num = strlen(num_conv);
    
    int num_stringhe = fattoriale(dim_num); //il max numero di stringhe ottenibili come permutazioni(limite superiore)
    
    char** array_cazzi;
    int pos = 0;
    
    array_cazzi = (char**)malloc(num_stringhe * sizeof(char*)); //alloco memoria sufficiente
    
    for(int i=0; i<num_stringhe;i++){
        array_cazzi[i] = malloc(dim_num + 1 * sizeof(char));
    }
    
    permute(num_conv, 0, dim_num - 1, array_cazzi, &pos); //permuta il numero in ogni modo possibile
    
/*
    for(int i=0; i<pos; i++){
        printf("%s\n", array_cazzi[i]);
    }
*/
    unsigned long long numero_piccolo;
    
    for(int i=0; i<pos; i++){
        if(numero_piu_piccolo_cercato(num_conv, array_cazzi[i]) == 1){
            numero_piccolo = atoi(array_cazzi[i]);
            return numero_piccolo;
        }
    }
    
    
    free(array_cazzi); //libero memoria allocata
    
    return -1;
}

long permutazioni(int n,int k){
    
    
    long perm;
    
    perm = fattoriale(n)/fattoriale(n - k);
    
    
    return perm;    
}

long fattoriale(int num){
    
    if(num == 0)
        return 1;
    
    long sas = num;
    
    for(int i=1; i<num; i++){
        sas *= i;
    }
    return sas;
}

int numero_piu_piccolo_cercato(char* numero_di_riferimento, char* numero_dell_array){
    
    
    if(numero_dell_array[0] == '0')
        return -1;
    
    unsigned long long num_riferim = atoi(numero_di_riferimento);
    unsigned long long num_panino = atoi(numero_dell_array);
    
    if(num_panino < num_riferim)
        return 1;
    
    return -1;   
}


