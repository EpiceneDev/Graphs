"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}   

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("That node already exists.")
        else:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 in self.vertices[v1]:
            print("This edge already exists. ")
        else:
            self.vertices[v1].add(v2)

    # ADJACENCY LIST MADE HERE
    def get_neighbors(self, vertex_id):  
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()

        # enqueue our starting node
        q.enqueue(starting_vertex)

        # make a set to track if we have traversed node already
        visited = set()

        # while our queue isn't empty
        while q.size() > 0:
        ## dequeeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
        ## if we haven't visited
            if current_node not in visited:
        ### mark as visited
                visited.add(current_node)
                print(current_node)
        ### get it neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors,
                for neighbor in neighbors:
        #### add to queue
                    q.enqueue(neighbor)
        # print("VISITED BFT: ", visited)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        #while our stack isn't empty
        while s.size() > 0:
        ## pop off top, this is the current_node
            current_node = s.pop()
        ## if we haven't visited this vertex before
            if current_node not in visited:
        ### mark as visited
                visited.add(current_node)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors
                for neighbor in neighbors:
        #### add to our stack
                    s.push(neighbor)
            # return visited

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

         # check if the node is visited
            # if not...
                # mark it as visited
                # print
                # call dft_recursive on each child  
        """
        
        visited = set()

        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

         BFS ALGORITHM
        # Create an empty queue
        # Add THE STARTING VERTEX TO A PATH (LIST) BEFORE ADDING IT to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first PATH
            # GRAB THE LAST VERTEX FROM THE PATH
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add A PATH TO all neighbors to the back of the queue
                    # (Make a copy of the path before adding)
        """
        visited = set()
        q = Queue()

        q.enqueue([starting_vertex])
        # visited.append(starting_vertex)

        while q.size() > 0:
             # Dequeue, the first PATH
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1]

             # CHECK IF IT'S THE TARGET 
            if last_vertex == destination_vertex:
                return path

            # Check if it's been visited
            if last_vertex not in visited:
                visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    #   BFS(graph, startVert):
    #       for v of graph.vertexes:
    #         v.color = white

    #       startVert.color = gray
        #     queue.enqueue(startVert)

    #       while !queue.isEmpty():
    #           u = queue[0]  // Peek at head of the queue, but do not dequeue!

    #           for v of u.neighbors:
    #             if v.color == white:
    #             v.color = gray
    #             queue.enqueue(v)

    #           queue.dequeue()
    #           u.color = black

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # dft the starting node
        #  place the nodes into stack
        #  when hit destination, return the stack
        #   in reverse order
        # DFS ALGORITHM
        # Create an empty stack
        # Add THE STARTING VERTEX TO A PATH (LIST) BEFORE ADDING IT to the stack
        # Create an empty set to store visited nodes
        # While the stack is not empty...
            # Pop, the last PATH
            # GRAB THE LAST VERTEX FROM THE PATH
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add A PATH TO all neighbors to the back of the stack
                    # (Make a copy of the path before adding)

        s = Stack()

        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            last_path = s.pop()

            last_vertex = last_path[-1]

            if last_vertex == destination_vertex:
                return last_path

            if last_vertex not in visited:
                visited.add(last_vertex)

                for neighbor in self.get_neighbors(last_vertex):
                    new_path = list(last_path)
                    new_path.append(neighbor)
                    s.push(new_path
                    )

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.

         BFS RECURSIVE ALGORITHM
        #check if starting vertex has been visited
        #if not...
            #if starting vertex is not destination:
                #return path
            #mark it as visited
            #call dfs_recursive on each neighbor
        """
        
        visited = set()

        path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
