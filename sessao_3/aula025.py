#Testando interpolacao
# s   --> string
# f   --> float
# d,i --> inteiro
# x,X --> hexadecimal

nome="Edivaldo"
preco=2501.015678
format='%s preço é R$ %.2f' % (nome, preco)
print(format)

print('valor de %d em hexadecimal é %04x' % (255,255))
print('valor de %d em hexadecimal é %04X' % (255,255))

"""
Exibe ao executar:

Edivaldo preço é R$ 2501.02
valor de 255 em hexadecimal é 00ff
valor de 255 em hexadecimal é 00FF
"""
