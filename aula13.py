#exercício de imc 

nome = "Julio"
altura = 1.70
peso = 80

linha_1 = f"{nome} tem {altura: .2f}m de altura e pesa {peso}kg"
print(linha_1)


imc = peso / altura ** 2
print(imc)

linha_2 = f"Olá, {nome} seu imc é {imc: .3f}"
print(linha_2)