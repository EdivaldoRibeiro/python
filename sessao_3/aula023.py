senha=input("Senha: ")
if not senha:
    print("Nao foi informado a senha")

print(f'not 0     ->{not 0}')
print(f'not -1    ->{not -1}')
print(f'not False ->{not False}')
print(f'not True  ->{not True}')
print(f'not \'\'    ->{not ''}')
print(f'not \'abc\' ->{not 'abc'}')


"""
Exibe ao executar:

Senha: 
Nao foi informado a senha
not 0     ->True
not -1    ->False
not False ->True
not True  ->False
not ''    ->True
not 'abc' ->False
"""
