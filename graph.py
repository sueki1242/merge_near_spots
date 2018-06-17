# coding : utf-8

class Edge:
    """edge of ({source} -> {target}) with cost {distance}"""
    def __init__(self, source, target, distance):
        self.source = source
        self.target = target
        self.distance = distance

    def get_distance(self):
        return self.distance

    def __str__(self):
        return "[({} -> {}), {}]".format(
            self.source, self.target, self.distance)

class Graph:
    """represent graph as adjacency list"""
    def __init__(self, num_node):
        self.links = []
        for i in range(num_node):
            self.links.append([])

    def addEdge(self, source, target, distance):
        self.links[source].append(Edge(source, target, distance))

    def get_out_links(self, source):
        return self.links[source]
