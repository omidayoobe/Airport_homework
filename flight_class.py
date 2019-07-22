


#flight class
class Flight():
    # __init__ flight date
    # __init__  flight number
    def __init__(self, origin, destination,date, flight_number):
        self.origin = origin
        self.distination = destination
        self.date = date
        self.flight_number = flight_number
        self.passengers = []

    def add_passen(self, passen):
        if passen not in self.passengers:
            self.passengers.append(passen)

    def print_passen(self):
        for passen in self.passengers:
            print(passen.get_fullname()+ " is flying from "+ self.origin + " to " +  self.distination + " on " + self.date + ". flight number: " + self.flight_number )




