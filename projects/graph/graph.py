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
        # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        # Get the relevant vertex
        v1_edges_set = self.vertices[v1]

        # add to a set by doing .add
        v1_edges_set.add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        # Adjacency lists are easy to get neighbors from
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # enqueue the starting_vertex
        q.enqueue(starting_vertex)
        # create a set to track vertices we have visited
        visited = set()
        # while the queue isn't empty:
        while q.size() > 0:
            # dequeue, this is our current_node
            current_node = q.dequeue()
        # if we haven't visited it yet
            if current_node not in visited:
                # mark as visited
                print(current_node)
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # and add each to the back of queue
                for neighbor in neighbors:
                    q.enqueue(neighbor)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # create an empty stack
        stack = Stack()
        # push the starting_vertex onto the stack
        stack.push(starting_vertex)
        # create a visited set
        visited = set()

        # while our stack isn't empty:
        while stack.size() > 0:
            # pop off what's on top, this is current_node
            current_node = stack.pop()
            # if it hasn't been visited
            if current_node not in visited:
                print(current_node)
                # set is as visited
                visited.add(current_node)
                # get the node's neighbors
                neighbors = self.get_neighbors(current_node)
                # iterate through the neighbors and add each to the stack
                for neighbor in neighbors:
                    stack.push(neighbor)
        return visited

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:  # check if we were provided a set of visited nodes
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Write a function within your Graph class that takes takes a starting node
        and a destination node as an argument, then performs BFS.
        Your function should return the shortest path from the start node
        to the destination node. Note that there are multiple valid paths.

        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        Q = Queue()
        visited = set()
        Q.enqueue([starting_vertex])

        while Q.size():
            current_path = Q.dequeue()
            # last node in the path is the current_vertex
            current_vertex = current_path[-1]
            if current_vertex is destination_vertex:  # if the last vert matches the vert we're looking for
                return current_path
            elif current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        neighbor_path = current_path.copy()
                        neighbor_path.append(neighbor)
                        Q.enqueue(neighbor_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Write a function within your Graph class that takes takes a starting node
        and a destination node as an argument, then performs DFS.
        Your function should return a valid path (not necessarily the shortest)
        from the start node to the destination node.
        Note that there are multiple valid paths.

        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])

        while stack.size():
            current_path = stack.pop()
            current_vertex = current_path[-1]

            if current_vertex is destination_vertex:
                return current_path
            elif current_vertex not in visited:
                visited.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
                    stack.push(neighbor_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        # always use None as default for any mutable arguments you will use!
        # https://florimond.dev/blog/articles/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
        """
        Write a function within your Graph class that takes takes a starting node
        and a destination node as an argument, then performs DFS using recursion.
        Your function should return a valid path (not necessarily the shortest)
        from the start node to the destination node.
        Note that there are multiple valid paths.

        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = []
        if visited is None:
            visited = set()
        print("start vert", starting_vertex)
        print("path", path)
        path = path + [starting_vertex]

        visited.add(starting_vertex)

        if starting_vertex is destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            print("neighbor", neighbor)
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(
                    neighbor, destination_vertex, path, visited)
                if neighbor_path and neighbor_path[-1] is destination_vertex:
                    return neighbor_path
        return None


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
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
