entrada=input("Digite opcao desejada entre (1-10) para sair digite (0): ")

opcao=-1
if(entrada.isnumeric):
    opcao=int(entrada)
print(f'opcao={opcao}')

if opcao == 0 :                     # Sintaxe do if
    print("saindo do sistema...")   # identar usando TAB
elif opcao > 0 and opcao < 10:
    print(f'voce digitou opcao {opcao}')
else :
    print("Opcao invalida!")

"""
Exibe ao executar:

Digite opcao desejada entre (1-10) para sair digite (0): -1
opcao=-1
Opcao invalida!
"""
