class Star:
    __slots__ = ("_name","_massa", "_temp")

    def __init__(self, name, massa, temp):
        self._name, self._massa, self._temp =  name, massa, temp

class WhiteDwarf(Star):
    __slots__ = ("_type_star", "_radius",)

    def __init__(self,name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star, self._radius = type_star, radius

class YellowDwarf(Star):
    __slots__ = ("_type_star", "_radius",)

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star, self._radius = type_star, radius

class RedGiant(Star):
    __slots__ = ("_type_star", "_radius",)

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star, self._radius = type_star, radius

class Pulsar(Star):
    __slots__ = ("_type_star", "_radius",)

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star, self._radius = type_star, radius

stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))
print(len(white_dwarfs))
