# coding=utf-8


class QuickSort:
    def sort(self, array: list) -> list:
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            left_partition = [i for i in array[1:] if i <= pivot]
            right_partition = [i for i in array[1:] if i > pivot]
            return self.sort(left_partition) + [pivot] \
                + self.sort(right_partition)
