import random
from random import randint
'''
#1
# um numero é par se o
lista = [1,2,3,4,5]

for i in lista:
'''

#2
"""
num = int(input("Digite um número: "))
resultado = 1
count = 1

while count <= num:
    resultado = resultado * count
    count += 1

print("Fatorial:", resultado)
"""

#3

#3.1 sem biblioteca
'''
jog = int(input('digite um numero: '))

numero = 90

while jog!= numero:
    
    if jog <=100 and jog >=1:
        if jog>numero:
            print("numero maior que o secreto (entre 1 e 100)")
        elif jog<numero:
            print("numero menor que o secreto (entre 1 e 100)")

    else:
        print("numero fora do jogo, digite um numero entre 1 e 100")
    jog = int(input('digite um numero: '))

else:
    print ("parabéns você acertou o número! o numero secreto era:", numero)
'''

#3.2

jog = int(input('digite um numero: '))

numero = random.randint(1,100)

while jog != numero:

    if jog <= 100 and jog >= 1:
        if jog > numero:
            print("numero maior que o secreto (entre 1 e 100)")
            print(numero)
        elif jog < numero:
            print("numero menor que o secreto (entre 1 e 100)")
            print(numero)
    #else:
     #   pass
        #print("numero fora do jogo, digite um numero entre 1 e 100")
    jog = int(input('digite um numero: '))

else:
    print("parabéns você acertou o número! o numero secreto era:", numero)
    
'''
numerosecreto = 38

tentativa = 0

while tentativa != numerosecreto:
    tentativa = int(input('digite um numero: '))
    if tentativa > numerosecreto:
        print('o numero secreto é menor')
'''