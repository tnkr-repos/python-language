import math


class Vector2d:

    def __init__(self, x, y):
        """Converting x and y to float in __init__ catches errors early, which is helpful in case Vector2d is called with unsuitable arguments"""
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        """__iter__ makes a Vector2d iterable; that is what makes unpacking work. We implement it simply by using a generator expression to yield the components one after the other"""
        return (i for i in (self.x, self.y))

    def __repr__(self):
        """__repr__ builds a string by interpolation the components with {!r} to get their repr; because Vector2d is iterable, *self feeds the x and y components to format"""
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        """From an iterable Vector2d, its easy to build a tuple to display as an ordered pair"""
        return str(tuple(self))

    def __eq__(self, other):
        """To quickly compare all components build tuples out of the operands. But this also returns True when comparing Vector2d instances to other iterables holding the same numerical values (Vector2d(3, 4) == [3, 4])"""
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """__bool__ uses abs(self) to compute the magnitude, then converts it to bool so 0.0 becomes False and nonzero is True"""
        return bool(abs(self))
