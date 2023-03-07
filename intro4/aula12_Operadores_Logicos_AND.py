# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)

entrada = input('[E]ntrar  [S]air: ')
senha_permitida = '123456'
if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Digite sua senha: ')
    if not senha_digitada :
        print('Você não digitou a senha')

    if senha_digitada == senha_permitida :
        print('Acesso permitido')
    else:
        print('**Acesso negado**')

elif entrada == 'S' :
    print('saindo do programa')
    exit()


else :
    print('Comando Invalido')

if senha_digitada == senha_permitida and entrada == 'E' or entrada == 'e':
    print(100 * '-')
    print('Seja bem vindos ao nosso sistema')


