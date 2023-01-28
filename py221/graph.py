import unittest

class Vertex:
    """
    Simple Vertex Implementation for Graphs
    """
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
    
    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)
    
    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)

class DirectedGraph:
    """
    Directed Graph implementation using Adjacency List with utility functions
    """
    def __init__(self):
        self.al = []

    def get_vertices(self):
        return self.al
    
    def reset_visited(self):
        for vertex in self.al:
            vertex.visited = False
    
    def add_vertex(self, vertex):
        if vertex not in self.al:
            self.al.append(vertex)

    def remove_vertex(self, vertex):
        if vertex in self.al:
            for adjacent in vertex.edges:
                if vertex in adjacent.edges:
                    adjacent.edges.remove(vertex)
            
            self.al.remove(vertex)
    
    def add_edge(self, beginning, end):
        index = self.al.index(beginning)
        self.al[index].add_edge(end)
    
    def remove_edge(self, beginning, end):
        index = self.al.index(beginning)
        self.al[index].remove_edge(end)

def breadth_first_search(graph, value):
    """
    Breadth First Search the given graph for a vertex with the given value
    - Time Complexity: O(n + m) where n is the number of vertices and m is the number of edges
    - Space Complexity: O(n) where n is the number of vertices
    """
    graph.reset_visited()
    initial_vertex = graph.get_vertices()[0]
    initial_vertex.visited = True

    queue = [initial_vertex]
    while len(queue) > 0:
        current_vertex = queue.pop()
        if current_vertex.value == value:
            return current_vertex

        for adjacent_vertex in current_vertex.edges:
            if not adjacent_vertex.visited:
                queue.insert(0, adjacent_vertex)
                adjacent_vertex.visited = True
    
    return None

def depth_first_search_iterative(graph, value):
    """
    Iterative Depth First Search the given graph for a vertex with the given value
    - Time Complexity: O(n + m) where n is the number of vertices and m is the number of edges
    - Space Complexity: O(n) where n is the number of vertices
    """
    graph.reset_visited()
    initial_vertex = graph.get_vertices()[0]

    stack = [initial_vertex]
    while len(stack) > 0:
        current_vertex = stack.pop()
        if not current_vertex.visited:
            current_vertex.visited = True
            if current_vertex.value == value:
                return current_vertex

            for adjacent_vertex in current_vertex.edges:
                stack.append(adjacent_vertex)
    
    return None

def depth_first_search_recursive(graph, value):
    """
    Recursive Depth First Search the given graph for a vertex with the given value
    - Time Complexity: O(n + m) where n is the number of vertices and m is the number of edges
    - Space Complexity: O(n) where n is the number of vertices
    """
    def _depth_first_search(vertex):
        vertex.visited = True

        if vertex.value == value:
            return vertex
            
        for adjacent_vertex in vertex.edges:
            if not adjacent_vertex.visited:
                found = _depth_first_search(adjacent_vertex)
                if found != None:
                    return found

        return None

    graph.reset_visited()
    return _depth_first_search(graph.get_vertices()[0])

if __name__ == "__main__":
    def get_test_graph():
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
        graph.add_edge(a, b)
        graph.add_edge(a, c)
        graph.add_edge(b, c)
        graph.add_edge(b, e)
        graph.add_edge(b, d)
        graph.add_edge(c, e)
        graph.add_edge(d, e)
        graph.add_edge(e, c)
        graph.add_edge(e, a)
        return graph

    class TestGraph(unittest.TestCase):
        def test_all(self):
            search_algorithms = [breadth_first_search, depth_first_search_iterative, depth_first_search_recursive]
            graph = get_test_graph()
            for algorithm in search_algorithms:
                find_z = algorithm(graph, 'Z')
                self.assertEqual(find_z, None)
                find_e = algorithm(graph, 'E')
                self.assertEqual(find_e.value, 'E')
        
    unittest.main()