# multiple inheritance = a child class is derived from
#                        more than one parent class.

class Prey:  # Parent 1

    def flee(self):
        print("This animal flees")


class Predator:  # Parent 2

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):  # Inherited from borh parent 1 and parent 2
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()  # This animal flees
hawk.hunt()  # This animal is hunting
fish.hunt()  # This animal is hunting
fish.flee()  # This animal flees
