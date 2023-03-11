"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

# Define a palavra secreta
palavra_secreta = 'perfume'

# Cria uma variável para salvar as letras digitadas corretamente
salvar_letra_digitada = ''

# Define a quantidade de tentativas
numero_tentativas = 6

# Inicializa um contador de tentativas
i = 1

# Loop principal do jogo
while True:
    
    # Solicita ao usuário para digitar uma letra
    letra_digitada = input('Digite uma letra: ')

    # Verifica se o usuário digitou mais de uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    # Verifica se a letra digitada está na palavra secreta
    if letra_digitada in palavra_secreta:
        salvar_letra_digitada += letra_digitada

    # Verifica se o usuário digitou a letra "z" para sair do jogo
    if letra_digitada == 'z':
        break
    
    # Inicializa uma variável para formar a palavra com as letras digitadas corretamente
    palavra_formada = ''
    
    # Loop para percorrer cada letra da palavra secreta
    for letra_secreta in palavra_secreta:
        # Verifica se a letra secreta está na lista de letras digitadas corretamente
        if letra_secreta in salvar_letra_digitada:
            # Se estiver, adiciona a letra à palavra formada
            palavra_formada += letra_secreta
        else:
            # Se não estiver, adiciona o caractere "*" à palavra formada
            palavra_formada += '*'
    
    # Verifica se o usuário acertou a palavra
    if palavra_formada == palavra_secreta:
        # Se acertou, exibe uma mensagem de parabéns e encerra o jogo
        os.system('cls')
        print('Parabens, você ganhou o jogo!')
    
    # Incrementa o contador de tentativas
    i += 1

    # Verifica se o usuário ultrapassou o número máximo de tentativas
    if i == len(palavra_secreta):
        # Se ultrapassou, exibe uma mensagem informando que perdeu e a palavra secreta
        print('Você perdeu')
        print(f'A palavra formada era {palavra_secreta}')
        break

    # Exibe a palavra formada
    print(palavra_formada)