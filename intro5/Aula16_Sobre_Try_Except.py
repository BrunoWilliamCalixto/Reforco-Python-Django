numero_str = input('Vou dobrar o número que voce digitar: ') # String digitada pelo usuário

try:
    numero_float = float(numero_str) #conversão de string para um numero do tipo float
    print(f'O dobro do valor é {numero_float*2:.2f}') # Exibe a mensagem caso não haja erro de exceções
except:
    print('Isso não é um número') # Se houver um erro de exceções, ele retorna a mensagem, impedindo que o programa se quebre
