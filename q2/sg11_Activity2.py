# 1. 
# a. Duck typing is a concept in Python where an object's type does not matter as long as it has the required methods or behaviors. It focuses on what an object can do rather than what class it belongs to.
# b. The Car class needed to have the same method, move(), that the Dog and Cat classes have. This allows it to perform the required action without inheriting from the Animal class.
# 2.
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)
