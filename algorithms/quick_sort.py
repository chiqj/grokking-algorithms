# coding=utf-8

import random


class QuickSort:
    def sort(self, array: list) -> list:
        if len(array) <= 1:
            return array
        else:
            # choose pivot randomly
            pivot = array.pop(random.randrange(len(array)))
            left_partition = []
            right_partition = []
            for i in array:
                if i <= pivot:
                    left_partition.append(i)
                else:
                    right_partition.append(i)
            return self.sort(left_partition) + [pivot] \
                + self.sort(right_partition)
