from calendar import *

def calendar(anno,mese):
    
    mesi = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    str_tot = ""
    sec_str = "SUN MON TUE WED THU FRI SAT"
    first_str = ""
    first_str += str(anno) + ' '
    first_str += mesi[mese]
    first_str = first_str.center(len(sec_str))
    str_tot += first_str + '\n' + sec_str + '\n'
    matr = monthcalendar(anno,mese)
    for el in matr:
        for dat in el:
            if dat != 0:
                str_tot += '%3s' % str(dat)
            else:
                str_tot += '%3s' % (' ')
            str_tot += ' '
        str_tot += '\n'
    print(str_tot)
            
for i in range(1,13):
    calendar(2019,i)
