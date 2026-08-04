# ===========================
# Validações gerais
# ===========================


def validar_obrigatorio(valor, mensagem):

    if valor is None:
        raise ValueError(mensagem)


def validar_maior_que_zero(valor, mensagem):

    if valor <= 0:
        raise ValueError(mensagem)


def validar_obrigatorio_positivo(valor, erro_obrigatorio, erro_invalido):

    validar_obrigatorio(valor, erro_obrigatorio)
    validar_maior_que_zero(valor, erro_invalido)


def validar_intervalo(valor, minimo, maximo, nome):

    if valor < minimo or valor > maximo:
        raise ValueError(f"{nome} deve estar entre {minimo} e {maximo}")


def validar_maior(valor, limite, mensagem):

    if valor > limite:
        raise ValueError(mensagem)


# ===========================
# Validações de Menu
# ===========================


def validar_opcao(opcao, opcoes_validas, mensagem):

    if opcao not in opcoes_validas:
        raise ValueError(mensagem)
