
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

# dfs and keep track of the longest path
# '''
# def dfs_recursive(self, vertex, destination_vertex, path=None, visited=None):
#         if path is None:
#             path = []
#         if visited is None:
#             visited = set()
#         visited.add(vertex)
#         path = path + [vertex]

#         if vertex == destination_vertex:
#             return path

#         for neighbor in self.get_neighbors(vertex):
#             print("NEIGHBOR: ", neighbor)
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 new_path = self.dfs_recursive(neighbor, destination_vertex, path, visited)
#                 if new_path:
#                     return new_path
#         return None

    def earliest_ancestor(ancestors, starting_node):
#     # there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
#     # If the input individual has no parents, the function should return -1.
#     # Nodes are unique, no cycles in edges, 
#     # inputs are not empty
#     # id's are positive
#     # can be multiple children per parent
#     # node = (parent, child)
#     """

#     # make a graph and populate it with the given data
#     graph = Graph()
#     # go thru each ancestor in ancestors
#     ## check for ancestor[0] in graph, 
#     ### if no, add to graph
#     ## check for ancestor[1] in graph,
#     ### if no, add to graph
#     ## if yes, do bfs
#     save length of path and last in queue
#     ### compare length to old length
#     #### if length is longer
#     #### save the last queue
#     ### recurse the call
#     ## return the vertex from longest path

#     # Build Q

#     # Add starting node to Q

#     # Keep track of longest path and leaf

    


#     """

#     graph = Graph()

#     # Build the graph backwards
#     for pair in ancestors:
        
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # BUILD EDGES IN REVERSE!
#         graph.add_edge(pair[1], pair[0])

#     # BFS for storing the path
        q = Queue()
    
        q.enqueue([starting_node])

        max_path_len = 1
        earliest_ancestor = -1 #TODO WHY?

        while q.size() > 0:
            path = q.dequeue
            v = path[-1]

            if (len(path) >- max_path_len and v < earliest_ancestor or (len(path) > max_path_len)):
                earliest_ancestor = v
                max_path_len = len(path)

            for neighbor in graph.vertices[v]:
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
        return earliest_ancestor

# def earliest_ancestor(ancestors, starting_node):
#     # Build the graph
#     graph = Graph()
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # Build edges in reverse
#         graph.add_edge(pair[1], pair[0])
#     # Do a BFS (storing the path)
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_len = 1
#     earliest_ancestor = -1
#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]
#         # If the path is longer or equal and the value is smaller, or if the path is longer)
#         if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = v
#             max_path_len = len(path)
#         for neighbor in graph.vertices[v]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
#     return earliest_ancestor