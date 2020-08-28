def  decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('inner function executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwargs):
#         print('inner function executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)

@decorator_function    # display = decorator_function(display)
def display():
    print('Hi it is from display')

@decorator_function
def display_info(name, age):
    print(f"My name is {name} and i am {age} years old")

# @decorator_class    # display = decorator_function(display)
# def display():
#     print('Hi it is from display')

# @decorator_class
# def display_info(name, age):
#     print(f"My name is {name} and i am {age} years old")

display_info('fahim', 23)
display()