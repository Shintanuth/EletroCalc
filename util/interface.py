from util.constantes import SEPARADOR, VERSAO
from util.converte_entrada import converte_entrada 

def mostrar_cabecalho(titulo, versao=VERSAO, subtitulo=None):

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

def mostrar_erro(mensagem):

    print(SEPARADOR)
    print()

    print(f"ERRO: {mensagem}")

    print()
    print(SEPARADOR)

def ler_entrada(nome_grandeza, unidade):

    return converte_entrada(input(f"{nome_grandeza} ({unidade}): "))
