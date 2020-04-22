from rendu.classes.road import Road
from rendu.classes.road import RoadNetwork

import unittest

class RoadNetworkTest(unittest.TestCase):

    def test_shortest_path(self):
        roads_list = [
            Road(0, 1, 4),
            Road(0, 7, 8),
            Road(1, 7, 11),
            Road(1, 2, 8),
            Road(7, 8, 7),
            Road(7, 6, 1),
            Road(2, 8, 2),
            Road(8, 6, 6),
            Road(2, 3, 7),
            Road(2, 5, 4),
            Road(5, 6, 2),
            Road(3, 5, 14),
            Road(3, 4, 9),
            Road(4, 5, 10)
        ]

        network = RoadNetwork(roads_list, 9)

        self.assertEqual(network.shortest_path(0, 0), 0)
        self.assertEqual(network.shortest_path(0, 1), 4)
        self.assertEqual(network.shortest_path(0, 2), 12)
        self.assertEqual(network.shortest_path(0, 3), 19)
        self.assertEqual(network.shortest_path(0, 4), 21)
        self.assertEqual(network.shortest_path(0, 5), 11)
        self.assertEqual(network.shortest_path(0, 6), 9)
        self.assertEqual(network.shortest_path(0, 7), 8)
        self.assertEqual(network.shortest_path(0, 8), 14)
