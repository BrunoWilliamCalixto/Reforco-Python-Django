"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Entre com um número desejado: ')
try:
    numero_int = int(numero)
    numero_int = (numero_int  % 2 == 0)
    if numero_int:
        print('este número é par')
    else:
        print('Este número é impar')

except:
    print('Este não é um número válido')
    
print(100*'-')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Informe um horarío: ')
try:
    horario_float = float(horario)

    if horario_float >= 0 and horario_float < 12:
        print('Bom dia!')
    elif horario_float > 12 and horario_float < 18:
        print('Boa tarde')
    elif horario_float > 18 and horario_float < 24:
        print('Boa noite')
    
    else:
        print('Não reconheço esse horário')
    
except:
    print('Não conheço esse horário')

print(100*'-')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
quantidade_letras = len(nome)
NOME_CURTO = 1 < quantidade_letras <= 4
NOME_NORMAL = quantidade_letras > 4 and quantidade_letras <=6
NOME_GRANDE = quantidade_letras > 6

if ' ' in nome:
    print('Este nome contém espaços')
    exit()

elif  NOME_CURTO:
    print('Seu nome é curto')

elif NOME_NORMAL:
    print('Seu nome é normal')

elif NOME_GRANDE:
    print('Seu nome é grande')

else:
    print('Digite um nome maior que 1 letra')
