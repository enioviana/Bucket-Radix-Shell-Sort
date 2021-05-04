# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""
import timeit


class Shell:
    def __init__(self, vetor):
        print("\nOrdenando com Shell Sort")
        self.start = timeit.default_timer()
        self.total_time = 0
        self.total_comparations = 0
        # Start with a big gap, then reduce the gap
        n = len(vetor)
        gap = n // 2

        # Do a gapped insertion sort for this gap size. The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array is gap sorted
        while gap > 0:
            for i in range(gap, n):

                # add a[i] to the elements that have been gap sorted save a[i] in temp and make a hole at position i
                temp = vetor[i]

                # shift earlier gap-sorted elements up until the correct location for a[i] is found
                j = i
                while j >= gap and vetor[j - gap] > temp:
                    vetor[j] = vetor[j - gap]
                    j -= gap
                    self.total_comparations += 1

                # put temp (the original a[i]) in its correct location
                vetor[j] = temp
            gap //= 2

        self.stop = timeit.default_timer()
        self.total_time = self.stop - self.start

        print('Tempo total: {0}'.format(self.total_time))
        print('Comparações: {0}'.format(self.total_comparations))
        # print("Vetor ordenado {0}".format(vetor))
