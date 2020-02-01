def outer_function(msg):

    message = msg

    def inner_function():
        print(message)

    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

# same as above
def outer_function_2(msg):

    def inner_function():
        print(msg)

    return inner_function

hi_func = outer_function_2('Hi')
bye_func = outer_function_2('Bye')

hi_func()
bye_func()

# functionalities to original function

def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()

    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)

decorated_display()

# same as above 

@decorator_function
def display2():
    print('display function ran')

display2()

# will work with or without arguments
def decorator_function_with_args(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)

    return wrapper_function

@decorator_function_with_args
def display3():
    print('display function ran')

@decorator_function_with_args
def display_info(name, age):
    print(f'display_info ran with arguments: {name}, {age}')

display3()
display_info('John', 25)

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        self.original_function(*args, **kwargs)

@decorator_class
def display4():
    print('display function ran')

@decorator_class
def display_info2(name, age):
    print(f'display_info ran with arguments: {name}, {age}')

display4()
display_info2('John', 25)

# Practical examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.process_time()
        result = orig_func(*args, **kwargs)
        t2 = time.process_time()
        print(f'Ran {orig_func.__name__} for {t2 - t1} seconds')
        return result

    return wrapper

import time

# @my_logger 
# def display_info3(name, age):
#     print(f'display_info3 ran with arguments: {name}, {age}')

# @my_timer 
# def display_info4(name, age):
#     time.sleep(1)
#     print(f'display_info4 ran with arguments: {name}, {age}')

# display_info3('Hank', 78)
# display_info4('Dawn', 37)

# chain decorators

# @my_logger 
# @my_timer # executed first
# def display_info5(name, age):
#     time.sleep(1)
#     print(f'display_info5 ran with arguments: {name}, {age}')

# display_info5('Dave', 35)

# # same as above

# display_info_func = my_logger(my_timer(display_info5('Dave', 35)))


from functools import wraps

def my_logger_2(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer_2(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.process_time()
        result = orig_func(*args, **kwargs)
        t2 = time.process_time()
        print(f'Ran {orig_func.__name__} for {t2 - t1} seconds')
        return result

    return wrapper

@my_logger_2 
@my_timer_2 # executed first
def display_info6(name, age):
    time.sleep(1)
    print(f'display_info5 ran with arguments: {name}, {age}')

display_info6('John', 23)

# decorator that takes arguments

def prefix_decorator(prefix):
    def decorator_function(orig_func):
        @wraps(orig_func)
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executing before', orig_func.__name__)
            result = orig_func(*args, **kwargs)
            print(prefix, 'Executing after', orig_func.__name__)
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator('LOG:')
def display_info7(name, age):
    time.sleep(1)
    print(f'display_info7 ran with arguments: {name}, {age}')

display_info7('Abe', 45)


