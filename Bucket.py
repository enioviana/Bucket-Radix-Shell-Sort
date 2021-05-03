# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""


class Bucket:
    def __init__(self):
        self.arr = []
        self.slot_num = 10  # 10 means 10 slots, each

    def run(self, vetor):
        # slot's size is 0.1
        for i in range(self.slot_num):
            self.arr.append([])

        # Put array elements in different buckets
        for j in vetor:
            index_b = int(self.slot_num * j)
            self.arr[index_b].append(j)

        # Sort individual buckets
        for i in range(self.slot_num):
            self.arr[i] = Bucket.insertion_sort(self.arr[i])

        # concatenate the result
        k = 0
        for i in range(self.slot_num):
            for j in range(len(self.arr[i])):
                vetor[k] = self.arr[i][j]
                k += 1
        return vetor

    @staticmethod
    def insertion_sort(b):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while j >= 0 and b[j] > up:
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up
        return b
