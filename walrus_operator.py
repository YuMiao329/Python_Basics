# walrus operator :=
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expressions

# happy = True
# print(happy)

# Walrus form of upper algorithms
print(happy := True)  # True

#foods = list()
#while True:
#    food = input("what food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

# Walrus form of upper algorithms
foods = list()
while food := input("what food do you like?: ") != "quit":
    foods.append(food)
