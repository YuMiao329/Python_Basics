# zip(*iterables) = aggregate elements from two or more iterables (list,tuples,sets,...)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Code"]
passwords = ("password", "abc123", "guest")

# the type of zip function is zip
users = zip(usernames, passwords)
print(type(users))  # <class 'zip'>

# ----------------------------------------------------------------
# change zip type to list
users_list = list(zip(usernames, passwords))
print(type(users_list))  # <class 'list'>

for i in users_list:
    print(i)
# ('Dude', 'password')
# ('Bro', 'abc123')
# ('Code', 'guest')

# ----------------------------------------------------------------
# change zip type to dict
users_dict = dict(zip(usernames, passwords))
print(type(users_dict))  # <class 'dict'>

for key, value in users_dict.items():
    print(key + " : " + value)
# Dude:password
# Bro:abc123
# Code:guest

# ----------------------------------------------------------------
# you can also zip three list of iterables together by using zip
usernames = ["Dude", "Bro", "Code"]
passwords = ("password", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)
#('Dude', 'password', '1/1/2021')
#('Bro', 'abc123', '1/2/2021')
#('Code', 'guest', '1/3/2021')
