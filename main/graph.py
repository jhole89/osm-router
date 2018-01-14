class Graph:
    def __init__(self, graph_dict=None):
        """
        An in memory directional graph

        :param graph_dict: a directional graph
        :type graph_dict: dict
        """

        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict

    @property
    def graph_dict(self):
        return self._graph_dict

    @property
    def nodes(self):
        return list(self._graph_dict.keys())

    def add_node(self, node):
        """
        Add a new node to the graph

        :param node: a node
        """
        if node not in self._graph_dict:
            self._graph_dict[node] = {}

    def add_edge(self, edge, directional=True):
        """
        Add a new edge to the graph

        :param edge: an edge connecting two nodes
        :param directional: boolean declaring edge to be direction to bidirectional
        """
        (node1, node2, dist) = tuple(edge)
        self._add_directional_edge(node1, node2, dist)

        if not directional:
            self._add_directional_edge(node2, node1, dist)

    def _add_directional_edge(self, origin, dest, dist):
        """
        Adds a directional edge to the graph

        :param origin: start node
        :param dest: end node
        :param dist: weight of edge
        """
        if origin in self._graph_dict:
            self._graph_dict[origin][dest] = int(dist)
        else:
            self._graph_dict[origin] = {dest: int(dist)}

    def get_shortest_path(self, start, end):
        """
        Calculate the shortest path for a directed weighted graph.

        :param start: start node
        :param end: end node
        :return: length of shortest path
        """

        nodes_to_visit = {start}
        visited_nodes = set()

        distance_from_start = {start: 0}
        tentative_parents = {}

        while nodes_to_visit:
            # The next node should be the one with the smallest weight
            current = min([(distance_from_start[node], node) for node in nodes_to_visit])[1]

            if current == end:
                break

            nodes_to_visit.discard(current)
            visited_nodes.add(current)

            edges = self.graph_dict[current]
            unvisited_neighbours = set(edges).difference(visited_nodes)

            for neighbour in unvisited_neighbours:
                neighbour_distance = distance_from_start[current] + edges[neighbour]

                if neighbour_distance < distance_from_start.get(neighbour, float('inf')):
                    distance_from_start[neighbour] = neighbour_distance
                    tentative_parents[neighbour] = current
                    nodes_to_visit.add(neighbour)

        return distance_from_start[end]
