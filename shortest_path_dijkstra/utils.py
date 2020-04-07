import copy

class Graph(object):

    def __init__(self, graph_dict=None, weight_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        if weight_dict is None:
            weight_dict = {}
        self.__graph_dict = graph_dict
        self.__weight_dict = weight_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def get_neighbors(self, vertex):
        """ returns neighbors of a vertex """
        return self.__graph_dict[vertex]

    def edge_weight(self, vert1, vert2):
        keys = set(self.__weight_dict.keys())
        if vert1+vert2 in keys:
            weight = self.__weight_dict[vert1+vert2]
        elif vert2+vert1 in keys:
            weight = self.__weight_dict[vert2+vert1]
        else:
            weight = 0
        return weight

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


def shortest_path(graph, start, finish):

    distances = dict()  # Primary distance dictionary
    distances[start] = 0

    for vertex in graph.vertices():
        if vertex == start:
            distances[vertex] = 0
        else:
            distances[vertex] = 10**10  # If edges are longer, modify accordingly
    unvisited_distances = copy.deepcopy(distances)  # Secondary "unvisited" distance dictionary

    while unvisited_distances:
        vertex = min(unvisited_distances,
                     key=unvisited_distances.get)  # Min weight vertex we haven't visited yet
        del unvisited_distances[vertex]

        neighbors = graph.get_neighbors(vertex)
        for neighbor in neighbors:
            new_distance = distances[vertex]\
                           + graph.edge_weight(vertex, neighbor)
            if new_distance < distances[neighbor]:  # Is new path shorter?
                distances[neighbor] = new_distance
                if neighbor in unvisited_distances:
                    unvisited_distances[neighbor] = new_distance

    return distances[finish]
