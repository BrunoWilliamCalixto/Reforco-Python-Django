primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor= } é maior' 
        f'que {segundo_valor= }'
        )

elif segundo_valor > primeiro_valor:
    print(
        f'{segundo_valor= } é maior' 
        f'que {primeiro_valor= }')

else:
    print('Valores são iguais')

print('-----------------------------------')