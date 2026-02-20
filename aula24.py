# Operadores in e not in
# String não iteráveis -> navega item por item
# 0 1 2 3 4 
# J u l i o 
# -5-4-3-2-1


nome = 'Julio'
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])


print('J' in nome)
print('C' in nome)
print('Jul' in nome)
print('cezar' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')

