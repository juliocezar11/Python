"""
Docstring for aula25
interpolação básica de string
s - string
d e i int
f float
x e X hexadecimal (ABCDEF0123456789)
"""

nome = "julio"
preco = 1000.986763
variavel = "%s, o preço é R$%.5f" % (nome, preco)
print(variavel)
print("O Hexadecimal é %d é %04x" % (15, 15 ))
