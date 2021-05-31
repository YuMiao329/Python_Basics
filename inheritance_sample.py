class Animal:

    alive = True # begin an animal alive

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive) #True
fish.eat() #This animal is eating
hawk.sleep() #This animal is sleeping

rabbit.run() #This rabbit is running
fish.swim() #This fish is swimming
hawk.fly() #This hawk is flying






