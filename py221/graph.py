import unittest
import sys
import heap

class Vertex:
    """
    Simple Vertex Implementation for Graphs
    """
    def __init__(self, value):
        self.value = value
        self.visited = False

class Edge:
    """
    Simple Edge Implementation for Graphs
    """
    def __init__(self, beginning, end, weight=1):
        self.beginning = beginning
        self.end = end
        self.weight = weight

class Graph:
    """
    Graph implementation using Adjacency List with utility functions
    """
    def __init__(self):
        self.al = {}

    def get_vertices(self):
        return list(self.al.keys())
    
    def get_vertex_edges(self, vertex):
        return self.al[vertex]
    
    def reset_visited(self):
        for vertex in self.al.keys():
            vertex.visited = False
    
    def add_vertex(self, vertex):
        if vertex not in self.al:
            self.al[vertex] = []

class UndirectedGraph(Graph):
    """
    Undirected Graph implementation using Adjacency List with utility functions
    """
    def add_edge(self, edge):
        if edge.beginning in self.al and edge.end in self.al:
            self.al[edge.beginning].append(edge)
            self.al[edge.end].append(Edge(edge.end, edge.beginning, edge.weight))

class DirectedGraph(Graph):
    """
    Directed Graph implementation using Adjacency List with utility functions
    """    
    def add_edge(self, edge):
        if edge.beginning in self.al:
            self.al[edge.beginning].append(edge)

def BFS(graph, value):
    """
    Breadth First Search the given graph for a vertex with the given value
    - Time Complexity: O(n + m) where n is the number of vertices and m is the number of edges
    - Space Complexity: O(n) where n is the number of vertices
    """
    def breadth_first_search(vertex):
        vertex.visited = True

        queue = [vertex]
        while len(queue) > 0:
            current_vertex = queue.pop()

            if current_vertex.value == value:
                return current_vertex

            for edge in graph.get_vertex_edges(current_vertex):
                if not edge.end.visited:
                    queue.insert(0, edge.end)
                    edge.end.visited = True
        
        return None

    # This for loop is used for searching for a graph with disconnected components
    graph.reset_visited()
    for vertex in graph.get_vertices():
        found = breadth_first_search(vertex)
        if found != None:
            return found
        
    return None

def DFS_iterative(graph, value):
    """
    Iterative Depth First Search the given graph for a vertex with the given value
    - Time Complexity: O(n + m) where n is the number of vertices and m is the number of edges
    - Space Complexity: O(n) where n is the number of vertices
    """
    def depth_first_search_iterative(vertex):
        stack = [vertex]
        while len(stack) > 0:
            current_vertex = stack.pop()
            if not current_vertex.visited:
                current_vertex.visited = True

                if current_vertex.value == value:
                    return current_vertex

                for edge in graph.get_vertex_edges(current_vertex):
                    stack.append(edge.end)
        
        return None
    
    # This for loop is used for searching for a graph with disconnected components
    graph.reset_visited()
    for vertex in graph.get_vertices():
        found = depth_first_search_iterative(vertex)
        if found != None:
            return found
        
    return None

def DFS_recursive(graph, value):
    """
    Recursive Depth First Search the given graph for a vertex with the given value
    - Time Complexity: O(n + m) where n is the number of vertices and m is the number of edges
    - Space Complexity: O(n) where n is the number of vertices
    """
    def depth_first_search_recursive(vertex):
        vertex.visited = True

        if vertex.value == value:
            return vertex
            
        for edge in graph.get_vertex_edges(vertex):
            if not edge.end.visited:
                found = depth_first_search_recursive(edge.end)
                if found != None:
                    return found

        return None

    # This for loop is used for searching for a graph with disconnected components
    graph.reset_visited()
    for vertex in graph.get_vertices():
        found = depth_first_search_recursive(vertex)
        if found != None:
            return found
        
    return None

def Kruskal(graph):
    """
    Kruskal's algorithm to find the minimum spanning forest in a weighted, undirected graph
    - Time Complexity: O(mlogm) where m is the number of edges
    - Space Complexity: O(n) where n is the number of vertices
    """
    def union(set, x, y):
        set[x] = y
        
    def find(set, x):
        # Using path compression by reassigning each parent
        if set[x] != x:
            set[x] = find(set, set[x])
        return set[x]
        
    spanning_tree = []
    vertex_sets = list(map(lambda vertex : vertex.value, graph.get_vertices()))

    # Iterate over a list of edges, sorted by their weight
    edges = sorted(set([edge for vertex in graph.get_vertices() for edge in graph.get_vertex_edges(vertex)]), key=lambda edge : edge.weight)
    for edge in edges:
        # If the edge does not create a cycle, add it to the spanning tree and mark vertices as connected
        if find(vertex_sets, edge.beginning.value) != find(vertex_sets, edge.end.value):
            spanning_tree.append((edge.beginning.value, edge.end.value))
            union(vertex_sets, edge.beginning.value, edge.end.value)
        
        # Stop when the total number of edges in spanning tree is V - 1
        if len(spanning_tree) + 1 == len(vertex_sets):
            break

    return spanning_tree

