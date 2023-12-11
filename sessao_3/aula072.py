def multiplicacao(*args):
    total=1.0
    for val in args:
        ant=total
        total*=val
        print(f'{val:.02f} * {ant:.02f} = {total:.02f}')
    return total

def is_par(val):
    return val%2==0

def is_impar(val):
    return val%2==1

def paridade(funcao, numero):
    return funcao(numero)

def exibir(msg):
    print(f'-->{msg}')

def exibir_texto(funcao, *args):
    for str in args:
        funcao(str)

print('===========================================')
numeros=1,2,3,4,5,6

calculado=multiplicacao(*numeros)
print(f'Valor retornado da função = {calculado:.02f}')
print(f'O valor calculado {calculado:.02f} é par: {is_par(calculado)}')
print(f'O valor calculado {calculado:.02f} paridade par..: {paridade(is_par, calculado)}')
print(f'O valor calculado {calculado:.02f} paridade impar: {paridade(is_impar, calculado)}')

print('===========================================')
numeros=1,3,5,7,9,11

calculado=multiplicacao(*numeros)
print(f'Valor retornado da função = {calculado:.02f}')
print(f'O valor calculado {calculado:.02f} é par: {is_par(calculado)}')
print(f'O valor calculado {calculado:.02f} paridade par..: {paridade(is_par, calculado)}')
print(f'O valor calculado {calculado:.02f} paridade impar: {paridade(is_impar, calculado)}')

print('===========================================')
texto='Bom dia', 'hello word', 'São Paulo','11-nov-2023', '11:27'
exibir_texto(exibir,*texto)

"""
Exibe ao executar:

===========================================
1.00 * 1.00 = 1.00
2.00 * 1.00 = 2.00
3.00 * 2.00 = 6.00
4.00 * 6.00 = 24.00
5.00 * 24.00 = 120.00
6.00 * 120.00 = 720.00
Valor retornado da função = 720.00
O valor calculado 720.00 é par: True
O valor calculado 720.00 paridade par..: True
O valor calculado 720.00 paridade impar: False
===========================================
1.00 * 1.00 = 1.00
3.00 * 1.00 = 3.00
5.00 * 3.00 = 15.00
7.00 * 15.00 = 105.00
9.00 * 105.00 = 945.00
11.00 * 945.00 = 10395.00
Valor retornado da função = 10395.00
O valor calculado 10395.00 é par: False
O valor calculado 10395.00 paridade par..: False
O valor calculado 10395.00 paridade impar: True
===========================================
-->Bom dia
-->hello word
-->São Paulo
-->11-nov-2023
-->11:27
"""
