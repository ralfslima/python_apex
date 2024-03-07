# Importar pacote de tempo (data/hora)
import datetime

# Exibir data e hora
print(datetime.datetime.now())

# Exibir apenas data (dia-mês-ano)
informacao_atual = datetime.datetime.now()
print(informacao_atual.strftime('%d/%m/%Y'))