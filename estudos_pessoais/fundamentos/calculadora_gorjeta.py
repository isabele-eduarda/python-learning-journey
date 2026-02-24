'''
Imagine que você foi jantar e quer saber quanto deve deixar de gorjeta sem ter que fritar o cérebro com porcentagem.
O que o seu script deve fazer:
Pedir para o usuário digitar o valor total da conta (ex: 50.00).
Calcular quanto seria 10% desse valor.
Exibir na tela uma mensagem amigável dizendo o valor da gorjeta e o total final (conta + gorjeta).
💡 Dicas de Ouro para não travar:
O "Pulo do Gato" do Input: O comando input() sempre recebe o que você digita como texto (string). Para fazer contas, você precisa transformar esse texto em um número decimal (float).
Exemplo: valor = float(input("Digite o valor: "))
Matemática: Para achar 10%, basta multiplicar o valor por 0.10.
Organização: Use nomes de variáveis que façam sentido, como conta, gorjeta e total.

'''
conta= float(input("Digite o valor da conta: "))
gorjeta = conta * 0.10; total = gorjeta + conta;
print ("O valor da gorjeta é: R$", gorjeta, "e o total da conta é: R$", total)

