"""This is the file for my Distance exercise"""

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """ string method """
        return "({},{})".format(self.x, self.y)

    def distance(self, p2=None):
        """ returns distance from self to p2 """
        if p2 is None:
            p2 = Point()
        dx = self.x - p2.x
        dy = self.y - p2.y
        return (dx ** 2 + dy ** 2) ** .5


point_1 = Point(-4, -4)
point_2 = Point(4, 4)

distance = point_1.distance(point_2)
print(distance)
