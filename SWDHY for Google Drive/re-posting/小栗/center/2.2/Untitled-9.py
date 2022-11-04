
class p_ver():
    def __init__(self, ver=None):
        self.ver = [ver]

    def __repr__(self):
        return "p_ver("+str(self.ver[0])+")"

    def __str__(self):
        return str(self.ver[0])
    
    def __int__(self):
        return int(self.ver[0])

    def __float__(self):
        return float(self.ver[0])

    def __neg__(self):
        return -self.ver[0]

    def __pos__(self):
        return self.ver[0]

    def __abs__(self):
        return abs(self.ver[0])

    def __invert__(self):
        return ~self.ver[0]

    def __round__(self):
        return round(self.ver[0])

    def __round__(self, n=None):
        if not n:
            return round(self.ver[0])
        else:
            return round(self.ver[0], n)

    def __ceil__(self):
        return ceil(self.ver[0])

    def __floor__(self):
        return floor(self.ver[0])

    def __trunc__(self):
        return trunc(self.ver[0])

    def __add__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return float(self.ver[0])+y
        elif isinstance(y, p_ver):
            return self.ver[0]+y.ver[0]

    def __radd__(self, y):
        return self.__add__(y)

    def __sub__(self, y):
        return self.__add__(-y)

    def __rsub__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return -float(self.ver[0])+y
        elif isinstance(y, p_ver):
           return -self.ver[0]+y.ver[0]

    def __mul__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return float(self.ver[0])*y
        elif isinstance(y, p_ver):
           return self.ver[0]*y.ver[0]
    
    def __rmul__(self, y):
        return self.__mul__(y)

    def __truediv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return float(self.ver[0])/y
        elif isinstance(y, p_ver):
           return self.ver[0]/y.ver[0]
    
    def __rtruediv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return y/float(self.ver[0])
        elif isinstance(y, p_ver):
           return y.ver[0]/self.ver[0]

    def __floordiv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return float(self.ver[0])//y
        elif isinstance(y, p_ver):
           return self.ver[0]//y.ver[0]
    
    def __rfloordiv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return y//float(self.ver[0])
        elif isinstance(y, p_ver):
           return y.ver[0]//self.ver[0]

    def __mod__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return float(self.ver[0])%y
        elif isinstance(y, p_ver):
           return self.ver[0]%y.ver[0]
    
    def __rmod__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return y%float(self.ver[0])
        elif isinstance(y, p_ver):
           return y.ver[0]%self.ver[0]

    def __pow__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return float(self.ver[0])**y
        elif isinstance(y, p_ver):
           return self.ver[0]**y.ver[0]

    def __rpow__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return y**float(self.ver[0])
        elif isinstance(y, p_ver):
           return y.ver[0]**self.ver[0]

    def __lshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])<<y
            elif isinstance(y, p_ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]<<y.ver[0]
        raise Exception(f"TypeError: unsupported operand type(s) for <<: {type(self)} and {type(y)}")

    def __rlshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return y<<int(self.ver[0])
            elif isinstance(y, p_ver):
                if isinstance(y.ver[0], int):
                    return y.ver[0]<<self.ver[0]
        raise Exception(f"TypeError: unsupported operand type(s) for <<: {type(y)} and {type(self)}")

    def __rshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])>>y
            elif isinstance(y, p_ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]>>y.ver[0]
        raise Exception(f"TypeError: unsupported operand type(s) for >> {type(self)} and {type(y)}")

    def __rrshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])>>y
            elif isinstance(y, p_ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]>>y.ver[0]
        raise Exception(f"TypeError: unsupported operand type(s) for >> {type(y)} and {type(self)}")

    def __and__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])&y
            elif isinstance(y, p_ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]&y.ver[0]
        raise Exception(f"TypeError: unsupported operand type(s) for & {type(y)} and {type(self)}")

    def __rand__(self, y):
        return self.__and__(y)

    def __xor__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])^y
            elif isinstance(y, p_ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]^y.ver[0]
        raise Exception(f"TypeError: unsupported operand type(s) for ^ {type(y)} and {type(self)}")

    def __rxor__(self, y):
        return self.__xor__(y)
    
    def __or__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])|y
            elif isinstance(y, p_ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]|y.ver[0]
        raise Exception(f"TypeError: unsupported operand type(s) for | {type(y)} and {type(self)}")

    def __ror__(self, y):
        return self.__or__(y)

p = p_ver([1, 2])
print(p[0])
