
class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def test_zero(self):
        side = None
        if side in self.sides == 0:
            return False
        else:
            return True

    def test_sum(self):
        sum1 = self.sides[0] + self.sides[1]
        sum2 = self.sides[1] + self.sides[2]
        sum3 = self.sides[0] + self.sides[2]
        if (sum1 > self.sides[2]) and (sum2 > self.sides[0]) and (sum3 > self.sides[1]):
            return True
        else:
            return False


def is_equilateral(sides):
    triangle = Triangle(sides)
    if triangle.test_sum() == False:
        return False
    if triangle.test_zero() != True:
        return False
    if sides[0] == sides[1] and sides[0] == sides[2]:
        return True
    else:
        return False


def is_isosceles(sides):
    triangle = Triangle(sides)
    if triangle.test_sum() == False:
        return False
    if triangle.test_zero() != True:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return True
    else:
        return False


def is_scalene(sides):
    triangle = Triangle(sides)
    if triangle.test_sum() == False:
        return False
    if triangle.test_zero() != True:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return False
    else:
        return True

