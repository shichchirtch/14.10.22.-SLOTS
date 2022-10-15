class FloatValidator:
    def __init__(self, min_value, max_value):
        if not isinstance(min_value, (int,float)) or not isinstance(max_value, (int, float)):
            raise AttributeError
        self.min_value, self.max_value = min_value, max_value

    def __call__(self, value, *args, **kwargs):
        if not isinstance(value, float) or value < self.min_value or value > self.max_value:
            raise ValueError('значение не прошло валидацию')
        return value

class IntegerValidator:
    def __init__(self, min_value, max_value):
        if not isinstance(min_value, (int,float)) or not isinstance(max_value, (int, float)):
            raise AttributeError
        self.min_value, self.max_value = min_value, max_value

    def __call__(self, value, *args, **kwargs):
        if not isinstance(value, int) or value < self.min_value or value > self.max_value:
            raise ValueError('значение не прошло валидацию')
        if str(value) == "True":
            raise ValueError('значение не прошло валидацию')
        return value
arr = []
def is_valid(lst, validators):
    for x in lst:
        try:
            arr.append(validators[0](x))
        except:
            try:
                arr.append(validators[1](x))
            except:
                pass
    return arr


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])
print(lst_out)



# d = FloatValidator(1, 10)
# print(d("ff"))
