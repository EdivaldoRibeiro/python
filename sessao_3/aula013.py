nome="Edivaldo Ribeiro"
peso=83
altura=1.72
imc=...                     #isso nao gera erro, é um Ellipsis, ou seja, será atribuido depois
imc=peso/altura**2

exibir=f"{nome} tem imc {imc:.2f}"  #Formatacao de string
print(exibir)


exibir=f"{nome} pesa {peso} kilos e tem {altura:.2f} metros de altura, imc {imc:.2f}"
print(exibir)

"""
Exibe ao executar:

Edivaldo Ribeiro tem imc 28.06
Edivaldo Ribeiro pesa 83 kilos e tem 1.72 metros de altura, imc 28.06
"""
