"""
dates.py
~~~~~~~

Módulo com funções auxiliares para datas
"""

import datetime


def list_generate(start, end):
    """Gera uma lista de tuplas de datas
        a partir de uma data inicial e final.

    :param start: Data inicial.
    :param end: Data final.
    :return: Lista de tuplas de datas.
    """

    date_list = [start + datetime.timedelta(days=x)
                 for x in range(0, (end-start).days)]

    return list(zip(date_list, date_list[1:]))
