#include <stdio.h>
#include <stdlib.h>
#include <math.h>


/*contare gli '1' presenti nell'intervallo left, right(estremi compresi) convertito in binario*/
long long countOnes ( int left, int right );
int main(int argc, char** argv) {
    
    
    printf("%lld",countOnes(4,7));

    return (EXIT_SUCCESS);
}



long long countOnes ( int left, int right ) //SEE oeis.org/A000788
{
    
    long long contatore = 0;
    long long num = right;
    long long differenza;
    
    while(num>0){
        int i= (int)(log10(num)/log10(2));
        contatore += pow(2, i-1)*i;
        contatore += num - pow(2, i)+1;
        num -= pow(2, i);
    }
    differenza = contatore;
    
    if(left > 0){
        
        contatore = 0;
        num = left - 1;
        
        while(num>0){
        int i= (int)(log10(num)/log10(2));
        contatore += pow(2, i-1)*i;
        contatore += num - pow(2, i)+1;
        num -= pow(2, i);
        }
        
        differenza -= contatore;
        
    }
    
    return differenza;
} 
