from math import sqrt


class Vector3(list):
    """ 
    A simple vector.
    """
    def __init__(self, *values):
        """ 
        Construct the vector from the given values.
        """
        if not values:
            self.append(0.0)
            self.append(0.0)
            self.append(0.0)
        else:
            for value in values:
                assert(type(value) == float)
                self.append(value)

    def __add__(self, other):
        """ 
        Add one vector to another: result = self + other
        """
        assert(len(other) == len(self))
        return Vector3(self[0] + other[0], self[1] + other[1], 
                       self[2] + other[2]) 

    def __iadd__(self, other):
        """ 
        Add one vector to another: self += other
        """
        assert(len(other) == len(self))
        self[0] += other[0]
        self[1] += other[1]
        self[2] += other[2]
        return self

    def __sub__(self, other):
        """ 
        Subtract one vector from another: result = self - other
        """
        assert(len(other) == len(self))
        return Vector3(self[0] - other[0], self[1] - other[1], 
                       self[2] - other[2]) 

    def __isub__(self, other):
        """ 
        Subtract one vector from another: self -= other
        """
        assert(len(other) == len(self))
        self[0] -= other[0]
        self[1] -= other[1]
        self[2] -= other[2]
        return self

    def __mul__(self, other):
        """
        Scalar multiplication: result = self * val
        """
        return Vector3(self[0] * float(other), 
                       self[1] * float(other), 
                       self[2] * float(other)) 

    def __imul__(self, other):
        """
        self *= scalar
        """
        self[0] *= float(other)
        self[1] *= float(other)
        self[2] *= float(other)
        return self

    def __rmul__(self, other):
        """
        Scalar multiplication: result = other * self

        The other right hand side operators didn't have 
        to be overridden because both sides of the 
        operation are vectors, with their operators overridden. 
        In this case, the left side is other, and so the right 
        side must be overridden for the operator to work.
        """
        return self.__mul__(other)

    def __div__(self, other):
        """
        Scalar division: result = self / other
        """
        return Vector3(self[0] / float(other), 
                       self[1] / float(other), 
                       self[2] / float(other))

    def __idiv__(self, other):
        """
        Scalar division: self /= other
        """
        self[0] /= float(other)
        self[1] /= float(other)
        self[2] /= float(other)
        return self 

    def __neg__(self):
        """
        Returns a negated vector           
        """
        return Vector3(-self[0], -self[1], -self[2])

    def length(self):
        return sqrt(self[0] * self[0] + self[1] * self[1] + 
                         self[2] * self[2])

    def normalize(self):
        """
        Normalize the vector (retain dir, set length to 1)
        """
        length = self.length()
        if length == 0:
            return
        self[0] /= length
        self[1] /= length
        self[2] /= length

    def unit(self):
        """
        Returns a normalized copy of this vector
        """
        length = self.length()
        if length == 0:
            return self.copy()
        return Vector3(self[0] / length, 
                       self[1] / length, 
                       self[2] / length)
    
    def copy(self):
        """
        Returns a copy of this vector.
        """
        return Vector3(*self)

    def zero(self):
        """
        Sets the vector components to 0.
        """
        self[0] = 0.0
        self[1] = 0.0
        self[2] = 0.0

    def is_shorter_than(self, magnitude):
        """
        Returns true if the magnitude of the vector is shorter 
        than the listed magnitude.
        
        Taking the square root of a number is a slow process 
        (newtons method, right?). To solve that problem, we 
        just square both sides and compare: 
        magnitude^2 > x*x + y*y ...
        """
        # Sum the right hand side of the equation above.
        total = 0.0
        for item in self:
            total += item*item

        # Check the magnitude.
        return magnitude * magnitude > total

