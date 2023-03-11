condicao = True
name = 0
while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')
    print(100 * '-')
    name += 1

    if ' ' in nome:
        condicao = False

print('Vezes que foram repetidas: ', name)

contador = 0
numero = int(input('Digite um número: '))
while contador <= 10:
    resultado = contador * numero
    print(f'{contador} X {numero} = {resultado}')
    contador += 1