import messages

print('lol')
name = 'sss'
print(name.count('s'))
x = 1
y = 3.2
z = '3'
print(type(x))
zz = float(x) + int(y) + float(z)
print(zz)
# name = input('what is your name?:')
# print('my name is ' + name)
# [start(inclusive):stop(exclusive):step]

# slicing
website1 = 'http://google.com'
website2 = 'http://wikipedia.com'
slicer = slice(7, -4)
print(website1[slicer])
print(website2[slicer])

# nested loops
for i in range(5):
    for j in range(6):
        print('*', end='')
    print()

# break continue pass
phone_number = '123-456-7890'
for i in phone_number:
    if i == '-':
        continue
    print(i, end='')
print()

for i in range(1, 31):
    if i == 13:
        pass
    else:
        print(i, end='')
print()

phone_number = '123-456-7890'
for i in phone_number:
    if i == '-':
        pass
    else:
        print(i, end='')

# lists
food = ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'pudding']
food[0] = 'sushi'
food.append('ice_cream')
food.remove('hotdog')
food.pop()
food.insert(0, 'cake')
for x in food:
    print(x)
print()

food.sort()
for x in food:
    print(x)
print()

# 2d lists
drinks = ['coffee', 'soda']
dinner = ['pizza', 'hamburger']
dessert = ['cake', 'icecream']

food = [drinks, dinner, dessert]

print(food[0])  # ['coffee','coda']
print(food[0][0])  # coffee

# tuple = collection which is ordered and unchangeable
#        used to group together related data

student = ('bro', 21, 'male')
print(student.count('bro'))  # 1
print(student.index('male'))  # 2

for x in student:
    print(x)

if 'bro' in student:
    print('bro is here')

# set = collection which is unordered, unindexed, NO duplicated values

utensils = {'fork', 'spoon', 'knife', 'knife', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}
# utensils.add('napkin')   utensils={'fork','spoon','knife','knife','knife','napkin'}
# utensils.remove('fork')
# utensils.clear() #clear all
for x in utensils:
    print(x)  # spoon knife fork

utensils.update(dishes)  # add all dishes to the utensil set
dinner_table = utensils.union(dishes)  # elements from both sets
print(utensils.difference(dishes))  # print all utensils have but not dishes
# will be fork and spoon
print(utensils.intersection(dishes))  # print all common things in both sets
# will be only knife

# dictionary

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}
print(capitals['Russia'])  # Moscow
# print(capitals['Germany']) #Error Message
print(capitals.get('Russia'))  # Moscow
print(capitals.get('Germany'))  # None
print(capitals.keys())  # dict_keys(['USA', 'India', 'China', 'Russia'])
print(capitals.values())  # dict_values(
# ['Washington DC', 'New Dehli', 'Beijing', 'Moscow'])
print(capitals.items())  # dict_items([('USA', 'Washington DC'),
# ('India', 'New Dehli'), ('China', 'Beijing'),
# ('Russia', 'Moscow')])

for key, value in capitals.items():
    print(key, value)

# USA Washington DC
# India New Dehli
# China Beijing
# Russia Moscow
capitals.update({'Germany': 'Berlin'})
for key, value in capitals.items():
    print(key, value)
# USA Washington DC
# India New Dehli
# China Beijing
# Russia Moscow
# Germany Berlin
capitals.update({'USA': 'Las Vegas'})
for key, value in capitals.items():
    print(key, value)
# USA Las Vegas
# India New Dehli
# China Beijing
# Russia Moscow
# Germany Berlin

# capitals.pop('China') #remove China from the dictionary
# capitals.clear #remove all things from the dictionary

# Indexing Operator []
name = 'bro code'
if name[0].islower():
    name = name.capitalize()
print(name)  # Bro code

first_name = name[:3].upper()
last_name = name[4:].lower()
print(first_name)  # BRO
print(last_name)  # code
name = 'bro code!'
last_character = name[-1]
print(last_character)  # !


# Function
def hello(first, last, age):
    print('Hello ' + first + ' ' + last)
    print('You are ' + str(age) + ' years old')
    print('have a nice day!')


hello('bro', 'code', 21)


# Return Statement
def multiply(num1, num2):
    return num1 * num2


