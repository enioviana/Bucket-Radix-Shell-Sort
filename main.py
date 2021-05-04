# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""
from random import randint
import timeit

from Bucket import Bucket
from Radix import Radix
from Shell import Shell


def criar_vetor(tamanho):
    v1 = []
    v2 = []
    v3 = []
    for i_ in range(tamanho):
        aux = randint(0, tamanho)
        v1.append(aux)
        v2.append(aux)
        v3.append(aux)
    return v1, v2, v3


vec_buck, vec_rad, vec_shel = criar_vetor(100000)
# print("Vetor a ser ordenado\n{0}".format(vec_rad))

buck = Bucket(vec_buck)
rad = Radix(vec_rad)
shel = Shell(vec_shel)
