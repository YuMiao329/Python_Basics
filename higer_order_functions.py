# higher order function = a function that either:
#                         1. accepts a function as an argument
#                            or
#                         2. returns a function
#                         (In Python, functions are also treated as objects)


# examples: accepts a function as an argument
def loud(text):
    return text.upper()


def quite(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)  # HELLO
hello(quite)  # hello


# examples: returns a function
def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)  # assign dividend method to divide variable
#                      then the divide will be a callable function
print(divide(10))  # call the divide function as the form of dividend method
#                  # 5.0
