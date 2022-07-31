class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    @classmethod
    def details(cls,name, birth_year):
        cls.name = name
        cls.birth_year = year
        if cls.birth_year < 2002:
            return False
        else:
            return True
    def check_age(self):
        if self.age < 19:
            return False
        else:
            return True

person1 = Person('나웅기', 27)
print(person1.check_age())