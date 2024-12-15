class person():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(person, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person('Tom', 20)
p2 = person('Jerry', 30)
print(p1.name, p1.age)
print(p2.name, p2.age)