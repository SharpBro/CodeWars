#include <stdio.h>
#include <stdlib.h>

void sel_sort(int* array, int dim);
void my_error(char* s, int err);
void swap(int*,int*);
void print_array(int* array,int dim);
int* acquisizione_array(int dim);

int main(int argc, char** argv){
    int* array;
    array = acquisizione_array(20);
    
    if(!array)
        my_error("impossibile allocare memoria sufficiente all'operazione", 1);
    
    print_array(array,20);
    
    sel_sort(array,20);
    
    print_array(array,20);
    
    return 0;
}


int* acquisizione_array(int dim){
    int* arr;
    
    arr = malloc(dim*sizeof(int));
    if(!arr)
        return NULL;
    
    int temp;
    int res;
    
    for(int i=0; i<dim; i++){
        printf("inserisci elemento %d: ", i + 1);
        scanf("%d",&temp); 
        *(arr + i) = temp;
        
    }
    
    return arr;
    
}
void print_array(int* array,int dim){
    
    puts("");
    for(int i=0; i<dim; i++){
        printf("%d ", *(array + i));
    }
    puts("");
    
}
void sel_sort(int* array, int dim){
    
  int posmin;
  
  for(int i = 0; i<dim; i++){
    posmin = i;
    for (int j = (i + 1); j< dim; j++){
      if (*(array + j) < *(array + posmin))
            posmin = j;
      if (posmin != i){
        swap((array + i), (array + posmin));
      }
    }
  }
  
  return;
}

void swap(int* a,int* b){
    int temp;
    
    temp = *a;
    *a = *b;
    *b = temp;
}

void my_error(char* s, int err){
    
    fprintf(stderr,"\n%s",s);
    exit(err);
    
}
 
