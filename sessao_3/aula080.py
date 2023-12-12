import random

def formata(lista):
    resp='['
    for val in lista:
        resp+=f'{int(val):03d} '
    resp+=']'
    return resp

def verify_duplicados(lista, indice):
    set_array=set(lista)
    duplicado=[]
    for num1 in set_array:
        qtd=0
        for num2 in lista:
            if num1 == num2:
                qtd+=1
        if qtd > 1:
            duplicado.append(num1)
    print(f'{idx:02d} - {formata(lista)} -> {formata(duplicado)} duplicados={len(duplicado)}')

lista_de_lista=[]
for _none in range(0,15):
    lista=[]
    for _none in range(0,15):
        num = random.randint(0,100)
        lista.append(num)
    lista_de_lista.append(lista)

for idx, lista in enumerate(lista_de_lista):
    verify_duplicados(lista, idx)

"""
Exibe ao executar:

00 - [087 048 010 096 065 011 002 050 003 036 082 033 063 056 085 ] -> [] duplicados=0
01 - [098 069 019 064 093 059 068 025 040 045 005 006 093 062 084 ] -> [093 ] duplicados=1
02 - [078 048 069 086 081 068 060 098 085 088 035 083 002 006 072 ] -> [] duplicados=0
03 - [099 059 051 020 041 080 033 091 056 013 046 078 025 080 013 ] -> [013 080 ] duplicados=2
04 - [099 023 098 029 059 028 037 016 069 045 078 093 080 059 068 ] -> [059 ] duplicados=1
05 - [095 081 002 010 082 011 008 058 026 017 014 055 056 087 025 ] -> [] duplicados=0
06 - [011 026 008 077 039 075 097 073 007 097 072 036 074 050 069 ] -> [097 ] duplicados=1
07 - [001 056 086 081 081 098 059 042 041 082 076 075 048 012 049 ] -> [081 ] duplicados=1
08 - [089 080 014 023 070 027 068 047 074 098 025 013 026 088 007 ] -> [] duplicados=0
09 - [014 010 095 062 042 038 063 099 005 017 067 004 071 029 099 ] -> [099 ] duplicados=1
10 - [073 015 069 074 053 022 068 050 020 007 030 059 035 071 027 ] -> [] duplicados=0
11 - [076 072 001 018 032 030 032 036 069 099 089 027 021 043 088 ] -> [032 ] duplicados=1
12 - [081 031 060 019 085 086 098 060 063 069 064 006 016 006 047 ] -> [006 060 ] duplicados=2
13 - [067 010 015 076 089 043 006 072 075 100 073 049 070 008 095 ] -> [] duplicados=0
14 - [071 041 097 008 034 076 056 049 095 080 049 094 012 094 009 ] -> [049 094 ] duplicados=2
"""
