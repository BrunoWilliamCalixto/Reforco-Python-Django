# Definindo variáveis
velocidade = 70 # km/h
local_carro = 101 # metros

# Definindo constantes
RADAR_1 = 60 # km/h
LOCAL_1 = 100 # metros
RADAR_RANGE = 1 # metros

# Verificando se o carro passou pelo radar e se estava acima do limite
velocidade_radar_carro = velocidade > RADAR_1

# Verificando se o carro foi multado
carro_foi_multado = (local_carro >= (LOCAL_1 - RADAR_RANGE) and
                     local_carro <= (LOCAL_1 + RADAR_RANGE) and
                     velocidade_radar_carro)

# Imprimindo mensagem de acordo com a verificação
if carro_foi_multado:
    print('Carro multado por alta velocidade')
else:
    print('Sem multa')