# sort() method = used in lists
# sort() function = used in iterables

students = ["Squidward", "Sandy", "Partric", "Spongebob", "Mr.Krabs"]

# cant sort tuple: (something)
# To sort students in alphabetical order
students.sort()
# could use arguments: reverse=True

students_tuple = ("Squidward", "Sandy", "Partric", "Spongebob", "Mr.Krabs")
# this can be used for tuple
sorted_students = sorted(students_tuple)
# could use arguments: reverse=True

for i in students:
    print(i)
#Mr.Krabs
#Partric
#Sandy
#Spongebob
#Squidward
for i in sorted_students:
    print(i)
#Mr.Krabs
#Partric
#Sandy
#Spongebob
#Squidward
#---------------------------------------------------------------------------

#iterables with tuple:
#use .sort method
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

students.sort()

for i in students:
    print(i)
#('Mr.Krabs', 'C', 78)
#('Patrick', 'D', 36)
#('Sandy', 'A', 33)
#('Spongebob', 'B', 20)
#('Squidward', 'F', 60)

#Sort by the second column!
grades = lambda grades:grades[1]
students.sort(key=grades)
#can also reverse it at the same time
#students.sort(key=grades, reverse=True)

#If want to change the 3rd column:
#ages = lambda ages:ages[2]
#students.sort(key=ages)


for i in students:
    print(i)
#('Sandy', 'A', 33)
#('Spongebob', 'B', 20)
#('Mr.Krabs', 'C', 78)
#('Patrick', 'D', 36)
#('Squidward', 'F', 60)

#-----------------------------------------------------------------

#tuple with tuple:
#use sorted function
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

sorted_tuple_students = sorted(students, key=grades)

for i in sorted_tuple_students:
    print(i)
#('Sandy', 'A', 33)
#('Spongebob', 'B', 20)
#('Mr.Krabs', 'C', 78)
#('Patrick', 'D', 36)
#('Squidward', 'F', 60)
