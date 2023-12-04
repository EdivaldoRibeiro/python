nome=input("Informe nome: ")
senha=input("Informe a senha: ")

if(nome and senha):
    print(f'Seu nome é [{nome}]')
    print(f'Seu nome invertido é [{nome[::-1]}]')
    if(' ' in nome):
        print(f'Seu nome [{nome}] tem espacos')
    print(f'Seu nome [{nome}] tem {len(nome)} caracteres')
    print(f'Seu nome [{nome}] tem o primeiro caracter {nome[0]}')
    print(f'Seu nome [{nome}] tem o último caracter {nome[len(nome)-1]}')
else:
    print("Desculpe! Informaçoes insuficientes")

"""
Exibe ao executar:

Informe nome: Edivaldo Ribeiro
Informe a senha: ola mundo
Seu nome é [Edivaldo Ribeiro]
Seu nome invertido é [oriebiR odlavidE]
Seu nome [Edivaldo Ribeiro] tem espacos
Seu nome [Edivaldo Ribeiro] tem 16 caracteres
Seu nome [Edivaldo Ribeiro] tem o primeiro caracter E
Seu nome [Edivaldo Ribeiro] tem o último caracter o
"""
