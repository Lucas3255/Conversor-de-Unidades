from utils.funcoes import limpaTela, mensagemErro, telaCarregamento
from utils.funcoes import definindoMedidas, telaResultado

def perguntaChave():
    return """ 1 - Segundo.
 2 - Minuto.
 3 - Hora.
 4 - Dia.
 5 - Semana.
 6 - Mês.
 7 - Ano.
 8 - Sair.
 \n >> """

def calculoTempo():
    tempo = ['s', 'min', 'h', 'dia', 'sem', 'mes', 'ano']

    fatores = {
        's': 1,
        'min': 60,
        'h': 3600,
        'dia': 86400,
        'sem': 604800,
        'mes': 2628000,
        'ano': 31536000
    }

    nomes_completos = {
        's': 'segundo',
        'min': 'minuto',
        'h': 'hora',
        'dia': 'dia',
        'sem': 'semana',
        'mes': 'mês',
        'ano': 'ano'
    }

    tempoInicial = definindoMedidas(tempo, "Qual o tempo inicial?", perguntaChave(), 0, 7)
    if tempoInicial is None:
        return
    
    limpaTela()
    tempoFinal = definindoMedidas(tempo, "E o tempo final?", perguntaChave(), 0, 7)
    if tempoFinal is None:
        return
    
    limpaTela()
    telaCarregamento(6)
    while True:
        try:
            limpaTela()
            valor_input = input(f"Informe o valor em {nomes_completos[tempoInicial]}.\n >> ").replace(',', '.')
            valor = float(valor_input)
            break

        except ValueError:
            mensagemErro(valor_input)

    resultado = (valor * fatores[tempoInicial]) / fatores[tempoFinal]

    telaResultado(nomes_completos[tempoInicial], nomes_completos[tempoFinal], resultado, 1, tempoFinal)



