class MultiplicationObject(object) :
    def __init__(self, a, b, c) :
        self._a = a 
        self._b = b 
        self._c = c 
    
    def multiplication(self) :
        return self._a*self._b*self._c

    @property
    def a(self) :
        return self._a

    @property
    def b(self) :
        return self._b

    @property
    def c(self) :
        return self._c

    @a.setter
    def a(self, a) :
        self._a = a

    @b.setter
    def b(self, b) :
        self._b = b

    @c.setter
    def c(self, c) :
        self._c = c


if __name__ == '__main__' : #main program
    obj = MultiplicationObject(1, 2, 3)
    result = obj.multiplication()
    print(result)

    obj = MultiplicationObject(5, 6, 7)
    result = obj.multiplication()
    print(result)