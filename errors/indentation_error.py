class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def double_age(self):
        return self.age * 2

# Square object #1
person1 = Person('Peter',18)
print(person1.name + " double age is "+ str(person1.double_age()))


