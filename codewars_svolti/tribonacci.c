#include <stdlib.h>
#include <malloc.h>
#define DIM 30


long long *tribonacci(const long long signature[3], size_t n);

int main(){
   
    long long * trib;
    long long sas[3] = {1,1,1};
    
    trib = tribonacci(sas, DIM);
    
    if(trib == NULL){
        puts("dimensione non valida");
        exit(EXIT_FAILURE);
    }
    
    for(int i=0; i<DIM; i++)
        printf("%lld ", trib[i]);
    
    
 return 0;   
}

/*LA FUNZIONE RESTITUISCE */

long long *tribonacci(const long long signature[3], size_t n) {

  if(n <= 0)
    return NULL;
  
  long long* seq_trib = (long long*)malloc(n * sizeof(long long));
  
  long long trib_3 = signature[0];
  long long trib_2 = signature[1];
  long long trib_1 = signature[2];
  long long trib;

  
  seq_trib[0] = trib_3;
  seq_trib[1] = trib_2;
  seq_trib[2] = trib_1;
  
  for(int i=3; i<n; i++){
      
      trib = trib_1 + trib_2 + trib_3;
      seq_trib[i] = trib;
      
      trib_3 = trib_2;
      trib_2 = trib_1;
      trib_1 = trib;      
  }
  
  return seq_trib;

} 
