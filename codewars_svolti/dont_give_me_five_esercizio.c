#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

/*In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. 
 * The start and the end number are both inclusive!

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12

The result may contain fives. ;-)
The start number will always be smaller than the end number. Both numbers can be also negative!*/

char * int_to_str(int);
int check_five(char*);
int dontGiveMeFive(int start, int end);


int main(){
    
    
    
    dontGiveMeFive(500,2000);
    
    
    return 0;
}




/*the function converts the integer into a string*/
char * int_to_str(int num){
    
    char* string;
    int num_cifre = 0;
    int temp = num;
    
    /*absolute value of the negative number(i should have used math.h)*/
    if(num < 0){
        temp *= -1;
        num_cifre += 1; //one more space for the sign
    }        
    
    
    
    //the cycle counts how many digit the number has
    while(temp > 0){
        temp /= 10;
        num_cifre += 1;
    }
    //for the 0's case
    if(num == 0)
        num_cifre = 1;
    
    //to allocate the necessary amount of space + the special character '\0'
    string = (char*)malloc((num_cifre + 1) * sizeof(char));

    
  //use the function sprintf to convert
    sprintf(string, "%d", num);
    //return the string
    return string;
    
    
}
/*returns 1 if there is a 5, 0 otherwise*/
int check_five(char* num){
    
    int lung = strlen(num);
    int flag = 0;
    
    for(int i=0; i < lung && flag == 0; i++){
        
        if(num[i] == '5')
            flag = 1;
        
    }
    
    return flag;
}


int dontGiveMeFive(int start, int end){
    
    int counter = 0;
    char* num;
    
    for(int i = start; i<=end; i++){
        
        num = int_to_str(i);
        
        if(check_five(num) == 0)
            counter += 1;//increase the counter if the number meets all the conditions
        
    }
    
    return counter;
     
}
