# pede o número ao usuário
num = int(input("Digite um número: "))

# inicializa as variáveis com os valores iniciais da sequência de Fibonacci
a, b = 0, 1

# loop para gerar a sequência de Fibonacci até encontrar um número maior ou igual ao número informado pelo usuário
while b < num:
    a, b = b, a + b

# verifica se o número informado pelo usuário está na sequência de Fibonacci
if b == num:
    print(f"{num} pertence à sequência de Fibonacci")
else:
    print(f"{num} não pertence à sequência de Fibonacci")
