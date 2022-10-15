class Note:
    def __init__(self, name, ton=0):
        if name not in ["до", "ре", "ми", "фа", "соль", "ля", "си"]:
            raise ValueError('недопустимое значение аргумента')
        self._name = name
        if ton not in [-1, 0, 1]:
            raise ValueError('недопустимое значение аргумента')
        self._ton = ton

    def __setattr__(self, name, value):
        if self.verify_name(name):
            if not value in [-1, 0, 1]:
                raise ValueError('недопустимое значение аргумента')
            object.__setattr__(self, name, value)
        else :
            if value not in  ["до", "ре", "ми", "фа", "соль", "ля", "си"]:
                raise ValueError('недопустимое значение аргумента')
            object.__setattr__(self, name, value)

    def verify_name(self, name):
        if name == "_ton":
            return True


class Notes:
    __in = None
    def __new__(cls, *args, **kwargs):
        if cls.__in == None:  # то есть ЭК ещё ни разу не создавался !
            cls.__in = super().__new__(cls)  # Наследование от базового класса Object,  super().__new__(cls)
        return cls.__in

    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si',)
    slots_dict = {'_do':"до", '_re':"ре", '_mi':"ми", '_fa':"фа", '_solt':"соль", '_la':"ля", '_si':"си"}

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __getitem__(self, item):
        if not isinstance(item, int) or item not in [0, 1, 2, 3, 4, 5, 6]:
            raise IndexError('недопустимый индекс')
        name_note = self.__slots__[item]
        return getattr(self, name_note)

fa = Notes()
notes = Notes()
print(fa[1])
print(notes[1]._name)
notes[3]._ton = -1
print(notes[3].__dict__)
print("put -1-----", notes[3]._ton)
