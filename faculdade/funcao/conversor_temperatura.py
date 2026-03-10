temp = int (input("Digite a temperatura:"))
simb = str (input("Digite para qual temperatura você quer converter (f ou c):"))

def conversor_temp (temp,simb):
    if simb == 'f':
        f = (1.8 * temp) + 32
        return f'A temperatura em Fahrenheit é: {round(f, 2)}' # a função round() está arredondando 'f' para no máximo 2 casas decimais
    elif simb == 'c':
        c = (temp-32)/1.8
        return f'A temperatura em Celsius é: {round(c, 2)}' 
    else:
        return 'simbolo invalido'
print (conversor_temp(temp,simb))