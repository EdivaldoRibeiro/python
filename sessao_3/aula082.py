#Só use lambda se for de fácil compreensao

def executa(funcao, *args):
    return funcao(*args)


print(executa(lambda x, y : x + y, 10, 2))

duplica=executa(lambda m: lambda n: m*n , 5)

print(duplica(2))

print(executa(lambda *args: sum(args), 1,2,3,4,5,6,7,8))

"""
Exibe ao executar:

12
10
36
"""
