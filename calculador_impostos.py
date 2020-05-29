# -*- coding: UTF-8 -*-

# calculador_de_impostos.py
from impostos import ICMS, ISS


class Calculador_de_impostos(object):

  def realiza_calculo(self, orcamento, imposto):
    calculado = imposto.calcula(orcamento)
    print(calculado)

if __name__ == '__main__':

    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, ICMS) ## imprimirá 50.0
    calculador_de_impostos.realiza_calculo(orcamento, ISS) ## imprimirá 30.0
