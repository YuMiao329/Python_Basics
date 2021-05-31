# method chaining = calling multiple methods sequentially
#                  each class performs an action on the same object
#                  and returns itself

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

car.turn_on()  # You start the engine
car.drive()  # You drive the car

car.turn_on().drive()  # You start the engine
#                        You drive the car
# if you call a method with no return
# the method will return None
# after adding the return self statement for each method definition
# the first call part will return "car" then adding to the second part as car.drive

car.brake().turn_off()  # You step on the brake
#                         You turn off the engine

car.turn_on().drive().brake().turn_off()  # You start the engine
#                                           You drive the car
#                                           You step on the brake
#                                           You turn off the engine

# adding line continuation character after "\" each method
# make it more readable
car.turn_on() \
    .drive() \
    .brake() \
    .turn_off()
