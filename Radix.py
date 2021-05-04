# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""
import timeit


class Radix:
    def __init__(self, vetor):
        print("\nOrdenado por Radix Sort")
        self.start = timeit.default_timer()
        self.total_time = 0
        self.total_comparations = 0

        ma = max(vetor)
        place = 1
        while ma // place > 0:
            self.counting_sort(vetor, place)
            place *= 10
        self.stop = timeit.default_timer()
        self.total_time = self.stop - self.start

        print('Tempo total: {0}'.format(self.total_time))
        print('Comparações: {0}'.format(self.total_comparations))
        # print("Vetor ordenado {0}".format(vetor))

    def counting_sort(self, vetor, place):
        size = len(vetor)
        output = [0] * size
        count = [0] * 10

        # Calculate count of elements
        for i in range(0, size):
            index = vetor[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            # self.total_comparations += 1
            index = vetor[i] // place
            output[count[index % 10] - 1] = vetor[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            vetor[i] = output[i]
