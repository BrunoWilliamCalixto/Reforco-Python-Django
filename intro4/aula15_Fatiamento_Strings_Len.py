"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(len(variavel))

print(variavel[0:len(variavel):1]) #Imprima variavel com [indice 0: até 9 de Olá mundo: e percorra de 1 em 1]
print(variavel[-1:-len(variavel):-1]) # Imprima a variável com [Indice -1 até o -10 de Olá Mundo invertido, e percorra de -1 em -1]
        #Primeiro numero: Começo, segundo: final, terceiro: