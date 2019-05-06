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


class QuickSortInPlace:
    def partition(self, array: list, left: int, right: int):
        if left >= right:
            return
        else:
            # choose pivot
            pivot_idx = random.randint(left, right)
            pivot = array[pivot_idx]
            # swap pivot to the end
            array[pivot_idx], array[right] = array[right], array[pivot_idx]
            store_idx = left
            # if value is smaller than pivot, swap it to the front
            for i in range(left, right):
                if array[i] < pivot:
                    array[i], array[store_idx] = array[store_idx], array[i]
                    store_idx += 1
            # swap pivot to the store_idx position
            array[store_idx], array[right] = array[right], array[store_idx]

            self.partition(array, left, store_idx-1)
            self.partition(array, store_idx+1, right)

    def sort(self, array: list) -> list:
        self.partition(array, 0, len(array)-1)
        return array
