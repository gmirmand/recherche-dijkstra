import sys
import unittest


class Road:
    def __init__(self, intersection1, intersection2, distance):
        self.intersection1 = intersection1
        self.intersection2 = intersection2
        self.distance = distance


class RoadNetwork:
    def __init__(self, road_list, intersections):
        self.road_list = road_list
        self.intersections = intersections
        self.nb_intersection = len(intersections)

    def get_neighbours(self, intersection):
        neighbours = []

        for item in self.road_list:
            if item.intersection1 == intersection:
                neighbours.append(item.intersection2)
            if item.intersection2 == intersection:
                neighbours.append(item.intersection1)

        return neighbours

    def get_distance(self, intersection1, intersection2):
        distance = 0

        for item in self.road_list:
            # De manière à comprendre si on met en paramètre 1,7 ou 7,1
            if (item.intersection1 == intersection1 and item.intersection2 == intersection2) or (
                    item.intersection2 == intersection1 and item.intersection1 == intersection2):
                distance = item.distance

        if distance == 0:
            print('Les 2 intersections ne sont pas valide (non voisines ou inexistantes)')
        else:
            return distance

    def shortest_path(self, origin, destination):
        sorted_intersections = []
        min_distances = {}

        # Construct min_distances
        for item in self.intersections:
            if item == origin:
                min_distances[item] = 0
            else:
                min_distances[item] = sys.maxsize

        # algorithm
        intersection = origin
        while len(sorted_intersections) != self.nb_intersection:
            i = None
            min = sys.maxsize
            for item in min_distances:
                if min_distances[item] < min and sorted_intersections.count(item) == 0:
                    i = item
                    min = min_distances[item]
                    sorted_intersections.append(i)

            i_neighbours = self.get_neighbours(i)

            for neighbour in i_neighbours:
                distance_v_i = self.get_distance(neighbour, i)
                distance_v_n = distance_v_i + min_distances[i]
                if min_distances.get(neighbour) > distance_v_n:
                    min_distances[neighbour] = distance_v_n
                    intersection = i

        return min_distances.get(destination)


network_road_list = [
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

network_road_intersections = [0, 1, 2, 3, 4, 5, 6, 7, 8]

Network = RoadNetwork(network_road_list, network_road_intersections)

intersection0_neighbours = Network.get_neighbours(0)
intersection07_distance = Network.get_distance(1, 7)
Network.shortest_path(0, 0)
