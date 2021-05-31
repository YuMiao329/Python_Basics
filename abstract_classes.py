# abstract classes (ghost class)
# ***Underachieved dreams that children must achieve
# prevent a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod


class Vehicle(ABC):  # Put ABC as the argument to make Vehicle class abstract

    @abstractmethod  # specify the method as the fake method
    def go(self):  # This now only have definition but no actual use (fake method)
        # have to create same definitions in child class
        # Not callable
        pass

    @abstractmethod
    def stop(self):  # specify the method as the fake method
        # same as the ghost go method
        # Not callable
        pass


class Car(Vehicle):

    def go(self):  # generated abstract class from the parent class
        #            IF NO THIS CLASS, IT WILL GENERATE ERROR MESSAGE
        print("You drive the car")

    def stop(self):
        #            IF NO THIS CLASS, IT WILL GENERATE ERROR MESSAGE
        print("This car is stopped")


class Motorcycle(Vehicle):

    def go(self):
        #            IF NO THIS CLASS, IT WILL GENERATE ERROR MESSAGE
        print("You ride the motorcycle")

    def stop(self):
        #            IF NO THIS CLASS, IT WILL GENERATE ERROR MESSAGE
        print("This motorcycle is stopped")


# vehicle = Vehicle() #cant have this because go method is
#                      a ghost method which cant be instantiated
car = Car()
motorcycle = Motorcycle()

# vehicle.go()  #cant have this because go method is
#                a ghost method which cant be called
car.go()  # You drive the car
motorcycle.go()  # You ride the motorcycle

car.stop()  # This car is stopped
motorcycle.stop()  # This motorcycle is stopped
