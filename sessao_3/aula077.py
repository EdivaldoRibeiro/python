_PERGUNTA='pergunta'
_OPCOES='opcoes'
_RESPOSTA='resposta'

pergunta1={
    _PERGUNTA:'Quanto é 2+2?',
    _OPCOES:['1','3','4','5'],
    _RESPOSTA:'4'}

pergunta2={
    _PERGUNTA:'Quanto é 5*5?',
    _OPCOES:['25','55','10','51'],
    _RESPOSTA:'25'}

pergunta3={
    _PERGUNTA:'Quanto é 10/2?',
    _OPCOES:['4','5','2','1'],
    _RESPOSTA:'5'}

perguntas=[pergunta1, pergunta2, pergunta3]

def exibe_opcoes(*args):
    opcoes=args[0]
    correto=None
    if len(args) == 2:
        correto=args[1]

    if correto is None:
        print('')
        print('---------------------------------')
        print('Responda um dos valores:')
    else:
        print('Resposta correta:')
    for opcao in opcoes:
        if correto is None:
            print(opcao)
        elif int(opcao) == correto:
            print(f'{opcao} <==')
        else:
            print(opcao)

for pergunta in perguntas:
    r_pergunta=pergunta[_OPCOES]
    exibe_opcoes(r_pergunta)
    resp=input(f'{pergunta[_PERGUNTA]}: ')
    resp_digit=int(resp)
    is_valid=False
    for valor in r_pergunta:
        if int(valor) == resp_digit:
            is_valid=True
            break

    resp_valid=int(pergunta[_RESPOSTA])
    if is_valid and resp_valid == resp_digit:
        print(f'a resposta {resp_digit} esta na lista, e está correta!')
    elif is_valid and resp_digit != resp_valid:
        print(f'a resposta {resp_digit} esta na lista, mas errado, o correto seria {resp_valid}')
    else:
        print(f'o valor informado {resp_digit} não esta na lista e está incorreto')
    exibe_opcoes(pergunta[_OPCOES], resp_valid)

"""
Exibe ao executar:


---------------------------------
Responda um dos valores:
1
3
4
5
Quanto é 2+2?: 4
a resposta 4 esta na lista, e está correta!
Resposta correta:
1
3
4 <==
5

---------------------------------
Responda um dos valores:
25
55
10
51
Quanto é 5*5?: 10
a resposta 10 esta na lista, mas errado, o correto seria 25
Resposta correta:
25 <==
55
10
51

---------------------------------
Responda um dos valores:
4
5
2
1
Quanto é 10/2?: 3
o valor informado 3 não esta na lista e está incorreto
Resposta correta:
4
5 <==
2
1
"""
