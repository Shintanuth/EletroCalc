from math import pi

SEPARADOR = "=" * 41
VERSAO = "v0.1"
LARGURA = 41
TITULO_MENU_PRINCIPAL = "ELETROCALC"
TITULO_MENU_LEI_DE_OHM = "LEI DE OHM"
TITULO_MENU_POTENCIA = "POTÊNCIA"
TITULO_MENU_REAT_CAP = "REATÂNCIA CAPACITIVA"
TITULO_MENU_REAT_IND = "REATÂNCIA INDUTIVA"
TITULO_MENU_POTENCIAS = "POTÊNCIA ELÉTRICA"
TITULO_MENU_POTENCIA_APARENTE = "POTÊNCIA APARENTE"
FORMULA_REATANCIA_CAPACITIVA = "XC = 1 / 2 π × ƒ × C"
FORMULA_LEI_DE_OHM = "I = E / R"
FORMULA_REATANCIA_INDUTIVA = "XL = 2 x π x ƒ x L"
FORMULA_POTENCIA_ATIVA = "P = E x I"
OPCOES_MENU_PRINCIPAL = [
                        "Lei de Ohm",
                        "Potência Elétrica", 
                        "Reatância Indutiva", 
                        "Reatância Capacitiva"
                        ]
OPCOES_MENU_POTENCIAS = [
                        "Potência Ativa",
                        "Potência Reativa", 
                        "Potência Aparente", 
                        "Fator de Potência"
                        ]
OPCOES_MENU_POTENCIA_APARENTE = ["Calcular por Tensão e Corrente",
                                 "Calcular por Potência Ativa e Fator de Potência",
                                 "Calcular por Potência Ativa e Potência Reativa"
                                ]
SELETOR_MENU_PRINCIPAL = ["s", "1", "2", "3", "4"]
SELETOR_MENU_POTENCIAS = ["s", "v", "c", "1", "2", "3", "4"]
SELETOR_MENU_POTENCIA_APARENTE = ["s", "v", "c", "1", "2", "3"]
PI = pi
FREQUENCIA_PADRAO = 60
OHM = "Ω"
VOLT = "V"
AMPERE = "A"
WATT = "W"
VOLT_AMPERE = "VA"
VOLT_AMPERE_REATIVO = "VAR"
HERTZ = "Hz"
HENRY = "H"
FARAD = "F"