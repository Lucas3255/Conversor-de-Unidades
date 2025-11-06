import platform, os, time, sys

def limpaTela():
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')


def aguarda_tecla():
    if platform.system().lower() == "windows":
        import msvcrt
        msvcrt.getch()
    else:


def mensagemErro(escolha):
    limpaTela()
    print(f"A opção '{escolha}' é Inválido!")
    time.sleep(1)
    print("\nClique qualquer tecla para continuar.")
    aguarda_tecla()
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
                mensagemErro(escolha)

        except ValueError:                  
            mensagemErro(escolha)







