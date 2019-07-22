from peoples_class import *
from aircrofts_class import *
from flight_class import *

########################################################################################################################
# people
passen_1 = Passenger("Adam", "johnson","25","british")
passen_2 = Passenger("danny", "shearman","20","british")
# print("number of passenger are = ", Passengers.num_of_passengers)
# print(passen_1.fullname())
# print(passen_1.email())
# print(passen_2.fullname())
# print(passen_2.email())
# print("")
###################
# staff
staff1 = Staff("jammy", "danielson", "20", "2201", "check-in Assistant")
# print("passengers on board: ")
# staff1.add_passen(passen_1)
# staff1.add_passen(passen_2)
# staff1.print_passen()
#
#
# print(" \n")
# print("staff details ")
# print(staff1.fullname())
# print(staff1.email())

#######################################################################################################################
# Aricrafts
boeing = Plane("Boeing-737","Emirates","white")
atlas = Helicopter("Atlas Oryx", "Emirates", "black")

########################################################################################################################
# Flights
flight1 = Flight("London","ireland", "2019/08/15", "BA7098")
flight2 = Flight("ireland","london", "2019/10/15", "BA7088")

flight1.add_passen(passen_1)
flight2.add_passen(passen_2)
flight1.print_passen()
flight2.print_passen()

