def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao} - {nome}'
    return saudar

def make_salutation(saudacao):
    def salutation(nome):
        return f'{saudacao} - {nome}'
    return salutation


print('-----Jeito padrão------')
s1 = criar_saudacao('Siga em frente', 'Edivaldo')
s2 = criar_saudacao('Prevaleça na fé', 'Maria')

print(f's1={s1()}')
print(f's2={s2()}')

print('-----Jeito magico------')
s1 = make_salutation('Siga em frente')
s2 = make_salutation('Prevaleça na fé')

print(f's1={s1('Edivaldo')}')
print(f's2={s2('Maria')}')


"""
Exibe ao executar:

-----Jeito padrão------
s1=Siga em frente - Edivaldo
s2=Prevaleça na fé - Maria
-----Jeito magico------
s1=Siga em frente - Edivaldo
s2=Prevaleça na fé - Maria
"""