x = multiply(6, 8)
print(x)  # 48


# Keyword arguments (python knows the keyword)
def hello2(first, middle, last):
    print('hello ' + first + ' ' + middle + ' ' + last)


hello2(last='code', middle='dude', first='bro')

# Nested function calls
num = input('Enter a whole positive number: ')
num = float(num)
num = abs(num)
num = round(num)
print(num)
# can be changed as below
print(round(abs(float(input('Enter a whole positive number: ')))))

# Variable Scope
name_2 = 'bro'  # the global variable


def display_name():
    name_2 = 'code'  # this name is local, which is only available inside of function
    print(name_2)


##python will follow the order: local, enclosing, global and Built-in (LEGB) rule for function variables
display_name()  # code
print(name_2)  # bro


# Args = parameter that will pack all arguments into a tuple

def addthing(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1


print(addthing(1, 2, 3, 4, 5, 6))  # 21


def addthing2(*stuff):
    sum_2 = 0
    stuff = list(stuff)  # we do this because argument is tuple, which cant be changed
    stuff[0] = 0
    for i in stuff:
        sum_2 += i
    return sum_2


print(addthing2(1, 2, 3, 4, 5, 6))  # 20


# **kwargs = parameters that will pack all arguments into a dictionary

def hello3(**kwargs):
    print('hello ' + kwargs['first'] + ' ' + kwargs['last'])  # hello Bro code


hello3(first='Bro', middle='dude', last='code')


def hello3(**kwargs):
    print('hello', end=' ')
    for keys, values in kwargs.items():
        print(values, end=' ')


hello3(first='Bro', middle='dude', last='code')  # hello Bro dude code
print()
hello3(title='Mr', first='Bro', middle='dude', last='code')  # hello Mr Bro dude code

# str.format() = optional to display more control displaying output
# {} is the place holder of the inserted variable
animal = 'cow'
item = 'moon'

print('The ' + animal + ' jumped over the ' + item)  # The cow jumped over the moon
print('The {} jumped over the {}'.format('cow', 'moon'))  # The cow jumped over the moon
print('The {} jumped over the {}'.format(animal, item))  # The cow jumped over the moon
# the format()'s sequence is important which means the positional argument
print('The {1} jumped over the {0}'.format(animal, item))  # The moon jumped over the cow
# we can also use key word argument
print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))  # The cow jumped over the moon
print('The {item} jumped over the {animal}'.format(animal='cow', item='moon'))  # The moon jumped over the cow
# variable(both positional arguments and key word arguments) could be used multiple times

text = 'the {} jumped over the {}'
print(text.format(animal, item))  # the cow jumped over the moon

name3 = 'bro'  # hello, my name is bro
print('hello, my name is {}'.format(name3))
print('hello, my name is {:10}. Nice to meet you'.format(name3))  # hello, my name is bro       . Nice to meet you
# this will assign ten spaces(space if none) to the blank
print('hello, my name is {:>10}. Nice to meet you'.format(name3))  # hello, my name is        bro. Nice to meet you
# this will align the inserted thing to the right
print('hello, my name is {:^10}. Nice to meet you'.format(name3))  # hello, my name is    bro    . Nice to meet you
# this will align the inserted thing to the middle
print('hello, my name is {name:10}. Nice to meet you'.format(name='bro'))
# if need to insert key word argument, just put the key word in front of the :

number1 = 3.14159
print('the number pi is {:.2f}'.format(number1))  # display the first two digits after the descimal
# the number pi is 3.14
number2 = 10000000000
print('the number pi is {:,}'.format(number2))  # display comma inserted form for each 1000 multiplers
# the number pi is 10,000,000,000#the number pi is 10,000,000,000
print('the number pi is {:b}'.format(number2))  # display the binary form of input number
# the number pi is 1001010100000010111110010000000000
print('the number pi is {:o}'.format(number2))  # display the octal form of unput number
# the number pi is 112402762000
print('the number pi is {:X}'.format(number2))  # the number pi is 2540BE400
print('the number pi is {:x}'.format(number2))  # the number pi is 2540be400
print('the number pi is {:e}'.format(number2))  # display the scientific-notation of input number
# the number pi is 1.000000e+10
print('the number pi is {:E}'.format(number2))
# the number pi is 1.000000E+10

