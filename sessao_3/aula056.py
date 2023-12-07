import re

texto='E, naquele mesmo tempo, houve um não pequeno alvoroço acerca do Caminho.'

print("split sem passar parametro")
palavras=texto.split()
for str in palavras:
    print(str)

print("")
print("split passando parametro")
frases=texto.split(',')
for str in frases:
    print(str)

print("")
print("split usando expressao regular")
frases=re.split(r'[^\w\s]', texto)
for str in frases:
    print(str.strip())

print("")
print("Usando join")
novo_texto=' '.join(palavras)
print(f'Nova frase:{novo_texto}')


"""
Exibe ao executar:

split sem passar parametro
E,
naquele
mesmo
tempo,
houve
um
não
pequeno
alvoroço
acerca
do
Caminho.

split passando parametro
E
 naquele mesmo tempo
 houve um não pequeno alvoroço acerca do Caminho.

split usando expressao regular
E
naquele mesmo tempo
houve um não pequeno alvoroço acerca do Caminho


Usando join
Nova frase:E, naquele mesmo tempo, houve um não pequeno alvoroço acerca do Caminho.
"""
