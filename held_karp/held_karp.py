from typing import List, Tuple, Dict, Optional
import itertools
import sys

class HeldKarp:
    """
    Use Held-Karp Algorithm to calculate the lowest cost and shortes path for TSP
    """

    dists: List[List[int]]

    # Python dict as hashmap
    # Map of {last,    via subset} :  {cost, parent as second last}
    # Map of {city, bits for city} :  { int,                  city}
    map: Dict[Tuple[int, int], Tuple[int, int]]

    def __init__(self, dists: List[List[int]]):
        self.dists = dists
        self.map = {}

    def shortest_one_step(self,
                          last: int,
                          via: int,
                          cities: Tuple[int, ...],
                          ) -> Tuple[int, int]:
        """
        Find shortest path to via:
        1. From which prev last to current last
        2. Added total
        """
        
        prev_last: int
        cost: int = -1

        prev_last_i: int
        for prev_last_i in cities:
            if prev_last_i == last: continue  # Ignore if same city
            prev_via: int = via & ~(1 << prev_last_i)
            
            temp_tuple: Optional[Tuple[int, int]] = self.map.get((prev_last_i, prev_via))
            if temp_tuple is None:
                raise Exception("[ERROR] Memo entry not found (this should NOT happen)")
                sys.exit()
            prev_cost = temp_tuple[0]
            if cost == -1 or prev_cost + self.dists[prev_last_i][last] < cost:
                cost = prev_cost + self.dists[prev_last_i][last]
                prev_last = prev_last_i
        return (cost, prev_last)

    def tsp_shortest_path(self) -> Tuple[int, List[int]]:
        """
        Parameters:
            dists: distance matrix
        Returns:
            (cost, path): Tuple
        """

        city_count: int = len(self.dists)

        # Base cases:
        # city 0 is start
        # To every city (1..city_count - 1) via subset of none
        i: int
        for i in range(1, city_count):
            self.map[(i, 0)] = (self.dists[0][i], 0)

        # Bottom-up DP
        via_size: int 
        for via_size in range(1, city_count - 1):  # Will enumerate all combinations except 0

            # cities will be element of combination sequences
            # e.g. (1), (2), ...; (1 2), (1 3), (2 3), ...; (1 2 3), (1 2 4) ...
            cities: Tuple[int, ...]
            for cities in itertools.combinations(range(1, city_count), via_size):
                
                via: int = 0  # via subet as in bits, e.g. 00110 (Largest at left, 0 at right)
                city: int
                for city in cities:
                    via |= 1 << city  # This is via. Excluding last

                last: int
                for last in range(1, city_count):
                    if via // (2**last) % 2 == 0:  # Choose one of cities not in via to be last
                        self.map[(last, via)] = self.shortest_one_step(last, via, cities)
                        
        # Last step: Find shortest back to start
        via = 2**city_count - 2  # via subset = all other city except 0. 0 Will be now last
        self.map[(0, via)] = self.shortest_one_step(0, via, tuple(range(1, city_count)))

        min_cost: int = self.map[(0, via)][0]
        reversed_path: List[int] = [0]  # From end to start

        last = 0
        for i in range(city_count - 1):
            reversed_path.append(self.map[(last, via)][1])
            last = self.map[(last, via)][1]
            via &= ~(1 << last)

        reversed_path.append(0)
        reversed_path.reverse()  # Reverse at the end
        return (min_cost, reversed_path)

    