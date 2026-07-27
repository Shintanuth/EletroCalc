from util.constantes import SEPARADOR, VERSAO

def mostrar_cabecalho(titulo, versao=None, subtitulo=None):

    print(SEPARADOR)

    print()
    print(f"{titulo:^40}")

    if versao:
        print(f"{VERSAO:^40}")

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

    return input("Digite uma opção: ")

def mostrar_resultado(grandeza, resultado, unidade):
    print(SEPARADOR)
    print()
    str_resultado = "RESULTADO:"
    print(f"{str_resultado:^40}")
    print()

    return f'{grandeza} = {resultado:.2f} {unidade}'
    