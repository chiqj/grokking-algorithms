# coding=utf-8

from collections import deque


class FindPathExist:
    def search(self, graph: dict, start_vertice, end_vertice) -> bool:
        # create FIFO queue and variable to store searched vertices
        search_queue = deque()
        searched = set()
        # put the start vertice in queue
        search_queue.append(start_vertice)
        while search_queue:
            # pop one vertice from queue
            vertice = search_queue.popleft()
            if vertice not in searched:
                if vertice == end_vertice:
                    return True
                # if not the target vertice,
                # record it is searched and put neighbors in queue
                else:
                    search_queue.extend(graph[vertice])
                    searched.add(vertice)
        return False
