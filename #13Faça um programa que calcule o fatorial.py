#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def fatorial(numero):
    resultado= 1
    for i in range(1,numero+1):
        resultado= resultado*i
    return resultado

numero= int(input('Informe o número:'))
valor= fatorial(numero)
print("o fatorial é ", valor)