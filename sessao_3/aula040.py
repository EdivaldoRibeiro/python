condicao=True
while condicao:
    print("")
    print("===Calculadora====================================================")
    in_val1=input("Digite numero1: ")
    in_val2=input("Digite numero2: ")
    in_ope=input("Digite operacao [+] soma [-] subtracao [*] multiplicacao [/] divisao: ")

    ope_soma=in_ope == '+'
    ope_subtracao=in_ope == '-'
    ope_multiplicacao=in_ope == '*'
    ope_divisao=in_ope == '/'

    val1=None
    try:
        val1=float(in_val1)
    except:
        print(f'{in_val1} não é um número válido')
        val1=0

    val2=None
    try:
        val2=float(in_val2)
    except:
        val2=0
        print(f'{in_val2} não é um número válido')

    if not (ope_soma or ope_subtracao or ope_multiplicacao or ope_divisao):
        print('f{in_ope} não é uma operação válida - será feito SOMA')
        ope_soma=True

    total=None
    if ope_soma:
        print(f'{val1:.2f} + {val2:.2f} = {val1+val2:.2f}')
        total=val1+val2
    elif ope_subtracao:
        print(f'{val1:.2f} - {val2:.2f} = {val1-val2:.2f}')
        total=val1-val2
    elif ope_multiplicacao:
        print(f'{val1:.2f} * {val2:.2f} = {val1*val2:.2f}')
        total=val1*val2
    else:
        print(f'{val1:.2f} / {val2:.2f} = {val1/val2:.2f}')
        total=val1/val2

    continuar=input("Digite [S] para sair ou Enter para continuar: ")
    if continuar:
        continuar = continuar.strip()[0].lower()        # trim()
        condicao = not (continuar == 's')

print("Sainda da calculadora...")

"""
Exibe ao executar:

===Calculadora====================================================
Digite numero1: 12.2
Digite numero2: 22.4
Digite operacao [+] soma [-] subtracao [*] multiplicacao [/] divisao: /
12.20 / 22.40 = 0.54
Digite [S] para sair ou Enter para continuar: 

===Calculadora====================================================
Digite numero1: 1
Digite numero2: 1
Digite operacao [+] soma [-] subtracao [*] multiplicacao [/] divisao: /
1.00 / 1.00 = 1.00
Digite [S] para sair ou Enter para continuar:  S
Sainda da calculadora...
"""
