# Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista. Solicite ao usuário um número e exiba a contagem.
lista = [1,2,2,1,1,1,1,1,5,6,1,6,7,8,9,9,1 ]

numero = input("entre com um número: ")
numero = int(numero)
contador = 0
for i in lista:
    if i == numero:
        contador += 1 

print("quantidade de", numero, ":", contador)

