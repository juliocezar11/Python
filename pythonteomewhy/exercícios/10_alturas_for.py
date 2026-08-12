# %%
# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

soma = 0 # valor final

qntde_entradas = 4 # contador de entradas

for i in range(qntde_entradas):
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    qntde_entradas -= 1 

print("soma das alturas: ", soma)

