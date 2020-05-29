# -*- coding: UTF-8 -*-
# impostos.py
class ICMS(object):
	def calcula(orcamento) -> float:
	    return orcamento.valor * 0.1

class ISS(object):
	def calcula(orcamento) -> float:
	    return orcamento.valor * 0.06
