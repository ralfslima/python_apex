# Varável nome
nome = ""

#Lista de nomes
lista = []

# Laço de repetição
while nome.lower() != "sair":

    # Obter um nome
    print("Informe um nome ou sair")
    nome = input()

    # Armazenar nome na lista
    if nome.lower() != "sair":
        lista.append(nome)

# Divisão
print("-----------------------")

# Exibir nomes armazenados
for n in lista:
    print(n)