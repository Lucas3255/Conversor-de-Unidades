from utils.funcoes import limpaTela, mensagemErro, telaCarregamento
from utils.funcoes import definindoMedidas, telaResultado

def perguntaChave():
    return """ 1 - Celsius (°C)
 2 - Fahrenheit (°F)
 3 - Kelvin (K)
 4 - Sair
 \n >> """

def calculoTemperatura():
    temperaturas = ['Celsius', 'Fahrenheit', 'Kelvin']

    formulas = {
        ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32
    }

    siglas = {
        'Celsius': '°C',
        'Fahrenheit': '°F',
        'Kelvin': 'K'
    }

    temperaturaInicial = definindoMedidas(temperaturas, "Qual a temperatura inicial?", perguntaChave(), 0, 3)
    if temperaturaInicial is None:
        return

    limpaTela()
    temperaturaFinal = definindoMedidas(temperaturas, "E a temperatura final?", perguntaChave(), 0, 3)
    if temperaturaFinal is None:
        return
    
    limpaTela()
    telaCarregamento(6)
    while True:
        try:    #Bug por aqui.
            limpaTela()
            valor_input = input(f"Informe o valor em {temperaturaInicial}.\n >> ").replace(',','.')
            valor = float(valor_input)
            break

        except ValueError:
            mensagemErro(valor_input)

    i = (temperaturaInicial, temperaturaFinal)
    if i in formulas:
        resultado = formulas[i](valor)

    telaResultado(temperaturaInicial, temperaturaFinal, resultado, 6, siglas[temperaturaFinal])
    

