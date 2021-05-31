# super() = function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used
#           *GOAL: Pass ARGUMENTS from parent methods to child classes

class Rectangle:

    # pass

    def __init__(self, length, width):  # These method will be used by child classes
        self.width = width  # These method will be used by child classes
        self.length = length  # These method will be used by child classes


class Square(Rectangle):

    def __init__(self, length, width):
        # self.length = length
        # self.width = width
        super().__init__(length, width)  # Use parent __init__ method
        # To get the self.parameters

    def check_length(self):
        print(self.length)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        # self.length = length
        # self.width = width
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())  # 9
print(cube.volume())  # 27

# square = Square(2,3) # Sanity Check
# square.check_length() # Sanity Check
