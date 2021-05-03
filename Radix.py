# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""


class Radix:
    def __init__(self, vetor):
        # Find the maximum number to know number of digits
        max1 = max(vetor)

        # Do counting sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1.0
        while max1 / exp > 0.0:
            Radix.counting_sort(vetor, exp)
            exp *= 10

    @staticmethod
    def counting_sort(vetor, exp1):

        n = len(vetor)

        # The output array elements that will have sorted arr
        output = [0] * n

        # initialize count array as 0
        count = [0] * 10

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (vetor[i] / exp1)
            count[int(index % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = (vetor[i] / exp1)
            output[count[int(index % 10)] - 1] = vetor[i]
            count[int(index % 10)] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(vetor)):
            vetor[i] = output[i]
