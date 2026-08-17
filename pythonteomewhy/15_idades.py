# %%

idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print(idades)
print("Média: ", media)
print("Mínimo: ", minimo)
print("Máximo: ", maximo)
print("Quantidade: ", qtde)




# %%
