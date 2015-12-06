# https://github.com/Empire-of-Code-Puzzles/checkio-empire-three-points-circle

# EQ:  (x-x0)^2+(y-y0)^2=r^2
import re, math

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __repr__(self):
        return "Point(%.2f, %.2f)" % (self.x, self.y)

P = re.compile(r'\([0-9],[0-9]\)')

def circle_equation(note):
    a, b, c = [Point(x[1], x[3]) for x in P.findall(note)]

    # find line between a and b: s1 + k * d1
    s1 = Point((a.x + b.x)/2.0, (a.y + b.y)/2.0)
    d1 = Point((b.y - a.y), -(b.x - a.x))

    # find line between a and c: s2 + k * d2
    s2 = Point((a.x + c.x)/2.0, (a.y + c.y)/2.0)
    d2 = Point((c.y - a.y), -(c.x - a.x))

    # intersection of both lines:
    # s1 + k * d1 == s2 + l * d2
    l = d1.x * (s2.y - s1.y) - d1.y * (s2.x - s1.x)
    l = l / (d2.x * d1.y - d2.y * d1.x)

    # circle center
    center = Point(s2.x + l * d2.x, s2.y + l * d2.y)

    dx = center.x - a.x
    dy = center.y - a.y
    radius = math.sqrt(dx * dx + dy * dy)

    x = str("%.2f" % center.x).rstrip('0').rstrip('.')
    y = str("%.2f" % center.y).rstrip('0').rstrip('.')
    r = str("%.2f" % radius).rstrip('0').rstrip('.')
    eq = "(x-%s)^2+(y-%s)^2=%s^2" % (x, y, r)

    return eq

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert circle_equation("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert circle_equation("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

    print("Use 'Check' to earn sweet rewards!")
