import os


def exibir_nome_do_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗

    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝

    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░

    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗

    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝

    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
    """)

 

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #print(f'Você escolheu a opção{opcao_escolhida}')
        if opcao_escolhida == 1:
            print('Cadastrar restaurante')   
        elif opcao_escolhida == 2:
            print('Listar restaurantes')   
        elif opcao_escolhida == 3:
            print('Ativar restaurante')   
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

"""é importante entender que quando criamos um arquivo com a extensão .py, podemos ter duas opções.
A primeira: podemos indicar para o Python que esse é o arquivo principal do programa. Nós não queremos que
ele seja importado por outros arquivos Python para que seja executado, assim como fizemos com o import os.
Queremos que ele seja o arquivo principal da nossa aplicação. E podemos sinalizar isso para o Python,
dizendo: "Python, este é o arquivo principal". Vamos fazer isso agora.
Quando pedimos para que um programa Python seja executado, o interpretador cria uma
variável chamada __name__. Se o __name__ for __main__ (principal, em inglês), significa que esse
código não será importado por outros scripts de código Python, e ele será o programa principal."""
 
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
