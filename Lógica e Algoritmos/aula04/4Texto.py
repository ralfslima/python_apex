# Variável contendo uma frase
frase = 'aprendendo Python na Apex, Python é legal!'

# Contar os caracteres
print('A quantidade de caracteres é ' + str(len(frase)))
print('--------------------------------')

# Obter os caracteres individualmente
for f in frase:
    print(f)
print('--------------------------------')

# Deixar a primeira letra em maiúscula
print(frase.capitalize())
print('--------------------------------')

# Deixar todos os caracteres em maísculo
print('Letras maiúsculas: ' + frase.upper())
print('--------------------------------')

# Deixar todos os caracteres em minúsculo
print('Letras minúsculas: ' + frase.lower())
print('--------------------------------')

# Alterar termos
print('Remover espaços: ' + frase.replace(' ',''))
print('--------------------------------')

# Converter texto em 'vetor'
vetor = frase.split(' ')
print('Tamanho do vetor: ' + str(len(vetor)))