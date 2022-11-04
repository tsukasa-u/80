import math

class P_Ver():
    def __init__(self, ver=None):
        self.ver = [ver]

    def __new__(cls, ver=None):
        return  super().__new__(cls)

    def __repr__(self):
        return "P_Ver("+str(self.ver[0])+")"

    def __dir__(self):
        return self

    def __len__(self):
        if isinstance(self.ver[0], list) or isinstance(self.ver[0], tuple) or isinstance(self.ver[0], set):
            return len(self.ver[0])
        raise TypeError(f"object of type {type(self)} has no len()")

    def __contains__(self, y):
        if isinstance(y, P_Ver):
            return y.ver[0] in self.ver[0]
        else:
            return y in self.ver[0]

    def __getitem__(self, key):
        if isinstance(self.ver[0], list) or isinstance(self.ver[0], tuple) or isinstance(self.ver[0], set):
            return self.ver[0][key]
        else:
            raise TypeError(f"{type(self)} object is not subscriptable")

    def __setitem__(self, key, val):
        if isinstance(self.ver[0], list) or isinstance(self.ver[0], tuple) or isinstance(self.ver[0], set):
            self.ver[0][key] = val
        else:
            raise TypeError(f"{type(self)} object is not subscriptable")

    def __delitem__(self, key):
        if isinstance(self.ver[0], dict) or isinstance(self.ver[0], list):
            del self.ver[0][key]
        raise AttributeError(f"{type(self.ver[0])} object has no attribute 'del'")

    def __missing__(self, key):
        if isinstance(self.ver[0], dict):
            return None
        raise AttributeError(f"{type(self.ver[0])} object has no attribute '__missing__'")

    def __str__(self):
        if isinstance(self.ver[0], str):
            return str(self.ver[0])
        raise TypeError(f"unsupported operand type(s) for str: {type(self.ver[0])}")
    
    def __int__(self):
        if isinstance(self.ver[0], int):
            return int(self.ver[0])
        raise TypeError(f"unsupported operand type(s) for int: {type(self.ver[0])}")

    def __float__(self):
        if isinstance(self.ver[0], float):
            return float(self.ver[0])
        raise TypeError(f"unsupported operand type(s) for float: {type(self.ver[0])}")

    def __neg__(self):
        if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
            return -1*self.ver[0]
        raise TypeError(f"unsupported operand type(s) for -: {type(self.ver[0])}")

    def __pos__(self):
        if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
            return self.ver[0]
        raise TypeError(f"unsupported operand type(s) for +: {type(self.ver[0])}")

    def __abs__(self):
        if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
            return abs(self.ver[0])
        raise TypeError(f"unsupported operand type(s) for abs: {type(self.ver[0])}")

    def __invert__(self):
        if isinstance(self.ver[0], int):
            return ~self.ver[0]
        raise TypeError(f"unsupported operand type(s) for ~: {type(self.ver[0])}")

    def __round__(self, n=None):
        if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
            if not n:
                return round(self.ver[0])
            else:
                return round(self.ver[0], n)
        raise TypeError(f"unsupported operand type(s) for round: {type(self.ver[0])}")

    def __ceil__(self):
        return math.ceil(self.ver[0])

    def __floor__(self):
        return math.floor(self.ver[0])

    def __trunc__(self):
        return math.trunc(self.ver[0])

    def __add__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return self.ver[0]+y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return self.ver[0]+y.ver[0]
            elif isinstance(y.ver[0], list) and isinstance(self.ver[0], list):
                return self.ver[0]+y.ver[0]
            elif isinstance(y.ver[0], str) and isinstance(self.ver[0], str):
                return self.ver[0]+y.ver[0]
        elif isinstance(y, str) and isinstance(self.ver[0], str):
            return self.ver[0]+y
        raise TypeError(f"unsupported operand type(s) for +: {type(self.ver[0])} and {type(y)}")

    def __concat__(self, y):
        if isinstance(y, list) and isinstance(self.ver[0], list):
            return self.ver[0]+y
        elif isinstance(y, tuple) and isinstance(self.ver[0], tuple):
            return self.ver[0]+y

    def __radd__(self, y):
        return self.__add__(y)

    def countOf(self, y):
        count = 0
        for i in self.ver[0]:
            if i==y:
                count += 1
        return count

    def indexOf(self, y):
        for count, i in enumerate(self.ver[0]):
            if i==y:
                return count

    def __sub__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return self.ver[0]-y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return self.ver[0]-y.ver[0]
        raise TypeError(f"unsupported operand type(s) for -: {type(self.ver[0])} and {type(y)}")

    def __rsub__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return -1*self.ver[0]+y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return -1*self.ver[0]+y.ver[0]
        raise TypeError(f"unsupported operand type(s) for -: {type(self.ver[0])} and {type(y)}")

    def __mul__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return self.ver[0]*y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return self.ver[0]*y.ver[0]
        raise TypeError(f"unsupported operand type(s) for *: {type(self.ver[0])} and {type(y)}")
    
    def __rmul__(self, y):
        return self.__mul__(y)

    def __truediv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return self.ver[0]/y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return self.ver[0]/y.ver[0]
        raise TypeError(f"unsupported operand type(s) for /: {type(self.ver[0])} and {type(y)}")
    
    def __rtruediv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return y/self.ver[0]
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return y.ver[0]/self.ver[0]
        raise TypeError(f"unsupported operand type(s) for /: {type(self.ver[0])} and {type(y)}")

    def __floordiv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return self.ver[0]//y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return self.ver[0]//y.ver[0]
        raise TypeError(f"unsupported operand type(s) for //: {type(self.ver[0])} and {type(y)}")
    
    def __rfloordiv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return y//self.ver[0]
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return y.ver[0]//self.ver[0]
        raise TypeError(f"unsupported operand type(s) for //: {type(self.ver[0])} and {type(y)}")

    def __mod__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return self.ver[0]%y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return self.ver[0]%y.ver[0]
        raise TypeError(f"unsupported operand type(s) for %: {type(self.ver[0])} and {type(y)}")
    
    def __rmod__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return y%self.ver[0]
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return y.ver[0]%self.ver[0]
        raise TypeError(f"unsupported operand type(s) for %: {type(self.ver[0])} and {type(y)}")

    def __pow__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return self.ver[0]**y
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return self.ver[0]**y.ver[0]
        raise TypeError(f"unsupported operand type(s) for **: {type(self.ver[0])} and {type(y)}")

    def __rpow__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                return y**self.ver[0]
        elif isinstance(y, P_Ver):
            if isinstance(y.ver[0], int) or isinstance(y.ver[0], float):
                if isinstance(self.ver[0], int) or isinstance(self.ver[0], float):
                    return y.ver[0]**self.ver[0]
        raise TypeError(f"unsupported operand type(s) for <<: {type(self.ver[0])} and {type(y)}")

    def __lshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])<<y
            elif isinstance(y, P_Ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]<<y.ver[0]
        raise TypeError(f"unsupported operand type(s) for <<: {type(self.ver[0])} and {type(y)}")

    def __rlshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return y<<int(self.ver[0])
            elif isinstance(y, P_Ver):
                if isinstance(y.ver[0], int):
                    return y.ver[0]<<self.ver[0]
        raise TypeError(f"unsupported operand type(s) for <<: {type(y)} and {type(self.ver[0])}")

    def __rshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])>>y
            elif isinstance(y, P_Ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]>>y.ver[0]
        raise TypeError(f"unsupported operand type(s) for >> {type(self.ver[0])} and {type(y)}")

    def __rrshift__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])>>y
            elif isinstance(y, P_Ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]>>y.ver[0]
        raise TypeError(f"unsupported operand type(s) for >> {type(y)} and {type(self.ver[0])}")

    def __and__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])&y
            elif isinstance(y, P_Ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]&y.ver[0]
        raise TypeError(f"unsupported operand type(s) for & {type(y)} and {type(self.ver[0])}")

    def __rand__(self, y):
        return self.__and__(y)

    def __xor__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])^y
            elif isinstance(y, P_Ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]^y.ver[0]
        raise TypeError(f"unsupported operand type(s) for ^ {type(y)} and {type(self.ver[0])}")

    def __rxor__(self, y):
        return self.__xor__(y)
    
    def __or__(self, y):
        if isinstance(self.ver[0], int):
            if isinstance(y, int):
                return int(self.ver[0])|y
            elif isinstance(y, P_Ver):
                if isinstance(y.ver[0], int):
                    return self.ver[0]|y.ver[0]
        raise TypeError(f"unsupported operand type(s) for | {type(y)} and {type(self.ver[0])}")

    def __ror__(self, y):
        return self.__or__(y)

    def __eq__(self, y):
        return self.ver[0]==y

    def __ne__(self, y):
        return self.ver[0]!=y

    def __lt__(self, y):
        return self.ver[0]<y

    def __le__(self, y):
        return self.ver[0]<=y

    def __gt__(self, y):
        return self.ver[0]>y

    def __ge__(self, y):
        return self.ver[0]>=y

    def __bool__(self):
        return bool(self.ver[0])

    def __copy__(self):
        return self

    def append(self, y):
        if isinstance(self.ver[0], list):
            self.ver[0].append(y)
        else:
            raise AttributeError(f"{type(self.ver[0])} object has no attribute 'append'")
        return self

    def pop(self):
        if isinstance(self.ver[0], list):
            return self.ver[0].pop()
        else:
            raise AttributeError(f"{type(self.ver[0])} object has no attribute 'pop'")

a = P_Ver("1")
b = P_Ver("2")
print(a+"2")