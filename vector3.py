class Vector3(list):
    """ 
    A simple vector.
    """
    def __init__(self, *values):
        """ 
        Construct the vector from the given values.
        """
        for value in values:
            assert(type(value) == float)
            self.append(value)

    def __add__(self, other):
        """ 
        Add one vector to another: result = self + other
        """
        ret = Vector3()
        if type(other) == float:
            for i in self:
                ret.append(i + other)
        else:
            assert(len(other) == len(self))
            for idx, val in enumerate(self):
                ret.append(val + other[idx])
        return ret

    def __iadd__(self, other):
        """ 
        Add one vector to another: self += other
        """
        return self.__add__(other)

    def __sub__(self, other):
        """ 
        Subtract one vector from another: result = self - other
        """
        ret = Vector3()
        if type(other) == float:
            for i in self:
                ret.append(i - other)
        else:
            assert(len(other) == len(self))
            for idx, val in enumerate(self):
                ret.append(val - other[idx])
        return ret

    def __isub__(self, other):
        """ 
        Subtract one vector from another: self -= other
        """
        return self.__sub__(other)

    def __mul__(self, other):
        """
        Scalar multiplication: result = self * val
        """
        ret = Vector3()
        if type(other) == float:
            for i in self:
                ret.append(i * other)
        else:
            for idx, val in enumerate(self):
                ret.append(val * other[idx])
        return ret

    def __imul__(self, other):
        """
        self *= other
        """
        return self.__mul__(other)

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

    def copy(self):
        """
        Returns a copy of this vector.
        """
        return Vector3(*self)

    def isShorterThan(self, magnitude):
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

