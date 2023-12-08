def calculo(valor, taxa, acrescimo):
    total=valor*taxa/100+acrescimo
    print(f'valor={valor:02f} taxa={taxa:.02f} acrescimo={acrescimo:.02f} total:{total:.02f}')
    return total

valor=100.0
taxa=15.0
acrescimo=3.0

print(f'resposta1:{calculo(valor, taxa, acrescimo):.02f}')
print(f'resposta2:{calculo(valor, taxa=taxa, acrescimo=acrescimo):.02f}')
print(f'resposta3:{calculo(acrescimo=acrescimo, taxa=taxa, valor=valor):.02f}')

"""
Exibe ao executar:

valor=100.000000 taxa=15.00 acrescimo=3.00 total:18.00
resposta1:18.00
valor=100.000000 taxa=15.00 acrescimo=3.00 total:18.00
resposta2:18.00
valor=100.000000 taxa=15.00 acrescimo=3.00 total:18.00
resposta3:18.00

"""
