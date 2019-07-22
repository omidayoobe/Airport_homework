

##### Aircrafts class
class Aircraft():
    # aircroft name
    def __init__(self,aircraft_name, company, colour ):
        self.aircraft_name = aircraft_name
        self.company = company
        self.colour = colour


##### planes sub-class
class Plane(Aircraft):
    # plane company
    # plane colour
    # plane number
    def __init__(self, aircraft_name, company, colour ):
        super().__init__(aircraft_name,company, colour)




##### helicopter sub-class
class Helicopter(Aircraft):
    # helicopter company
    # helicopter colour
    # helicopter number
    def __init__(self,aircraft_name, company,colour):
        super().__init__(aircraft_name, company, colour)


