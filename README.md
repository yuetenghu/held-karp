# Held-Karp Algorithm
Python implementation (with typing) of Held-Karp Algorithm for TSP

## Algorithm

The Held–Karp algorithm is a dynamic programming algorithm solve the Traveling Salesman Problem (TSP), i.e. to find the shortest path to traverse all destinations and return to the starting point.

To find out more about Held-Karp algorithm, visit [Wikipedia Page](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm).

## Implementation Features

### 1 Notation for better understanding

To expedite understanding, the code implementation is designed as identical with the notation in Wikipedia page as possible as following.

```
Implementation (see `map` below)

g(x, S) - starting from 1, path min cost ends at vertex x, passing vertices in set S exactly once
x: last
S: via subset

p(x, S) - the second-to-last vertex to x from set S. Used for constructing the TSP path back at the end.
x: parent as second last
```

```python
# Python dict as hashmap
# Map of {last,    via subset} :  {cost, parent as second last}
# Map of {city, bits for city} :  { int,                  city}
map: Dict[Tuple[int, int], Tuple[int, int]]
```

I hope you'll find this implementation resonate with Wikipedia notes, hence more understandable.

### 2 Asymmetric distance

It **supports asymmetric distance values**, for instance, the distance from A to B can be different from B to A.

### 3 Typing

Python Typing are included in the implementation, e.g. `Tuple Dict List Optional`.

This would make the code more readable.

## Usage

A test script `held_karp_test.py` is included, which also serves as a usage sample.

There are three test cases in the ``held_karp_test.py``, with input distance matrices of size `4*4`, `5*5`, and `17*17`.

The diagonal in the distance matrix could be any value (e.g. `0`, `9999`, or other), since it will be ignored in the code.

```shell
python held_karp_test.py
```

To run the test script, simply use the command above.

### Output

```shell
$ python held_karp_test.py
Minimum cost: 21
Shortest_path: [0, 2, 3, 1, 0]
Minimum cost: 215
Shortest_path: [0, 3, 2, 4, 1, 0]
Minimum cost: 39
Shortest_path: [0, 11, 16, 8, 7, 4, 3, 15, 14, 6, 5, 12, 10, 9, 1, 13, 2, 0]
.
----------------------------------------------------------------------
Ran 1 test in 3.246s

OK
```

The algorithm will return both:

-   **Minimum cost**
-   **Shortest path**, including the starting point at the beginning and the end