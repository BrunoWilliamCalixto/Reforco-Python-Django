# Define a string contendo o nome completo
nome = "Bruno William Calixto"

# Inicializa uma variável de controle de loop i com valor 0
i = 0

# Inicializa uma string vazia para armazenar a saída
saida = ""

# Enquanto i for menor que o comprimento do nome
while i < len(nome):

    # Verifica se a letra atual é um espaço em branco
    if nome[i] == " ":

        # Se for um espaço em branco, adiciona um espaço à saída
        saida += " "

    else:
        # Caso contrário, adiciona o índice correspondente entre colchetes à saída
        saida += f"[{nome[i]}]"

    # Incrementa o valor da variável de controle de loop i em 1
    i += 1

# Imprime a string de saída sem adicionar uma quebra de linha no final
print(saida, end="")