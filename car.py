class Car:
#Defined object car factory (also called blueprint): Car.
    def __init__(self, make, model, year, color):
        #define attributes - what the object is/has
        self.make = make #This shows how to assign functions/orders for the function call
        self.model = model
        self.year = year
        self.color = color

    #define methods - what the object can do
    def drive(self):
        print("This " + self.model+" is driving")

    def stop(self):
        print("This " + self.model+" is stopping")