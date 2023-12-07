resp='abacaxi' if True else 'abobrinha'
print(f"ternário: 'abacaxi' if True else 'abobrinha' - resultado:{resp}")

resp='mane' if 'mane' == 'MANE'.lower() else 'manoel'
print(f"ternário: 'mane' if 'mane' == 'MANE'.lower() else 'manoel' - resultado: {resp}")

resp='Mane' if 'Mane' == 'MANE'.lower() else 'Manoel'
print(f"ternário: 'Mane' if 'Mane' == 'MANE'.lower() else 'Manoel' - resultado: {resp}")

for numero in range(11):

    resp='ZERO' if numero==0 else \
        'UM' if numero==1 else \
        "DOIS" if numero==2 else \
        'TREIS' if numero==3 else \
        'QUATRO' if numero==4 else \
        'CINCO'if numero==5 else \
        'SEIS' if numero==6 else \
        'SETE' if numero==7 else \
        'OITO' if numero==8 else \
        'NOVE' if numero==9 else 'Inválido'
    print(f'numero:{numero} - {resp}')

"""
Exibe ao executar:

ternário: 'abacaxi' if True else 'abobrinha' - resultado:abacaxi
ternário: 'mane' if 'mane' == 'MANE'.lower() else 'manoel' - resultado: mane
ternário: 'Mane' if 'Mane' == 'MANE'.lower() else 'Manoel' - resultado: Manoel
numero:0 - ZERO
numero:1 - UM
numero:2 - DOIS
numero:3 - TREIS
numero:4 - QUATRO
numero:5 - CINCO
numero:6 - SEIS
numero:7 - SETE
numero:8 - OITO
numero:9 - NOVE
numero:10 - Inválido
"""
