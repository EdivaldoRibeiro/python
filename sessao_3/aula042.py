frase='E, servindo eles ao Senhor, e jejuando, disse ' \
      'o Espirito Santo: Apartai-me a Barnabé e a ' \
      'Saulo para a obra a que os tenho chamado.'

print(f'{frase}')
print("=INICIO===========")
palavras=''
idx=0
while idx<len(frase):
    caracter=frase[idx]
    if caracter not in palavras:
        palavras=palavras+caracter
    idx+=1

idx=0
total=0
master=''
master_total=0
while idx<len(palavras):
    caracter=palavras[idx]
    conta=frase.count(caracter)

    if conta > master_total:
        if caracter != ' ':
            master = caracter
            master_total = conta

    total+=conta
    print(f'Existem {conta:02d} do caracter "{caracter}" na frase - {total:02d}')
    idx+=1
print("=FIM==============")
print(f'Tamanho original da frase {len(frase)} soma dos bytes analisados {total}')
print(f'Caracter campeão diferente de espaço é "{master}" com {master_total:03d} ocorrencias')

"""
Exibe ao executar:

E, servindo eles ao Senhor, e jejuando, disse o Espirito Santo: Apartai-me a Barnabé e a Saulo para a obra a que os tenho chamado.
=INICIO===========
Existem 02 do caracter "E" na frase - 02
Existem 03 do caracter "," na frase - 05
Existem 24 do caracter " " na frase - 29
Existem 06 do caracter "s" na frase - 35
Existem 11 do caracter "e" na frase - 46
Existem 07 do caracter "r" na frase - 53
Existem 01 do caracter "v" na frase - 54
Existem 05 do caracter "i" na frase - 59
Existem 06 do caracter "n" na frase - 65
Existem 04 do caracter "d" na frase - 69
Existem 12 do caracter "o" na frase - 81
Existem 02 do caracter "l" na frase - 83
Existem 17 do caracter "a" na frase - 100
Existem 03 do caracter "S" na frase - 103
Existem 03 do caracter "h" na frase - 106
Existem 02 do caracter "j" na frase - 108
Existem 03 do caracter "u" na frase - 111
Existem 03 do caracter "p" na frase - 114
Existem 04 do caracter "t" na frase - 118
Existem 01 do caracter ":" na frase - 119
Existem 01 do caracter "A" na frase - 120
Existem 01 do caracter "-" na frase - 121
Existem 02 do caracter "m" na frase - 123
Existem 01 do caracter "B" na frase - 124
Existem 02 do caracter "b" na frase - 126
Existem 01 do caracter "é" na frase - 127
Existem 01 do caracter "q" na frase - 128
Existem 01 do caracter "c" na frase - 129
Existem 01 do caracter "." na frase - 130
=FIM==============
Tamanho original da frase 130 soma dos bytes analisados 130
Caracter campeão diferente de espaço é "a" com 017 ocorrencias
"""
