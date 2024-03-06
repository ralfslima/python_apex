# Perguntando e armazenando um número
print("Informe um número")
numero = int(input())

# Variável para armazenar o resultado
valor = 0

# Variável para armazenar o índice
indice = numero - 1

# Laço de repetição
while indice > 1:

    # Cálculo
    if numero-1 == indice:
        valor = numero * indice
    else:
        valor = valor * indice

    # Decremento
    indice-=1

# Exibir o fatorial
print("O fatorial de " + str(numero) + " é " + str(valor))