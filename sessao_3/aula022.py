entrada=input("Digite [E]ntrar ou [S]air: ") or "Nada foi digitado"
senha=input("Digite senha: ") or "Nao informou a senha"
senha_valida="12345"

print(f'entrada: {entrada} senha: {senha}')
if (entrada == 'E' or entrada == 'e') and senha == senha_valida:
    print("ok, pode entrar")
elif (entrada == 'E' or entrada == 'e') and senha != senha_valida:
    print("A senha nao confere...")
elif (entrada == 'S' or entrada == 's'):
    print("Saindo de mansinho...")
else:
    print("Opção nao reconhecida")

"""
Exibe ao executar:

Digite [E]ntrar ou [S]air: e
Digite senha: 
entrada: e senha: Nao informou a senha
A senha nao confere...
"""
