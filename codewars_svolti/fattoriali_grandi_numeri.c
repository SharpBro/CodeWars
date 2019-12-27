#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>

int moltiplica_cifra(int pos_cifra,int a[],int dim);
char* converti_in_stringa(int[], int);
char *factorial(int n);

int main(int argc, char** argv) {
    
    char* fattoriale;
    int num;
    
    
    printf("inserire il numero del quale si vuole calcolare il fattoriale: ");
    scanf("%d", &num);
    
    
    fattoriale = factorial(num);
    
    
    printf("%s\n", fattoriale);  
        
    free(fattoriale); //svuoto la stringa

    
    return (EXIT_SUCCESS);
}

int moltiplica_cifra(int pos_cifra,int a[],int dim)
{
	int riporto =0,i,p;
    
	for(i=0;i<dim;++i)
	{
		p=a[i]*pos_cifra+riporto;
		a[i]=p%10;
		riporto=p/10;
	}
		
	while(riporto !=0)
	{
            a[dim] = riporto%10;
            riporto /= 10;
            dim += 1;		
	}    	
    	return dim;
}

char* converti_in_stringa(int num[], int size){
    
    char* str;
    
    str = calloc(size + 1, sizeof(char));
    
    
    for(int i=size-1;i>=0;--i)
    {
		str[size-i-1] = num[i] + '0';   	
    }
    
       
    str[size] = '\0';
    
    return str;
}


char *factorial(int n){
    
    double res;
    
    /*thanks to "factorial number of digits" at math.stackexchange.com*/
    res = ceil(n * log10(n) - 0.434 * n + log10(2 * 3.1415926 * n));

    int dim = (int)res;/*di quante cifre e' costituito il fattoriale*/
    int *a;
    
    a = calloc(dim, sizeof(int));
    
    int i;
    int size=1;
    
    a[0]=1;
    
    for(i=2;i<=n;++i) {
        size=moltiplica_cifra(i,a,size);    		
    }
    	
    char * str;
    
    str = converti_in_stringa(a, size);
    
    free(a);
    
    return str;
    
}
