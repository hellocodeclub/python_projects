import unittest
from dfs_bfs.datastructures import Stack, Queue,Cell, build_graph, dfs, dfs_recursive, bfs_shortest_path

class DataStructureTest(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        stack.add(1)
        stack.add(2)
        last_item = stack.pop()
        self.assertEqual(2,last_item)
        self.assertEqual([1],stack.list)

    def test_queue(self):
        queue = Queue()
        queue.add(1)
        queue.add(2)
        last_item = queue.pop()
        self.assertEqual(1,last_item)
        self.assertEqual([2],queue.list)
        queue.pop()
        last_item = queue.pop()
        self.assertEqual(None,last_item)

    def test_build_graph(self):
        matrix = [[1,1,1,1],[0,1,0,1],[1,0,0,1],[1,1,1,1]]
        graph = build_graph(matrix)
        dfs(graph,Cell(3,3))

    def test_dfs_recursive(self):
        matrix = [[1,1,1,1],[0,1,0,1],[1,0,0,1],[1,1,1,1]]
        graph = build_graph(matrix)
        dfs_recursive(graph,Cell(3,3))

    def test_bfs_shortest_path(self):
        matrix = [[1,1,1,1],[0,1,0,1],[1,0,0,1],[1,1,1,1]]
        graph = build_graph(matrix)
        shortest_path_distance = bfs_shortest_path(graph, Cell(2,3),Cell(2,0))
        print(shortest_path_distance)



