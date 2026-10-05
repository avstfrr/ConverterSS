def input_10_cust_cel_ss(chislo,ss):
    res = ''
    alf = ('a','b','c','d','e','f')
    while chislo >= ss:
        ostatok = chislo % ss
        if ostatok < 10:
            res = str(ostatok) + res
        elif ostatok == 0:
            res = '1' + res
        else:
            res = alf[(ostatok - 10)] + res
        chislo = chislo // ss
    ostatok = chislo % ss
    if ostatok < 10:
        res = str(ostatok) + res
    else:
        res = alf[(ostatok - 10)] + res
    return(res)


def input_10_cust_dr_ss(chislo,ss):
    znakov = 6
    chislo = float(chislo)
    dr = chislo % 1
    res = ''
    cel = int(chislo//1)
    alf = ('a','b','c','d','e','f')
    while len(res) < znakov:
        stack = int((dr * ss) // 1)
        if stack < 10:
            res = res + str(stack)
        else:
            res = res + alf[(stack - 10)]
        dr = (dr * ss) % 1
    return(input_10_cust_cel_ss(cel,ss)+'.'+res)


def others_in_10_cel(chislo,ss):
    chislo = str(chislo)
    res = 0
    alf = ('a','b','c','d','e','f')
    count = len(chislo)-1
    for x in chislo:
        if not x in alf:
            res = res + (int(x) * (ss**count))
            count-=1
        else:
            cifra = 1
            for i in alf:
                if i == x:
                    res = res + ((9+cifra) * (ss**count))
                cifra +=1
            count-=1
    return(res)


def others_in_10_dr(chislo,ss):
    chislo = str(chislo)
    znak = chislo.find('.')
    dr = chislo[znak+1: ]
    cel = chislo[:znak]
    alf = ('a','b','c','d','e','f')
    res = 0.0
    count = len(cel)-1
    
    for x in cel:
        if not x in alf:
            res = res + (int(x) * (ss**count))
            count-=1
        else:
            cifra = 1
            for i in alf:
                if i == x:
                    res = res + ((9+cifra) * (ss**count))
                cifra +=1
            count-=1
            
    count = -1
    
    for x in dr:
        if not x in alf:
            res = res + (int(x) * (ss**count))
            count-=1
        else:
            cifra = 1
            for i in alf:
                if i == x:
                    res = res + ((9+cifra) * (ss**count))
                cifra +=1
            count-=1
    count = -1
        
    return(res)


def standartout(chislo):
    chislo = str(chislo)
    znak = chislo.find('.')
    dr = chislo[znak+1: ]
    cel = chislo[:znak]
    res = ''
    if len(dr) > 6:
        dr = dr[0:6]
        return(res)
    elif len(dr) < 6:
        while len(dr) < 6:
            dr = dr + '0'
    res = cel+'.'+dr
    return(res)
    



def universalinout():
    print('Введите число:')
    chislo = str(input())
    if chislo == 'ex':
        return('exit')
    alf = '.0123456789abcdef'
    for x in chislo:
        if not x in alf:
            print('Ваше число некорректно введено, вы можете использовать только данные символы:' + alf)
            return('Error')
    print('Введите систему счисления числа:')
    inputss = int(input())
    if (inputss < 2) or (inputss > 16):
        print('Поддерживаются лишь системы счисления от 1, до 16')
        return('Error')
    for x in chislo:
              if x not in alf[:18-(17-inputss)]:
                  print('Эта система счисления не соответствует ранее указаному числу')
                  return('Error')
    print('Введите систему счисления для вывода:')
    outputss = int(input())
    if (inputss < 2) or (inputss > 16):
        print('Поддерживаются лишь системы счисления от 1, до 16')
        return('Error')
    if inputss == outputss:
        if '.' in chislo:
            return(standartout(chislo))
        else:
            return(chislo)
    if not '.' in chislo:
        if inputss == 10:
            return(input_10_cust_cel_ss(chislo,outputss))
        else:
            chisloin10 = others_in_10_cel(chislo,inputss)
            return(input_10_cust_cel_ss(chisloin10,outputss))
    else:
        if inputss == 10:
            return(input_10_cust_dr_ss(chislo,outputss))
        else:
            chisloin10 = others_in_10_dr(chislo,inputss)
            return(input_10_cust_dr_ss(chisloin10,outputss))



print('Поддерживаются числа до 16-ричной СС, использует вычислительные округления python и выводит 6 знаков после запятой.')
print('Вы можете ввести "ex" для выхода.')
res = 'None'
while True:
    res = universalinout()
    if res == 'exit':
        break

    if res != 'Error':
        if '.' in str(res):
            print(standartout(res))
        else:
            print(res)
    print()
print('Программа завершена.')

#print(int(x,2))
#universalinout()
#print(input_10_cust_cel_ss(6782,16))
#print(others_in_10_cel("1a7e",16))
#print(int('1a7e',16))
#print(input_10_cust_dr_ss(0.125,8,6))
#x = 90.99
#print(input_10_cust_dr_ss(x,2,6), input_10_cust_dr_ss(x,8,6), input_10_cust_dr_ss(x,16,6))
