#precedencia  matematica PEMDAS (vale da esquerda para a direita)
#1o. [P]arenteses ()
#2o. [E]xpoentes **
#3o. [M]ultiplicacao * / // %
#4o. [D]ivisao
#5o. [A]dicao/[S]ubtracao
conta1=1+1**5+5
conta2=(1+1)**5+5
conta3=(1+1)**(5+5)

print("conta1:", conta1)
print("conta2:", conta2)
print("conta3:", conta3)

"""
Exibe ao executar:

conta1: 7
conta2: 37
conta3: 1024
"""
