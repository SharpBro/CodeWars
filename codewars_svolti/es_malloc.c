#include <stdio.h>
#include <stdlib.h>

void my_exit(char* err, int sas);
void funz_1();
void funz_2();
void funz_3();

int main(int argc, char** argv){
    
    //funz_1();
    funz_2();
    
    return 0;
}

void funz_1(){
   int dim;
   int *v;
   
   printf("quanti elementi inserire nel vettore?: ");
   scanf("%d", &dim);
   
   v = malloc(dim * sizeof(int));
   if(!v){
       my_exit("impossibile allocare memoria",1);
   }
   
   for(int i=0; i<dim; i++){
    printf("\ninserisci elemento %d: ",i+1);
    scanf("%d",v + i);
   }
   
      
   for(int i=0; i<dim; i++){
    printf("\nelemento %d: %d ",i+1, v[i]);
   }
    
    free(v);
    
    return;
    
}
void funz_2(){
    int allocata = 2;
    int *v = malloc(allocata * sizeof(int));
    int input;
    int richiesta = 0;
    do{
        printf("inserire elemento %d: ", richiesta + 1);
        scanf("%d", &input);
        if(input != 0){
            if (allocata < richiesta){
                    allocata *= 2;
                    v = realloc(v, allocata*sizeof(int));
            }
            v[richiesta] = input;
            richiesta ++;
        }
        
    }while(input != 0);
    
    for(int i=0; i<richiesta; i++){
        printf("\nelemento %d: %d", i+1,v[i]);
    }
    free(v);
    
    return;
}
void my_exit(char* err, int sas){
        fprintf(stderr,"%s",err);
        exit(sas);
}
