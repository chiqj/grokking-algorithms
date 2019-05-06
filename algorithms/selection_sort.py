# coding=utf-8


class SelectionSort:
    def find_minimum_idx(self, array: list) -> int:
        min_element = array[0]
        min_idx = 0
        for idx in range(1, len(array)):
            if array[idx] < min_element:
                min_idx = idx
                min_element = array[idx]
        return min_idx

    def sort(self, array: list) -> list:
        result = []
        for _ in range(len(array)):
            min_idx = self.find_minimum_idx(array)
            result.append(array.pop(min_idx))
        return result
