

######## big class peoples
class People():
    # def __init__ name, age
    def __init__(self, name, age):
        self.name = name
        self.age = age


####### sub-class staff
class Staff(People):
    # def __init__ ID, department
    def __init__(self, name, age, id, department):
        super().__init__(name, age)
        self.id = id
        self.deparment = department



####### sub-class passengers
class Passengers(People):
    # def __init__ passport
    def __init__(self, name, age, passport):
        super().__init__(name, age)
        self.passport = passport

    # details method
    def details(self):
        return "he is a good guy"

    # details method
    def mood(self):
        return"happy"


