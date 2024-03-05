# Obter número inicial
print("Informe o número inicial")
inicio = int(input())

# Obter número final
print("Informe o número final")
termino = int(input())

# Divisão
print("-----------------")

# Laço While
while inicio <= termino:

    # Condicional para verificar se é par
    if inicio % 2 == 0:
        print(inicio)

    # Incremento
    inicio+=1