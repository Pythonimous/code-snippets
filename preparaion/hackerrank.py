import copy


class Graph(object):

    def __init__(self, n):
        self.edges = {vertex: [] for vertex in range(n)}

    def connect(self, x, y):
        self.edges[x].append(y)

    # self.edges[y].append(x)

    def find_all_distances(self, s):
        self.distances = {
            vert: float('inf') for vert in self.edges
        }
        self.distances[s] = 0

        finalized_distances = set()
        to_finalize = [*range(n)]

        while to_finalize:

            closest_vertex = min(to_finalize, key=lambda v: self.distances[v])
            for neighbor in self.edges[closest_vertex]:
                if neighbor not in finalized_distances:
                    self.distances[neighbor] = min(
                        self.distances[neighbor],
                        self.distances[closest_vertex] + 6
                    )
            finalized_distances.add(closest_vertex)
            to_finalize.remove(closest_vertex)

        del self.distances[s]

        out_distances = [(k, v) for k, v in self.distances.items()]
        out_distances.sort()
        out_distances = [pair[1] if pair[1] != float('inf') else -1 for pair in out_distances]
        print(*out_distances)


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
