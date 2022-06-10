#06 crie um algoritmo que receba um número,conte o número total de digitos e mostre o resultado.por exemplo,se o número é 2021,então a saída deve ser 4

print('\t----contagem dos dígitos----')
digitos = int(input("digite um número para contar seus dígitos: "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador += 1
print("total de dígitos = ",contador)
print("\n")

#-----------------------#-------------------------------#
#05faça um programa que recebendo um valor inteiro,informe se o numero e positivo,negativo ou neutro.

print('\t----a danca dos numeros----')
x = int(input("informe um numero para brincar : "))
if x < 0:
        print('e um numero negativo ')
elif x == 0:
        print('e um numero neutro')
elif x > 0:
        print('e um numero positivo')
print("\n")

#-----------------------#-------------------------------#
#04 faça um programa que receba um numero digitado pelo usuario e calcule a soma de todos os numeros de 1 ate ao numero digitado.por exemplo,se o usuario digitou o numero 4,a saida deve ser 10 ->(1+2+3+4=10)

print('\t----soma de 1 ate o valor digitado----')
soma_numeros = 0
numero = int(input("por favor, insira um numero: "))
for i in range(1, numero + 1, 1):
    soma_numeros += i
print("a soma e =", soma_numeros)
print("\n")
#-----------------------#-------------------------------#
#03 escreva um programa que mostre todos os números entre 5 e 100 que são divisiveis por 7, mas não são múltiplos de 5. os números obtidos devem ser impressos em sequência.

print('\t-- números entre 5 e 100 que são divisiveis por 7--')
for num in range(5,100):
    if (num %7 == 0 and num % 5 != 0):
        print(num)
print("\n")

#-----------------------#-------------------------------#
#Questão 2
print('\t----calculo do novo salario----')
salario_atual = float(input('informe o salario atual:'))

if (salario_atual<500):
    salario_novo=salario_atual+(salario_atual*0.15)
    print('salario com reajuste = ',salario_novo)

if ((salario_atual>=500) and (salario_atual <=1000)):
    salario_novo=salario_atual+(salario_atual*0.10)
    print('salario com reajuste = ',salario_novo)

if (salario_atual>1000):
    salario_novo=salario_atual+(salario_atual*0.05)
    print('salario com reajuste =',salario_novo)
print("\n")
#-----------------------#-------------------------------#
#01 faça um programa em python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

print('\t----tabuada----')
numero = int(input('informe o numero para ver a tabuada: '))

print('\ntabuada de',numero,':')

for i in range(1, 11):
    print(numero,'x',i,'=',(numero * i))
print("\n")