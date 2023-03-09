"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# Definindo variável de condição
condicao = True

# Inicializando variável de verificação do if
passou_if = None

# Verificando a condição
if condicao:
    passou_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# Imprimindo o valor da variável passou_if e verificando se é None ou não
print(passou_if, passou_if is None)
print(passou_if, passou_if is not None)

# Verificando se a variável passou_if é None ou não e imprimindo uma mensagem correspondente
if passou_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
