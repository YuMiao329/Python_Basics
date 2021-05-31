# Multi-level inheritance: A derived (child) class is inherited from
#                          another derived (child) class.

class Organism:

    alive = True

class Animal(Organism): #Inherited from Organism

    def eat(self):
        print("This animal is eating")

class Dog(Animal): #Inherited from Animal

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive) # True
dog.eat() # This animal is eating
dog.bark() # This dog is barking





