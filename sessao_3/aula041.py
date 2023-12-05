BUSCA='x'
nome='Edivaldo Ribeiro'
idx=0
encontrou=True
while idx<len(nome):
    caracter=nome[idx].lower()
    if caracter == BUSCA:
        break
    idx+=1
else:
    encontrou=False

if encontrou:
    print(f'Encontrado "{BUSCA}" em "{nome}"')
else:
    print(f'Nao encontrou "{BUSCA}" em "{nome}"')


"""
Exibe ao executar:

Nao encontrou "x" em "Edivaldo Ribeiro"
"""
