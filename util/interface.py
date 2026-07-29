from util.constantes import SEPARADOR, LARGURA
from util.mensagens import TITULO_ERRO, TITULO_AVISO, TITULO_ATENCAO, TITULO_SUCESSO, MSG_OPCAO_INVALIDA
from util.converte_entrada import converte_entrada
from textwrap import fill 

def sair_do_menu():
    while True:
        print(SEPARADOR)
        print("[c] Continuar")
        print("[v] voltar ao menu principal")
        print("[s] sair")
        print(SEPARADOR)
        opcao = input("Digite sua opção: ").strip().lower()
        
        if opcao in ("c","v","s"):
            return opcao

        print(MSG_OPCAO_INVALIDA)

def mostrar_cabecalho(titulo, versao=None, subtitulo=None):

    print(SEPARADOR)

    print()
    print(f"{titulo:^40}")

    if versao:
        print(f"{versao:^40}")

    if subtitulo:
        print(f"{subtitulo:^40}")

    print()
    print(SEPARADOR)

def mostrar_opcoes(opcoes, voltar=True):
    for indice, opcao in enumerate(opcoes, start=1):
        print(f"{indice} - {opcao}")

    print()

    if voltar:
        print("[v] - Voltar ao menu anterior")

    print("[s] - Sair")
    print(SEPARADOR)

    return input("Digite uma opção: ")

def mostrar_resultado(grandeza, resultado, unidade):
    return (
    f"{SEPARADOR}\n\n"
    f"{'RESULTADO':^40}\n\n"
    f"{grandeza} = {resultado:.2f} {unidade}"
)

def mostrar_mensagem(titulo, mensagem):

    print(SEPARADOR)
    print()

    print(f"{titulo:^{LARGURA}}")
    print()
    print(formatar_texto(mensagem))

    print()
    print(SEPARADOR)

def ler_entrada(nome_grandeza, unidade):

    return converte_entrada(input(f"{nome_grandeza} ({unidade}): "))

def formatar_texto(texto):

    return fill(str(texto), width=LARGURA)

def mostrar_erro(mensagem):
    mostrar_mensagem(TITULO_ERRO, mensagem)

def mostrar_aviso(mensagem):
    mostrar_mensagem(TITULO_AVISO, mensagem)

def mostrar_sucesso(mensagem):
    mostrar_mensagem(TITULO_SUCESSO, mensagem)

def mostrar_atencao(mensagem):
    mostrar_mensagem(TITULO_ATENCAO, mensagem)