# coding=utf-8

from typing import Union


class BinarySearch:
    def search(self, search_list: list, search_item) -> Union[int, None]:
        low_idx = 0
        high_idx = len(search_list) - 1

        while low_idx <= high_idx:
            current_idx = (low_idx + high_idx) // 2
            if search_list[current_idx] == search_item:
                return current_idx
            elif search_list[current_idx] > search_item:
                high_idx = current_idx - 1
            else:
                low_idx = current_idx + 1
        return None
