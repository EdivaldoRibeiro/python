_MISTERY='manteiga'
secret='********'

def verify(word, secret):
    if word in _MISTERY:
        print(f'{word} esta na palavra secreta')
        nova=''
        for idx in range(0,len(_MISTERY)):
            letra=secret[idx]
            letra_sec=_MISTERY[idx]
            if letra_sec == word:
                nova+=letra_sec
            else:
                nova+=letra

        secret=nova
    return secret

palavras=set()
while True:
    word=input(f'Encontre a palava [{secret}]:')
    word=word.lower().strip()
    for carac in word:
        secret=verify(carac, secret)

    palavras.add(secret)
    print(palavras)
    if _MISTERY in palavras:
        print(f'Palavra [{_MISTERY}] encontrada, você é fera!')
        break

"""
Exibe ao executar:

Encontre a palava [********]:a
a esta na palavra secreta
{'*a*****a'}
Encontre a palava [*a*****a]:e
e esta na palavra secreta
{'*a*****a', '*a**e**a'}
Encontre a palava [*a**e**a]:i
i esta na palavra secreta
{'*a*****a', '*a**e**a', '*a**ei*a'}
Encontre a palava [*a**ei*a]:t
t esta na palavra secreta
{'*a*tei*a', '*a*****a', '*a**e**a', '*a**ei*a'}
Encontre a palava [*a*tei*a]:g
g esta na palavra secreta
{'*a**ei*a', '*a*****a', '*a**e**a', '*a*teiga', '*a*tei*a'}
Encontre a palava [*a*teiga]:man
m esta na palavra secreta
a esta na palavra secreta
n esta na palavra secreta
{'*a**ei*a', '*a*****a', '*a**e**a', '*a*teiga', '*a*tei*a', 'manteiga'}
Palavra [manteiga] encontrada, você é fera!
"""
