def calculo(valor, taxa, acrescimo, desconto=None):
    total=valor*taxa/100+acrescimo
    if desconto is not None:
        total=total-desconto
        print(f'valor={valor:02f} taxa={taxa:.02f} acrescimo={acrescimo:.02f} desconto={desconto:.02f} total:{total:.02f}')
    else:
        print(f'valor={valor:02f} taxa={taxa:.02f} acrescimo={acrescimo:.02f} total:{total:.02f}')
    
    return total

valor=100.0
taxa=15.0
acrescimo=3.0
desconto=1.5

print(f'resposta1:{calculo(valor, taxa, acrescimo):.02f}')
print(f'resposta2:{calculo(valor, taxa=taxa, acrescimo=acrescimo):.02f}')
print(f'resposta3:{calculo(acrescimo=acrescimo, taxa=taxa, valor=valor):.02f}')
print(f'resposta4:{calculo(acrescimo=acrescimo, taxa=taxa, valor=valor, desconto=desconto):.02f}')
print(f'resposta5:{calculo(valor, taxa, acrescimo=acrescimo, desconto=desconto):.02f}')

"""
Exibe ao executar:

valor=100.000000 taxa=15.00 acrescimo=3.00 total:18.00
resposta1:18.00
valor=100.000000 taxa=15.00 acrescimo=3.00 total:18.00
resposta2:18.00
valor=100.000000 taxa=15.00 acrescimo=3.00 total:18.00
resposta3:18.00
valor=100.000000 taxa=15.00 acrescimo=3.00 desconto=1.50 total:16.50
resposta4:16.50
valor=100.000000 taxa=15.00 acrescimo=3.00 desconto=1.50 total:16.50
resposta5:16.50
"""
