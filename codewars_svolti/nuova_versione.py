"""
You're fed up about changing the version of your software manually. Instead, you will create a little script that will make it for you.
Exercice

Create a function nextVersion, that will take a string in parameter, and will return a string containing the next version number.

For example:

nextVersion("1.2.3") === "1.2.4";
nextVersion("0.9.9") === "1.0.0";
nextVersion("1") === "2";
nextVersion("1.2.3.4.5.6.7.8") === "1.2.3.4.5.6.7.9";
nextVersion("9.9") === "10.0";

Rules

All numbers, except the first one, must be lower than 10: if there are, you have to set them to 0 and increment the next number in sequence.

You can assume all tests inputs to be valid.


"""

def nuova_vers(vecchia_vers):
    divisione = vecchia_vers.split('.')
    divisione = divisione[::-1]
    divisione = [int(el) for el in divisione]
    
    if len(divisione) != 1:
        if divisione[0] + 1 <= 9:
            divisione[0] += 1
            riporto = 0
        else:
            divisione[0] = 0
            riporto = 1
    else:
        divisione[0] += 1
        
    for elem in range(1, len(divisione)):
        if divisione[elem] + riporto > 9:
            if elem != len(divisione)-1:
                divisione[elem] = 0
                riporto = 1
            else:
                divisione[elem] += riporto
        else:
            divisione[elem] += riporto
            riporto = 0
    
    divisione = divisione[::-1]
    divisione = '.'.join(str(el) for el in divisione)
    return(divisione)
             
                
        

print(nuova_vers("10"))
