from utils.funcoes import limpaTela, mensagemErro, telaCarregamento
from utils.comprimento import calculoComprimento
from utils.massa import calculoMassa
from utils.temperatura import calculoTemperatura
from utils.tempo import calculoTempo

while True:
    limpaTela()
    print("==== Conversor de Unidades ====")
    print("-"*40)
    escolha = input(" 1 - Comprimento.\n 2 - Massa\n 3 - Temperatura\n 4 - Tempo\n 5 - Sair\n\n >> ")
    
    match escolha:
        case '1':   #Comprimento
            limpaTela()
            calculoComprimento()

        case '2':   #Massa
            limpaTela()
            calculoMassa()

        case '3':   #Temperatura
            limpaTela()
            calculoTemperatura()

        case '4':   #Tempo
            limpaTela()
            calculoTempo()

        case '5':
            limpaTela()
            print("Encerrando Programa.")
            telaCarregamento(8)
            exit()

        case _:
            mensagemErro(escolha)
