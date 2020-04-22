import unittest


class Road:
    def __init__(self, intersection1, intersection2, distance):
        self.intersection1 = intersection1
        self.intersection2 = intersection2
        self.distance = distance


class RoadNetwork:
    def __init__(self):
        print('todo')

    def get_neighbours(self, intersection):
        print('renvoie liste des intersections voisines')

    def get_distance(self, intersection1, intersection2):
        print('renvoie leur distance')
