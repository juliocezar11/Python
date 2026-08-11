#Altere o programa anterior para considerar a quantidade de garrafas de água

texto = """escolha sua agua mineral para comprar
(1) água mineral natural
(2) água mineral com gás
"""

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5


if valor_item == 0:
    print("digite um numero válido")


else: 
    qtde = input("quantas garafas?")
    qtde = int(qtde)
    valor_total = qtde * valor_item
    print("a sua conta deu ", valor_total)