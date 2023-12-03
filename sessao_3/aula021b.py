entrada=input("[E]ntrar [S]air: ")
senha_digitada=input("Senha: ")
senha_valida='12345'

if entrada == 'E' and senha_digitada == senha_valida:
    print("Acesso permitido")
elif entrada == 'E' and senha_digitada != senha_valida:
    print("Acesso negado, senha invalida...")
elif entrada == 'S':
    print("Saindo...")
else:
    print("Opcao invalida...")


"""
Exibe ao executar:

[E]ntrar [S]air: E
Senha: 12345
Acesso permitido
"""
