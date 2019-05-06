# coding=utf-8


class MergeSort:
    def merge(self, left: list, right: list) -> list:
        """ Merge operation. """
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result.extend(left)
        if right:
            result.extend(right)
        return result

    def sort(self, array: list) -> list:
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # sort left and right
        left = self.sort(left)
        right = self.sort(right)

        # merge left and right
        return self.merge(left, right)
