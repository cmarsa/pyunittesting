# calculate.py


class Calculate:
    def add(self, x, y):
        if self._assert_int_params(x, y):
            return x + y
        else:
            raise TypeError(f'Invalid type: {type(x)} and {type(y)}')

    def subtract(self, x, y):
        if self._assert_int_params(x, y):
            return x - y
        else:
            raise TypeError(f'Invalid type: {type(x)} and {type(y)}')
    
    def multiply(self, x, y):
        if self._assert_int_params(x, y):
            return x * y
        else:
            raise TypeError(f'Invalid type: {type(x)} and {type(y)}')
    
    def divide(self, x, y):
        assert y != 0, 'Zero division Error'
        if self._assert_int_params(x, y):
            return x / y
        else:
            raise TypeError(f'Invalid type: {type(x)} and {type(y)}')
    
    @staticmethod
    def _assert_int_params(x, y):
        return type(x) == int and type(y) == int
    


# if __name__ == '__main__':
#     calc = Calculate()
#     result = calc.add(2, 2)
#     print(result)