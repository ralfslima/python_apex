# Condicional simples
idade = 25

if idade >= 18:
    print("Pode obter a CNH")
else:
    print("Não pode obter a CNH")

# Condicional aninhada/composta
media = 8.5

if media == 10:
    print("Nota máxima! Parabéns")
elif media >= 9:
    print("Ótimo!")
elif media >= 8:
    print("Bom!")
elif media >= 7:
    print("Na média!")
elif media >= 5:
    print("Em exame")
else:
    print("Reprovado")

# Operadores lógicos
valor = 84

if valor >= 0 and valor <= 100:
   print("O valor está entre 0 e 100")
else:
    print("O valor não está entre 0 e 100")

print("Informe o valor da compra")
total = float(input())
formaPagamento = "a prazo"

if total >= 100 or formaPagamento == "a vista":
    print("Valor a pagar R$"+str(total * 0.9))
else:
    print("O valor a pagar R$"+str(total))