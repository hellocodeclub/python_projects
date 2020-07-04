import unittest
from coding_interview_delivery_route.delivery_route import build_graph, Cell, find_route

class DeliveryRouteTest(unittest.TestCase):
    def test_build_graph(self):
        graph = build_graph([[1,1,0],[0,1,2],[0,1,1]])
        self.assertEqual(1, len(graph.get(Cell(0,0).hashkey())))
        self.assertEqual(3, len(graph.get(Cell(1,1).hashkey())))

    def test_case2(self):
        min_distance = find_route([[1,1,0],[0,1,2],[0,1,1]])
        self.assertEqual(5,min_distance)

    def test_case3(self):
        min_distance = find_route([[1,1,1,1],[0,1,0,1],[0,1,0,1],[0,1,1,0],[0,1,2,1]])
        self.assertEqual(6, min_distance)