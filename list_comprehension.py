# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional] for filter
#                       list = [expression if/else for item in iterable] for new value return

squares1 = []  # create an  list
for i in range(1, 11):  # create a for loop
    squares1.append(i * i)  # define what each loop iteration should do
print(squares1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares2 = [i * i for i in range(1, 11)]  # list = [expression for item in iterable]
print(squares2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)  # [100, 90, 80, 70, 60]

passed_students2 = [i for i in students if i >= 60]
# list = [expression for item in iterable if conditional]
print(passed_students2)  # [100, 90, 80, 70, 60]

passed_students3 = [i if i >= 60 else "FAILED" for i in students]
# list = [expression if(conditions)/else(result) for item in iterable]
print(passed_students3)  # [100, 90, 80, 70, 60, 'FAILED', 'FAILED', 'FAILED', 'FAILED']
