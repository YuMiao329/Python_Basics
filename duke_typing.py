# Duck typing = concepts where the class of an
#               object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking ")

    def nod(self):
        print("This duck is nodding")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is talking")

    def nod(self):
        print("This chicken is nodding")


class Person():

    def catch(self, duck):
        duck.walk()  # since we only use walk and talk for duke and chicken,
        duck.talk()  # the duck type will not be checked and could be used
        #              for chicken too. They share NECESSARY methods within the catch function.
        print("You caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
#This duck is walking
#This duck is quacking
#You caught the critter

person.catch(chicken)
#This chicken is walking
#This chicken is talking
#You caught the critter
#HERE: class type is not checked if minimum methods/attributes are present
