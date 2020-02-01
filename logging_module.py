import logging

# this must be called before any logging

# print to console
# logging.basicConfig(level=logging.DEBUG)

# log to file
# logging.basicConfig(filename='./test_files/test.log',  level=logging.DEBUG)

# log to file with time, level and message
logging.basicConfig(filename='./test_files/test.log',  level=logging.DEBUG, 
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

# DEBUG: Detaited information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected
# WARNING: (Default) An idication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low').  The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running   

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y    

def multiply(x, y):
    return x * y        

def deivide(x, y):
    return x / y            

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logging.warning(f'Sub: {num_1} - {num_2} = {sub_result}') # default is warning, only this one and below will print to console

mul_result = multiply(num_1, num_2)
logging.error(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = multiply(num_1, num_2)
logging.critical(f'Div: {num_1} / {num_2} = {div_result}')

add_result = add(num_1, num_2)
logging.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logging.debug(f'Sub: {num_1} - {num_2} = {sub_result}') # default is warning, only this one and below will print to console

mul_result = multiply(num_1, num_2)
logging.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = multiply(num_1, num_2)
logging.debug(f'Div: {num_1} / {num_2} = {div_result}')

class Employee:

    # class variable - shared between instances
    raise_amount = 1.04

    num_of_emps = 0

    def __init__(self, first, last, pay):

        # instance variables - unique to each instance

        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

        logging.info(f'Created Employee: {self.first} {self.last}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Hak', 'Sim', 100000000)
emp_2 = Employee('Corey', 'Schafer', 200000000)




