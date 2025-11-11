from utils.funcoes import limpaTela, mensagemErro, telaCarregamento
from utils.funcoes import definindoMedidas, telaResultado

def perguntaChave():
    return """ 1 - Km (Quilômetro)
 2 - Hm (Hectômetro)
 3 - Dam (Decâmetro)
 4 - m (Metro)
 5 - dm (Decímetro)
 6 - cm (Centímetro)
 7 - mm (Milímetro)
 8 - Sair
 \n >> """

def calculoComprimento():
    unidades = ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm']

    fatores = {
        'km': 1000,
        'hm': 100,
        'dam': 10,
        'm': 1,   #base
        'dm': 0.1,
        'cm': 0.01,
        'mm': 0.001
    }

    nomes_completos = {
        'km': 'quilômetro', 'hm': 'hectômetro', 'dam': 'decâmetro', 'm': 'metro',
        'dm': 'decímetro', 'cm': 'centímetro', 'mm': 'milímetro'
    }

    medidaInicial = definindoMedidas(unidades, "Qual a medida inicial?", perguntaChave(), 0, 7)
    if medidaInicial is None:
        return
    
    limpaTela()
    medidaFinal = definindoMedidas(unidades, "E a medida final?", perguntaChave(), 0, 7)
    if medidaFinal is None:
        return

    limpaTela()
    telaCarregamento(6)
    while True:
        try:
            limpaTela()
            valor_input = input(f"Informe o valor em {nomes_completos[medidaInicial]}.\n >> ").replace(',', '.')
            valor = float(valor_input)
            break

        except ValueError:
            mensagemErro(valor_input)

    resultado = (valor * fatores[medidaInicial]) / fatores[medidaFinal]

    telaResultado(nomes_completos[medidaInicial], nomes_completos[medidaFinal], resultado, 6, medidaFinal)

