# Definindo a string a ser analisada
frase = 'eeee oooo uuuu'

# Inicializando variáveis
i = 0  # contador para percorrer a string
saida = ""  # string para armazenar a frase sem a letra mais comum
letra = ""  # variável auxiliar para armazenar cada letra da string
qtd_apareceu_mais_vezes = 0  # variável para armazenar a quantidade de vezes que a letra mais comum apareceu
maior_letra = ''  # variável para armazenar a letra mais comum encontrada até o momento
ja_contabilizadas = set()  # conjunto para armazenar letras já contabilizadas
empates = []  # lista para armazenar letras que aparecem a mesma quantidade de vezes que a letra mais comum


# Loop para percorrer a string
while i<len(frase):
    # Se o caractere atual for um espaço em branco, adiciona um espaço em branco à variável 'saida'
    if frase[i] == " ":
        saida += " "
    else:
        letra_atual = frase[i]  # Armazena a letra atual em uma variável auxiliar
        # Se a letra atual ainda não foi contabilizada, conta quantas vezes ela aparece na string
        if letra_atual not in ja_contabilizadas:
            conta_letra = frase.count(letra_atual)
            ja_contabilizadas.add(letra_atual)  # Adiciona a letra atual ao conjunto de letras já contabilizadas
            # Se a quantidade de vezes que a letra atual aparece na string é maior do que a quantidade que a letra mais comum apareceu até o momento,
            # atualiza as variáveis 'qtd_apareceu_mais_vezes' e 'maior_letra', e limpa a lista de empates
            if conta_letra > qtd_apareceu_mais_vezes:
                qtd_apareceu_mais_vezes = conta_letra
                maior_letra = letra_atual
                empates = []
            # Se a quantidade de vezes que a letra atual aparece na string é igual à quantidade que a letra mais comum apareceu até o momento,
            # adiciona a letra atual à lista de empates
            elif conta_letra == qtd_apareceu_mais_vezes:
                empates.append(letra_atual)

    i+=1  # Incrementa o contador

# Imprime a letra mais comum e a quantidade de vezes que ela apareceu na string
print('A letra que mais apareceu foi '
      f'[{maior_letra}] e a quantidade foi de '
      f'[{qtd_apareceu_mais_vezes}] vezes')

# Se houver empate, imprime as letras que empataram
if len(empates) > 0:
    print('Empate entre as letras:')
    for letra in empates:
        print(f'[{letra}][{qtd_apareceu_mais_vezes}]')


    