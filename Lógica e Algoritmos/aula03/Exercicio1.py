# Variável contendo a soma dos valores
soma = 0

# Variável para obter um número
numero = -1

# Laço (while)
while numero != 0:
    
    # Pedir um número ao cliente
    print("Informe um número")
    numero = int(input())

    # Realizar a soma
    soma += numero

# Exibir a soma
print("A soma dos valores é " + str(soma))