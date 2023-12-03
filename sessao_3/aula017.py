condicao1=5
condicao2=2

resp=False
if condicao1==1:
    print("condicao1 do if")
    resp=True
else:
    print("nao atende condicao1 do if")

if condicao2==2:
    print("condicao2 do if")
    resp=True
else:
    print("Nao atende condicao2 do if")

if resp:
    if condicao1==1 or condicao2==2:
        print("condicao1 ou condicao2 do if")

    if condicao1==1 and condicao2==2:
        print("condicao1 e condicao2 do if")
else:
    print("fora de condicao1 e condicao2 do if")

print("fora do if")


"""
Exibe ao executar:

nao atende condicao1 do if
condicao2 do if
condicao1 ou condicao2 do if
fora do if
"""
