# Vetor para armazenar diversos dados
# Para manipular listas, utilizandos índices
nomes = ['Ralf', 'Ana', 'Cristina', 'Pablo']

# Adicionar um novo nome
nomes.append('Luciana')

# Alterar o nome da segunda pessoa
nomes[1] = 'Aline'

# Remover a terceira pessoa da lista
# Opções para remover
    # nomes.remove("Cristina")
    # nomes.pop(2)
    # nomes.pop() // Remove o último nome
nomes.pop(2)

# Exibir nomes
#for n in nomes:
#    print(n)

indice = 0
while indice < len(nomes):
    print(nomes[indice])
    indice += 1


# SISTEMA CRUD
# Create (inserir)
# Read   (ler)
# Update (alterar)
# Delete (remover)