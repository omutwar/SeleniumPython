"""
    1. Basic function
    2. Function with parameters
    3. Return values
    4. Default parameters
    5. DocStrings
    6. Variable scope
    7. Recursion
    8. Lambda Functions
    9. Function Decorators
    10. Advanced Functions
"""


# 1. Basic functions


def my_function():
    print("Hello, Python!")


my_function()


# 2. Function with parameters


def greet(name):
    print(f'Hello, {name.capitalize()}')


greet("mamatweli")


# 3. Return Values


def add(a, b):
    return a + b


add(5, 4)
# 4. Default parameters


def greet(name="Dear User"):
    print(f'Hello {name.capitalize()}')


greet()

# 5. DocStrings


def add(a, b):
    """ added two numbers together """
    print(f'{a} + {b} is: {a + b}')


add(3, 7)

# 6. Variable Scope


global_var = 10


def some_function():
    local_var = 5
    print(global_var + local_var)


some_function()

# Recursion


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


factorial(5)
# 8. Lambda


double = lambda x: x * 2
result = double(6)
print(result)

# 9. Functional Decorators


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper()


@my_decorator
def say_hello():
    print("Hello![From decorator class]")


say_hello()

# 10. Advanced Functions


def apply(func, x):
    return func(x)


def square(x):
    return x ** 2


result(apply(square, 5))
