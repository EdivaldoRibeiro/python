secreto='Limonada'
descoberto='********'

tentativa=0
while secreto != descoberto:
    tentativa+=1
    palavra=input(f"Escolha palavra para descobrir [{descoberto}] (tentativa:{tentativa}): ")
    if not palavra:
        continue

    if palavra in secreto:
        print(f'{palavra} esta na palavra secreta')
        nova=''
        for idx in range(0,len(secreto)):
            letra=descoberto[idx]
            letra_sec=secreto[idx]
            if letra_sec == palavra:
                nova+=letra_sec
            else:
                nova+=letra

        descoberto=nova    
        if descoberto == secreto:
            print(f'**** VIVA! Descoberto palavra: {secreto} ****')
            break;

print("Sucesso fim do jogo")

"""
Exibe ao executar:

Escolha palavra para descobrir [********] (tentativa:1): a
a esta na palavra secreta
Escolha palavra para descobrir [*****a*a] (tentativa:2): e
Escolha palavra para descobrir [*****a*a] (tentativa:3): i
i esta na palavra secreta
Escolha palavra para descobrir [*i***a*a] (tentativa:4): o
o esta na palavra secreta
Escolha palavra para descobrir [*i*o*a*a] (tentativa:5): m
m esta na palavra secreta
Escolha palavra para descobrir [*imo*a*a] (tentativa:6): d
d esta na palavra secreta
Escolha palavra para descobrir [*imo*ada] (tentativa:7): n
n esta na palavra secreta
Escolha palavra para descobrir [*imonada] (tentativa:8): L
L esta na palavra secreta
**** VIVA! Descoberto palavra: Limonada ****
Sucesso fim do jogo
"""
