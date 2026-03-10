#Escrever uma função que recebe 3 números e retorna a media aritimetica entre eles

def f_media (a,b,c):
    return (a+b+c)/3
a = float (input()) 
b = float (input())
c = float (input())

#result_media = f_media(a,b,c)    #uma forma de chamar a função

print ('A media aritimetica é:', end=" ") # 'end = " " ' serve para imprimir várias palavras na mesma linha
print(f_media(a,b,c)) #jeito mais rápido, mas não é o mais organizado