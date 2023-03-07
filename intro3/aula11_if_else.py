numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

entrada = input('Você deseja "Somar", "Multiplicar" ou "Subtrair"? ')

if entrada == 'Somar':
    resultado = numero_1 + numero_2
    print(f'O resultado é {resultado}')

elif entrada == 'Multiplicar':
    resultado = numero_1 * numero_2
    print(f'O resultado é {resultado}')

elif entrada == 'Subtrair':
    resultado = numero_1 - numero_2
    print(f'O resultado é {resultado}')

else:
    print('Comando invalido')

