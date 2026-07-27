from util.constantes import SEPARADOR

def mostrar_cabecalho(titulo):

    print(SEPARADOR)
    print()
    print(f"{titulo:^40}")
    print()
    print(SEPARADOR)


def mostrar_resultado(grandeza, resultado, unidade):

    return f'{grandeza} = {resultado:.2f} {unidade}'     