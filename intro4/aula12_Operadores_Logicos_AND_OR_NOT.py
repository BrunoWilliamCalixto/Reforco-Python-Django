#Avaliação de curto circuito
print(True and 0 and True) # retorna o valor Falsy por conter o 0
print(True or False) # Retorna o valor True
print(False or 0 or 'abc' or False) # Retorna o valor da String por ser um operador verdadeiro

senha = input('Digite sua senha: ') or 'Sem senha' # Condição de um if genérico em uma linha para saciar uma condição
print(senha)
