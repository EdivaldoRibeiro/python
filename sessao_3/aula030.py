velocidade=65
local_carro=100

RADAR_1=60
LOCAL_1=100
RADAR_RANGE_1=1

if velocidade > RADAR_1:
    print(f'atual velocidade {velocidade} esta maior que previsto em radar {RADAR_1}')

    radar_inicio=LOCAL_1-RADAR_RANGE_1
    radar_final=LOCAL_1+RADAR_RANGE_1
    print(f'Carro no km {local_carro} sera multado se estiver entre km {radar_inicio} e km {radar_final}')

    if local_carro >= radar_inicio and local_carro <= radar_final:
        print('Carro foi multado')
    else:
        print('Carro fora do range do radar')
else:
    print(f'atual velocidade {velocidade} abaixo do previsto em radar {RADAR_1}')

"""
Exibe ao executar:

atual velocidade 65 esta maior que previsto em radar 60
Carro no km 100 sera multado se estiver entre km 99 e km 101
Carro foi multado
"""
