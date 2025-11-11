import platform, os, time


def limpaTela():
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')


def mensagemErro(escolha):
    limpaTela()
    print(f"A opção '{escolha}' é Inválido!")
    time.sleep(1)
    input("\nClique Enter para continuar.")
    pass


def telaCarregamento(num):
    for i in range(num):
        print(" o", end="", flush=True)
        time.sleep(0.1)


def definindoMedidas(lista, mensagem, pergunta, valorMin=0, valorMax=int()):

    telaCarregamento(6)

    while True:
        try:
            limpaTela()
            print(mensagem)
            print("-"*40)
            escolha = input(pergunta)
            escolha = int(escolha)

            if escolha == (valorMax+1):
                limpaTela()
                telaCarregamento(6)           
                break
            
            escolha -= 1
            
            if valorMin <= escolha < valorMax:
                return lista[escolha]
            else:
                mensagemErro(escolha+1)

        except ValueError:                  
            mensagemErro(escolha+1)


def telaResultado(nomeInicial, nomeFinal, result, i, medida):
    limpaTela()
    print(f"=== Conversão de {nomeInicial} para {nomeFinal} ===")
    print("-"*40)
    print(f"Resultado: {result:.{i}f} {medida}")
    time.sleep(1)
    input("\nClique Enter para continuar.")
    limpaTela()
    telaCarregamento(6)

