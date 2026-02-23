"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    numero_inteiro = int(input("Digite um número inteiro: "))

    if numero_inteiro % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')

except ValueError:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Que horas são? ')

try:    
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
         print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!!")
    else:
        print('Você no digitou um horário válido')
except:
    print('Digite números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Qual o seu primeiro nome? ')
nome = entrada
nome_len = len(nome)
if nome_len > 1:
    if nome_len <= 4:
        print(f'Seu nome é curto, tem {nome_len} letras.')
    elif nome_len >= 5 or nome_len >= 6:
            print(f'Seu nome é normal, tem {nome_len} letras.')
    elif nome_len > 6:
        print(f'Seu nome é grande, tem {nome_len} letras.')
else:
    print('Digite mais de uma letra')
