"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    # def add_edge(self, start, end, bidirectional=True):
    #     self.vertices[start].add(start)
    #     if bidirectional:
    #         self.vertices[end].add(end)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices: 
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    # def dfs(self, start, target=None):
    #     x = []
    #     x.append(start)
    #     y = set(x)

    #     while x:
    #         z = x.pop()
    #         if x == target:
    #             break
    #         x.extend(self.vertices[z])

    #     return x
    def dfs(self, start_vert, target_value=None):
        visited = []
        visited.append(start_vert)
        y = set(visited)

        while visited:
            z = visited.pop()
            if visited == target_value:
                break
            visited.extend(self.vertices[z])

        return visited
    def graph_rec(self, start, target=None):
        x = set()
        x.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
