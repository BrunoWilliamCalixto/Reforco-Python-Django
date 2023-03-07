"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}') # Pad que coloca uma largura fix de caracteres na variável
                    # > sinal de 10 caracteres para esquerda

print(f'{variavel: <10}') 
                    # < sinal de 10 caracteres para direita
print(f'{variavel: ^11}') 
                    # ^ sinal de caractere centralizado

print(f'{variavel:$^11}') 
                    # Preenchimento de caractere com $

print(f'{1000.234897237:.1f}') # Formatação de um número com 1 ponto flutuante

hexadecimal = int(input('Digite um valor para conversão hexadecimal: '))
print(f'O hexadecimal de {hexadecimal} é {hexadecimal:08X}')