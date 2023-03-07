# Formatação de Strings
# Tudo em Python é um objeto
# Objetos tem métodos dentro dele
# Métodos tem suas próprias ações e finalidades

a = 'A'
b = 'B'
c = 1.1

string = 'a= {1} b= {0} c= {2:.2f}' # Instância de chaves que reservam sua respectivas ordens de formatação
string1 = 'a= {nome1} b= {nome2} c= {nome3:.2f}'
# Método com a, b, c, passados como parâmetros
formato = string.format(a,b,c) #string instanciada com um objeto, e o format passando como argumento a ordem que será colocada na chave 

formato1 = string1.format(nome1=a, nome2=b, nome3=c) #Parâmetro nomeado


print(formato)
print(formato1)