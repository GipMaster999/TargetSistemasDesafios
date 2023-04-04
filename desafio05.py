# define uma string diretamente no código
string = "Exemplo de string para inverter"

# inicializa uma string vazia para armazenar a string invertida
string_invertida = ""

# percorre a string de trás para frente e adiciona cada caractere na string invertida
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# imprime a string invertida
print("String invertida:", string_invertida)
