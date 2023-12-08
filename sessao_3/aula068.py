x=1

def escopo1():
    x=2
    def escopo1_func():
        x=21
        print(f'escopo1_func -->x é local da função={x}')
    escopo1_func()
    print(f'escopo1 -> x é local da função={x}')


def escopo2():
    global x
    def escopo2_func():
        x=21
        print(f'escopo2_func -->x é local da função={x}')

    escopo2_func()
    print(f'escopo2 -> x é global={x}')


escopo1()
escopo2()

x=5
escopo1()
escopo2()

"""
Exibe ao executar:

escopo1_func -->x é local da função=21
escopo1 -> x é local da função=2
escopo2_func -->x é local da função=21
escopo2 -> x é global=1
escopo1_func -->x é local da função=21
escopo1 -> x é local da função=2
escopo2_func -->x é local da função=21
escopo2 -> x é global=5
"""
