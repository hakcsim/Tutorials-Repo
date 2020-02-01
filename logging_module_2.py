import logging
from employee import Employee

logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('./test_files/sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# do not need this anymore
# logging.basicConfig(filename='./test_files/sample.log', level=logging.DEBUG, 
#                     format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y    

def multiply(x, y):
    return x * y        

def divide(x, y):
    try:
        result = x / y            
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result        

num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logger.debug(f'Sub: {num_1} - {num_2} = {sub_result}') # default is warning, only this one and below will print to console

mul_result = multiply(num_1, num_2)
logger.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logger.debug(f'Div: {num_1} / {num_2} = {div_result}')

