# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think this as a shortcut)
#                   (useful if need for a short period of time, throw-away)
#
# lambda parameters:expression
# This is just like a function handle in matlab

def double(x):
    return x * 2


print(double(5))

# plan to use these functions once and then throw them away:
double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))  # 10
print(multiply(5, 6))  # 30
print(add(5, 6, 7))  # 18
print(full_name("Bro", "Code"))  # Bro Code
print(age_check(20))  # True
