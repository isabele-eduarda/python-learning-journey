num_fat = int (input())

def cal_fatorial (num_fat):
    cont = 1
    resultado = 1
    while cont <= num_fat:
        resultado *= cont
        cont +=1
    return resultado
print (cal_fatorial(num_fat))