# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""
import timeit


class Bucket:
    vetor = []

    def __init__(self, vetor, buckets=10):
        print("\nOrdenado por Bucket Sort")

        self.start = timeit.default_timer()
        Bucket.vetor = vetor
        self.total_time = 0
        self.total_comparations = 0
        self.slot_num = buckets

        Bucket.vetor = self.run(Bucket.vetor)

        self.stop = timeit.default_timer()
        self.total_time = self.stop - self.start

        print('Tempo total: {0}'.format(self.total_time))
        print('Comparações: {0}'.format(self.total_comparations))
        # print("Vetor ordenado {0}".format(Bucket.vetor))

    def run(self, vetor):
        comprimento = len(vetor)
        bucket = [[] for _ in range(comprimento)]
        maior = max(vetor)
        tamanho = maior / comprimento

        for i in range(comprimento):
            j = int(vetor[i] / tamanho)
            if j != comprimento:
                self.total_comparations += 1
                bucket[j].append(vetor[i])
            else:
                bucket[comprimento - 1].append(vetor[i])

        for i in range(comprimento):
            self.insertion_sort(bucket[i])

        vetor_ordenado = []
        for i in range(comprimento):
            vetor_ordenado = vetor_ordenado + bucket[i]
        return vetor_ordenado

    def insertion_sort(self, vetor):
        for i in range(1, len(vetor)):
            atual = vetor[i]
            j = i - 1
            while j >= 0 and atual < vetor[j]:
                self.total_comparations += 1
                vetor[j + 1] = vetor[j]
                j = j - 1
            vetor[j + 1] = atual