# random number

import random

x = random.randint(1, 6)
print(x)  # generate a random integer from 1 to 6
y = random.random()
print(y)  # generate a random number from 0 to 1

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)  # generate a random thing from myList

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k']
random.shuffle(cards)
print(cards)  # will shuffle the cards into random order

# exception handling =events detected during executuion that will interrupt the flow of program

try:
    numerator = int(input('enter a number to divide: '))
    denominator = int(input('enter a number to divide by: '))
    result = numerator / denominator
    # print(result)
except ZeroDivisionError as e:  # add as e at the end to also print out the error msg
    print(e)  # add as e at the end to also print out the error msg
    print("You can't divide by zero!")
except ValueError as e:
    print(e)  # add as e at the end to also print out the error msg
    print('Enter only numbers PLZ')
except Exception as e:
    print(e)  # add as e at the end to also print out the error msg
    print('something wen wrong :(')  # if enter denominator as 0 or somthing could cause error message
# better to put except exception at the end so that sub exception could be generated
else:
    print(result)  # print the result, only if there is no error appears
finally:
    print('this will always execute')  # This finally part will always execute no matter what happens

# File Detection

import os

path = "C:\\Users\\yum\\Desktop\\text.txt"  # the doulble \ means i could enter os folders (escape)

if os.path.exists(path):
    print('That location exists!')
    if os.path.isfile(path):
        print('That is a file!')
    elif os.path.isdir(path):
        print('That is a directory')
else:
    print('That location does not exist')

# Read a file

text_path = "C:\\Users\\yum\\Desktop\\text.txt"
# if the file is in the same folder of the code, then dont need directions before the file name
with open(text_path) as file:
    # will automatically close the file after opening the file
    # cant catch exception errors
    print(file.read())
print(file.closed)

try:
    with open(text_path) as file:
        # will automatically close the file after opening the file
        # cant catch exception errors
        print(file.read())
except FileNotFoundError:
    print('That file was not found :(')

# Write files (overwrite and append)

new_text = 'YOOOOOOO \n this is new text \n have a good one! \n'
append_text = 'yay!appended!\n'
text_path = "C:\\Users\\yum\\Desktop\\text.txt"
with open(text_path, 'w') as file:  # here 'w' means write the file (overwrite)
    file.write(new_text)
with open(text_path, 'a') as file:  # here 'a' means append the file
    file.write(append_text)

# Copy files
# copyfile() = copies contents of a file
# copy() = copyfile() +permission mode + destination can be a directory
# copy2() = copy() + copies matadata (file's creation and modification times)

import shutil

text_path = "C:\\Users\\yum\\Desktop\\text.txt"
shutil.copyfile(text_path, 'test.txt')  # src, dst
# if no such file, it will create one with copied content
# if there is such file with name specified, the content will be overwritten
# copy() and copy2() both use the same format as the copyfile
# shutil.copy(text_path,'test.txt')
# shutil.copy2(text_path,'test.txt')

# Move a file

import os
import shutil

source = 'py_to_exe.py'
destination = 'D:\\Python_Basics\\py_to_exe\\py_to_exe.py'

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        shutil.move(source, destination)
        print(source + 'Moved!')
except FileNotFoundError:
    print(source + 'was not found')

# Delete a file

import os

path = 'deleteme'

try:
    # os.remove(path) #remove the file
    # os.rmdir(path) #remove the folder #could not delete folder with sub-file or folders
    shutil.rmtree(path)  # could delete folders with contained things
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('You do not have permission to delete that')
except OSError:
    print('You can not delete that using this function')  # could not delete folder with sub-file or folders
else:
    print(path + ' was deleted')

# Modules

import messages as msg  # created *.py file with various functions

messages.hello()  # access hello() functions from messages
messages.bye()
msg.hello()  # access hello() functions from messages
msg.bye()

from messages import hello, bye  # import specific functions from the module messages

hello()
bye()

from messages import *  # import all functions from module messages

# not recommend because it could have conflict with multiple modules existed
hello()
bye()

help('modules')  # search useful modules that are built-ins
