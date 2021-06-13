class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()  # This rabbit is eating a carrot
# The inherited class with same attributes(definitions) as the parent class
# will override the definition from the parent class
