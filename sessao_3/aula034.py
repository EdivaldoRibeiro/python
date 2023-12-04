print('=======CASO1======')
condicao=True
contador=0
while condicao:
    contador+=1
    opcao=input("Digite [S] quando desejar sair: ")
    if opcao[0] == 's' or opcao[0] == 'S':
        condicao=False
        print(f'Saindo do loop {contador}')
    else:
        print(f'Continuando no loop {contador}')

print('=======CASO2======')
contador=0
condicao = True
while condicao:
    contador+=1
    condicao = contador < 10
    print(f'Loop vai continar enquanto {contador} < 10 [{condicao}]')

print('=======CASO3======')
contador=0
condicao = True
while condicao:
    contador+=1
    condicao = contador < 10
    if not condicao:
        print(f'Saindo forcado do loop {contador} < 10 [{condicao}]')
        break
    else:
        print(f'Loop vai continar enquanto {contador} < 10 [{condicao}]')

"""
Exibe ao executar:

=======CASO1======
Digite [S] quando desejar sair: s
Saindo do loop 1
=======CASO2======
Loop vai continar enquanto 1 < 10 [True]
Loop vai continar enquanto 2 < 10 [True]
Loop vai continar enquanto 3 < 10 [True]
Loop vai continar enquanto 4 < 10 [True]
Loop vai continar enquanto 5 < 10 [True]
Loop vai continar enquanto 6 < 10 [True]
Loop vai continar enquanto 7 < 10 [True]
Loop vai continar enquanto 8 < 10 [True]
Loop vai continar enquanto 9 < 10 [True]
Loop vai continar enquanto 10 < 10 [False]
=======CASO3======
Loop vai continar enquanto 1 < 10 [True]
Loop vai continar enquanto 2 < 10 [True]
Loop vai continar enquanto 3 < 10 [True]
Loop vai continar enquanto 4 < 10 [True]
Loop vai continar enquanto 5 < 10 [True]
Loop vai continar enquanto 6 < 10 [True]
Loop vai continar enquanto 7 < 10 [True]
Loop vai continar enquanto 8 < 10 [True]
Loop vai continar enquanto 9 < 10 [True]
Saindo forcado do loop 10 < 10 [False]
"""
