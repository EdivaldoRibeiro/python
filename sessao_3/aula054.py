produtos=[]
produto=''
while 'sair' != produto.lower():
    print("================================================")
    print("Digite <SAIR> para encerrar o programa")
    while True:
        produto=input('Digite um produto, <ENTER> para sair: ')
        if not produto or (produto and 'sair' == produto.lower()):
            break
        elif produto:
            produtos.append(produto)
            for id, produto in enumerate(produtos):
                print(f'{id:02d} - {produto}')
    
    if produto and 'sair' == produto.lower():
        continue

    while True:
        for id, produto in enumerate(produtos):
            print(f'{id:02d} - {produto}')

        produto=input('Informe indice do produto que deseja excluir, <ENTER> para sair: ')
        if not produto or (produto and 'sair' == produto.lower()):
            break

        if produto:
            try:
                idx=int(produto)
                if idx >= 0 and idx <= len(produtos):
                    produtos.pop(idx)
            except:
                print(f'Produto inválido')
print(f'Lista final da compra:')
if len(produtos) > 0:
    for id, produto in enumerate(produtos):
        print(f'{id:02d} - {produto}')
else:
    print("Lista esta vazia...")

"""
Exibe ao executar:

================================================
Digite <SAIR> para encerrar o programa
Digite um produto, <ENTER> para sair: Arroz
00 - Arroz
Digite um produto, <ENTER> para sair: Feijao
00 - Arroz
01 - Feijao
Digite um produto, <ENTER> para sair: Laranja
00 - Arroz
01 - Feijao
02 - Laranja
Digite um produto, <ENTER> para sair: Jaba
00 - Arroz
01 - Feijao
02 - Laranja
03 - Jaba
Digite um produto, <ENTER> para sair: 
00 - Arroz
01 - Feijao
02 - Laranja
03 - Jaba
Informe indice do produto que deseja excluir, <ENTER> para sair: 2
00 - Arroz
01 - Feijao
02 - Jaba
Informe indice do produto que deseja excluir, <ENTER> para sair: 2
00 - Arroz
01 - Feijao
Informe indice do produto que deseja excluir, <ENTER> para sair: 
================================================
Digite <SAIR> para encerrar o programa
Digite um produto, <ENTER> para sair: sair
Lista final da compra:
00 - Arroz
01 - Feijao
"""