def Dijkstra(graph, source):
    """
    Dijkstra's algorithm to find the shortest path from the source node to all other nodes in a weighted graph
    - Time Complexity: O(nlogn + mlogn) where n is the number of vertices and m is the number of edges
                       Note that the current implementation does not use a priority queue, therefore O(n^2)
    - Space Complexity: O(n) where n is the number of vertices
    """
    # Mark all vertices as unvisited
    graph.reset_visited()

    # Create a set of unvisited vertices
    unvisited_vertices = graph.get_vertices()

    # Create a list of distances from the source node to a specific node with initial value = +inf
    distances = dict.fromkeys(unvisited_vertices, sys.maxsize)
    distances[source] = 0

    while len(unvisited_vertices) > 0:
        # Set the current vertex to the unvisited node with the minimum distance
        current_vertex = min(unvisited_vertices, key=lambda vertex : distances[vertex])

        # Mark the current vertex as visited and remove it from the unvisited vertices set
        current_vertex.visited = True
        unvisited_vertices.remove(current_vertex)

        # For the current vertex, visit all of its unvisited neighbours and update their distance
        for edge in graph.get_vertex_edges(current_vertex):
            if not edge.end.visited and distances[current_vertex] + edge.weight < distances[edge.end]:
                distances[edge.end] = distances[current_vertex] + edge.weight

    return distances

if __name__ == "__main__":
    def get_test_unweighted_directed_graph():
        graph = DirectedGraph()
        a = Vertex('A')
        b = Vertex('B')
        c = Vertex('C')
        d = Vertex('D')
        e = Vertex('E')
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_edge(Edge(a, b))
        graph.add_edge(Edge(a, c))
        graph.add_edge(Edge(b, c))
        graph.add_edge(Edge(b, e))
        graph.add_edge(Edge(c, e))
        graph.add_edge(Edge(d, e))
        graph.add_edge(Edge(e, c))
        graph.add_edge(Edge(e, a))
        return graph
    
    def get_test_weighted_undirected_graph():
        graph = UndirectedGraph()
        a = Vertex(0)
        b = Vertex(1)
        c = Vertex(2)
        d = Vertex(3)
        e = Vertex(4)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_edge(Edge(a, b, 3))
        graph.add_edge(Edge(a, c, 6))
        graph.add_edge(Edge(b, c, 7))
        graph.add_edge(Edge(b, e, 8))
        graph.add_edge(Edge(c, d, 2))
        graph.add_edge(Edge(c, e, 1))
        graph.add_edge(Edge(d, e, 11))
        graph.add_edge(Edge(e, a, 5))
        return graph

    class TestGraph(unittest.TestCase):
        def test_unweighted_directed_grap_all(self):
            search_algorithms = [BFS, DFS_iterative, DFS_recursive]
            graph = get_test_unweighted_directed_graph()
            for algorithm in search_algorithms:
                find_z = algorithm(graph, 'Z')
                self.assertEqual(find_z, None)
                find_e = algorithm(graph, 'E')
                self.assertEqual(find_e.value, 'E')
        
        def test_kruskals(self):
            graph = get_test_weighted_undirected_graph()
            self.assertEqual(Kruskal(graph), [(2, 4), (2, 3), (0, 1), (4, 0)])

        def test_dijkstra(self):
            graph = UndirectedGraph()
            a = Vertex('A')
            b = Vertex('B')
            c = Vertex('C')
            d = Vertex('D')
            e = Vertex('E')
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_edge(Edge(a, b, 3))
            graph.add_edge(Edge(a, c, 6))
            graph.add_edge(Edge(b, c, 7))
            graph.add_edge(Edge(b, e, 8))
            graph.add_edge(Edge(c, d, 2))
            graph.add_edge(Edge(c, e, 1))
            graph.add_edge(Edge(d, e, 11))
            graph.add_edge(Edge(e, a, 5))
            self.assertEqual(Dijkstra(graph, a), { a: 0, b: 3, c: 6, d: 8, e: 5 })
        
    unittest.main()