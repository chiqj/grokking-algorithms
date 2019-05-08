# coding=utf-8


class DijkstraAlgorithm:
    def find_min_cost_vertice(self, costs: dict, processed: set):
        not_processed_vertice_costs = {
            vertice: cost for vertice, cost in costs.items()
            if vertice not in processed
        }
        return min(
            not_processed_vertice_costs,
            default=None,
            key=lambda x: not_processed_vertice_costs[x],
        )

    def get_path(self, parents: dict, start_vertice, end_vertice):
        result = [end_vertice]
        while result[0] != start_vertice:
            prev_vertice = parents.get(result[0])
            if prev_vertice:
                result.insert(0, prev_vertice)
            else:
                break
        return result

    def run(self, graph: dict, start_vertice, end_vertice):
        # process the start vertice
        costs = {
            vertice: cost for vertice, cost in graph[start_vertice].items()
        }
        parents = {vertice: start_vertice for vertice in graph[start_vertice]}
        processed = {start_vertice}

        # find the minimum cost vertice in costs, update neighbors
        # until all vertice in costs have been processed
        vertice = self.find_min_cost_vertice(costs, processed)
        while vertice is not None:
            cost = costs[vertice]
            neighbors_cost = graph[vertice]
            for neighbor in neighbors_cost:
                new_cost = cost + neighbors_cost[neighbor]
                if neighbor in costs and costs[neighbor] <= new_cost:
                    pass
                else:
                    costs[neighbor] = new_cost
                    parents[neighbor] = vertice
            processed.add(vertice)
            vertice = self.find_min_cost_vertice(costs, processed)

        return (
            costs[end_vertice],
            self.get_path(parents, start_vertice, end_vertice),
        )
