'''
Faça um programa que vende uma garrafa de água:
Se o cliente escolher água mineral natural, será cobrado R$1,50
Se o cliente escolher água mineral com gás, será cobrado R$2,50
'''
texto = """escolha sua agua mineral para comprar
(1) água mineral natural
(2) água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    print("o valor  da água mineral natural é R$1,50")

elif opcao == "2":
    print("o valor da água mineral com gás R$2,50")

else:
    print("você não escolheu uma opção válida")

