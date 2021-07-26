"""
cdi.py
~~~~~~~

Módulo com funções auxiliares para trabalhar com índice do CDI.
"""

import requests


def get_fator(dates):
    """Consulta o fator do CDI considerando o período informado.

    :param dates: Tupla com data inicial e final do período.
    :return: Dicionário com a data e o fator.
    """

    url = "https://calculadorarendafixa.com.br/calculadora/di/calculo"

    response = requests.get(
        url,
        params=[
            ('dataInicio', dates[0].strftime("%Y-%m-%d")),
            ('dataFim', dates[1].strftime("%Y-%m-%d")),
            ('percentual', '100'),
            ('valor', '1000.00'),
        ]
    ).json()

    return {
        "Data": dates[1],
        "Fator": response["fator"]
    }
