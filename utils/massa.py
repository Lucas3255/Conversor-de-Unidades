from funcoes import time, msvcrt
from funcoes import limpaTela, mensagemErro, telaCarregamento
from funcoes import definindoMedidas

def perguntaChave():
    return """ 1 - Kg (Quilograma)
 2 - Hg (Hectograma)
 3 - Dag (Decagrama)
 4 - g (grama)
 5 - dg (Decigrama)
 6 - cg (Centigrama)
 7 - mg (Miligrama)
 8 - Sair
 \n >> """

def calculoMassa():
    unidades = ['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg']

    fatores = {
        'kg': 1000,
        'hg': 100,
        'dag': 10,
        'g': 1,   #base
        'dg': 0.1,
        'cg': 0.01,
        'mg': 0.001
    }

    nomes_completos = {
        'kg': 'quilograma', 'hg': 'hectograma', 'dag': 'decagrama', 'g': 'grama',
        'dg': 'decigrama', 'cg': 'centímetro', 'mg': 'miligrama'
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

    limpaTela()
    print(f"=== Conversão de {nomes_completos[medidaInicial]} para {nomes_completos[medidaFinal]} ===")
    print("-"*40)
    print(f"Resultado: {resultado:.6f} {nomes_completos[medidaFinal]}")
    time.sleep(1)
    print("\nClique qualquer tecla para continuar.")
    msvcrt.getch()
    



