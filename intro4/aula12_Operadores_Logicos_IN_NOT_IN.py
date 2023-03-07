# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1


nome = 'Bruno'
print(nome[2]) #Procure em nome o indice 2
print('u' in nome) # U está entre nome? True
print('b' not in nome) #b minusculo não está entre nome? True

nomeUsuario = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
print(100 * '-')

if encontrar in nomeUsuario: # Se o que eu digitei, estiver entre o meu nome de Usuario
    print(f'{encontrar} está em {nomeUsuario}') # Imprima os devidos valores
else:
    print(f'{encontrar} não está em {nomeUsuario}')
