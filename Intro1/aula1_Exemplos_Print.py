#Permite que escrevemos um comentário referênte ao nosso código
'''@docString que permite que possamos 
pular uma linha para realizar devidos esclarecimentos do documento'''

print("Ta valendo", 12, sep="-") #a concatenação é separada por vírgula
print("Ta valendo", 12, sep="-") # sep="" é um método que define como a concatenação pode funcionar

numero1 = 22
numero2 = 44
resultado = numero1 + numero2

print("Total do resultado", resultado, sep=": ") #formatação do separador

#end interpreta como será o fim do print
print("Números utilizados", numero1, numero2, sep=": ", end="##\n") #\n ainda sim realiza uma quebra de linha, assim como porderíamos utilizar a formação padrão para não quebrar essa linha