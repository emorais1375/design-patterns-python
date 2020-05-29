# -*- coding: UTF-8 -*-
# impostos.py
def calcula_ICMS(orcamento) -> float:
    return orcamento.valor * 0.1

def calcula_ISS(orcamento) -> float:
    return orcamento.valor * 0.06