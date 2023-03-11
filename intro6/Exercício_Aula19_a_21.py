"""Calculadorra com While"""
condicao = True
resultado = 0
numero_valido = None
apenas_numeros = 1234567890
       

while condicao:
        numero1 = input('Digite um numero: ')
        numero2 = input('Digite outro numero: ')
       
        try:
            numero1_int = int(numero1)
            numero2_int = int(numero2)
            numero_valido = True
            operador = input('Digite qual operação será realizada: "/, *, +, -": ')
            operadores_permitidos = '/*-+'
            caracteres = '.,'

            if operador == '/':
                resultado = numero1_int / numero2_int
            
            if operador == '*':
                resultado = numero1_int * numero2_int
            
            if operador == '+':
                resultado = numero1_int + numero2_int
            
            if operador == '-':
                resultado = numero1_int - numero2_int

            if operador in caracteres:
                 print('Caracteres (,.) são invalidos! Apenas /, *, +, -"')
                 continue

            if len(operador) > 1:
                 print('Por favor, digite apenas 1 operador')
                 continue

            if operador not in operadores_permitidos:
                 print('Operador inválido')
        
            print(f'Resultado {resultado}')
            ##############                         #Converta para letra minuscula         
            sair = input('Você deseja sair? [s]im ou [n]ão: ').lower().startswith('s') #começa com 's'
            if sair is True:
                break
        except:
            ...
        if numero_valido is None:
                print('Um ou ambos os números não são válidos')
                continue
        
        if sair is True:
            break

    

    
    

