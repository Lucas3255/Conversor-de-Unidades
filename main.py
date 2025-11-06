'''
    O bug está na linha 38 do arquivo temperatura.py, na qual apresenta um bug
    mistérioso, n há erro de sintaxe e a lógica parece normal, por algum motivo,
    mesmo a variável sendo string e apenas precisando apresentar uma frase concatenada,
    ainda s, n está conseguindo realizar a ação simples. Olha e tentar resolver.
'''

from funcoes import time
from funcoes import limpaTela, mensagemErro, telaCarregamento
from utils.comprimento import calculoComprimento
from utils.massa import calculoMassa
from utils.temperatura import calculoTemperatura

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
            pass

        case '5':
            limpaTela()
            print("Encerrando Programa.")
            telaCarregamento(8)
            exit()

        case _:
            mensagemErro(escolha)
