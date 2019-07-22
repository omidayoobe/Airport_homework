

######## big class peoples
class People():

    # def __init__ name, age
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


        # fullname method
    def get_fullname(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.first_name + "." + self.last_name + "@yahoo.com"

####### sub-class staff
class Staff(People):

    # def __init__ ID, department
    def __init__(self, first_name,last_name, age, id, department):
        super().__init__(first_name, last_name, age)
        self.id = id
        self.deparment = department




####### sub-class passengers
class Passenger(People):

    # def __init__ passport
    def __init__(self, first_name, last_name, age, passport):
        super().__init__(first_name, last_name, age)
        self.passport = passport







