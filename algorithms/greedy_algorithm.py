# coding=utf-8

"""
Calculate minimum stations for covering all states.
"""


class GreedyAlgorithm:
    def run(self, stations: dict, states: set):
        not_covered_states = states.copy()
        result = set()

        # if there are not covered states
        while not_covered_states:
            # find the station of covering most not covered states
            best_covered_states = {}
            best_covered_station = None
            for station, covered_states in stations.items():
                covered = covered_states & not_covered_states
                if len(covered) > len(best_covered_states):
                    best_covered_states = covered
                    best_covered_station = station

            # if no station could cover more states, go end
            if not best_covered_station:
                break

            result.add(best_covered_station)
            not_covered_states -= best_covered_states

        return result
