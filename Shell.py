# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""


class Shell:
    def __init__(self, vetor):
        # Start with a big gap, then reduce the gap
        n = len(vetor)
        gap = n // 2

        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array
        # is gap sorted
        while gap > 0:

            for i in range(gap, n):

                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = vetor[i]

                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                while j >= gap and vetor[j - gap] > temp:
                    vetor[j] = vetor[j - gap]
                    j -= gap

                # put temp (the original a[i]) in its correct location
                vetor[j] = temp
            gap //= 2
