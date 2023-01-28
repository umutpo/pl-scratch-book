import unittest

class Edge:
    """
    Simple Edge Implementation for Graphs
    """
    def __init__(self, beginning, end, weight=1):
        self.beginning = beginning
        self.end = end
        self.weight = weight

class Vertex:
    """
    Simple Vertex Implementation for Graphs
    """
    def __init__(self, value):
        self.value = value
        self.visited = False

class DirectedGraph:
    """
    Directed Graph implementation using Adjacency List with utility functions
    """
    def __init__(self):
        self.al = {}

    def get_vertices(self):
        return self.al.keys()
    
    def get_vertex_edges(self, vertex):
        return self.al[vertex]
    
    def reset_visited(self):
        for vertex in self.al.keys():
            vertex.visited = False
    
    def add_vertex(self, vertex):
        if vertex not in self.al:
            self.al[vertex] = []
    
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

            for adjacent_vertex in graph.get_vertex_edges(current_vertex):
                if not adjacent_vertex.end.visited:
                    queue.insert(0, adjacent_vertex.end)
                    adjacent_vertex.end.visited = True
        
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
        graph.reset_visited()

        stack = [vertex]
        while len(stack) > 0:
            current_vertex = stack.pop()
            if not current_vertex.visited:
                current_vertex.visited = True

                if current_vertex.value == value:
                    return current_vertex

                for adjacent_vertex in graph.get_vertex_edges(current_vertex):
                    stack.append(adjacent_vertex.end)
        
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
            
        for adjacent_vertex in graph.get_vertex_edges(vertex):
            if not adjacent_vertex.end.visited:
                found = depth_first_search_recursive(adjacent_vertex.end)
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

if __name__ == "__main__":
    def get_test_unweighted_graph():
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
        graph.add_edge(Edge(b, d))
        graph.add_edge(Edge(c, e))
        graph.add_edge(Edge(d, e))
        graph.add_edge(Edge(e, c))
        graph.add_edge(Edge(e, a))
        return graph

    class TestGraph(unittest.TestCase):
        def test_all(self):
            search_algorithms = [BFS, DFS_iterative, DFS_recursive]
            graph = get_test_unweighted_graph()
            for algorithm in search_algorithms:
                find_z = algorithm(graph, 'Z')
                self.assertEqual(find_z, None)
                find_e = algorithm(graph, 'E')
                self.assertEqual(find_e.value, 'E')
        
    unittest.main()