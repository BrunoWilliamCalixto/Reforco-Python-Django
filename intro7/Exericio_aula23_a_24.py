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

# Define a palavra secreta
palavra_secreta = "abacaxi"

# Define a lista para armazenar as letras adivinhadas
letras_adivinhadas = []

# Define o número máximo de tentativas
num_tentativas_max = 6

# Define o número de tentativas atual
num_tentativas_atual = 0

# Loop principal
while True:
    # Verifica se o número máximo de tentativas foi atingido
    if num_tentativas_atual == num_tentativas_max:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)
        break

    # Verifica se todas as letras da palavra secreta foram adivinhadas
    if all(letra in letras_adivinhadas for letra in palavra_secreta):
        print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
        break

    # Pede ao usuário para digitar uma letra
    letra = input("Digite uma letra: ")

    # Verifica se a letra já foi adivinhada
    if letra in letras_adivinhadas:
        print("Você já tentou essa letra antes. Tente outra letra.")
        continue

    # Adiciona a letra adivinhada à lista de letras adivinhadas
    letras_adivinhadas.append(letra)

    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        print("A letra", letra, "está na palavra secreta.")
    else:
        print("A letra", letra, "não está na palavra secreta. Tente novamente.")
        num_tentativas_atual += 1

    # Imprime as letras adivinhadas até agora
    letras_corretas = [letra if letra in letras_adivinhadas else "*" for letra in palavra_secreta]
    print("Palavra secreta:", "".join(letras_corretas))




  