'''
Imagine que você está criando o sistema de entrada para um cinema que só aceita maiores de idade para um filme de terror.

O que o seu script deve fazer:

Perguntar ao usuário: "Qual a sua idade?"

Se a idade for 18 ou mais, o programa deve exibir: "Acesso liberado! Bom filme. 🍿"

Se a idade for menor que 18, o programa deve exibir: "Acesso negado. Você precisa de um responsável. 🚫"
'''

idade = int (input("Qual a sua idade? "))

if 100 > idade >= 18 :
    print ("Acesso liberado! Bom filme. 🍿")
elif idade == 100:
    print ("Uau, você é um espectador lendário!")
elif idade > 120:
    print("Perai po, deixa de mentira")
else:
    print ("Acesso negado. Você precisa de um responsável. 🚫")