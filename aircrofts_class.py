

##### Aircrafts class
class Aircrafts():
    # aircroft name
    def __init__(self,aircraft_name):
        self.aircraft_name = aircraft_name


##### planes sub-class
class Planes(Aircrafts):
    # plane company
    # plane colour
    # plane number
    def __init__(self, aircraft_name, company, colour, number):
        self.company = company
        self.colour = colour
        self. number = number
        super().__init__(aircraft_name)

    # ticket number
    def tickets(self, ticketsNO):
        self.ticketsNO = ticketsNO


##### helicopter sub-class
class Helicopter(Aircrafts):
    # helicopter company
    # helicopter colour
    # helicopter number
    def __init__(self,aircraft_name, company,colour, number):
        self.company = company
        self.colour = colour
        self.number = number
        super().__init__(aircraft_name)
