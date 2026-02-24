"""
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
"""

condicao = True
while condicao:
    nome = input('qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print ('acabou')