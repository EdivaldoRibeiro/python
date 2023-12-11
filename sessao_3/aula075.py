DUPLICAR=2
TRIPLICAR=3
QUADRUPLICAR=4

def operacao(oper):
    def calculo(valor):
        return oper*valor
    return calculo

valor=100
dup=operacao(DUPLICAR)
tri=operacao(TRIPLICAR)
qua=operacao(QUADRUPLICAR)

print(f'Duplicar {valor:05d} = {dup(valor):05d}')
print(f'Triplicar {valor:05d} = {tri(valor):05d}')
print(f'Quadruplicar {valor:05d} = {qua(valor):05d}')

"""
Exibe ao executar:

Duplicar 00100 = 00200
Triplicar 00100 = 00300
Quadruplicar 00100 = 00400
"""
