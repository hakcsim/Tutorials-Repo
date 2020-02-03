def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

def add_employee_fixed(emp, emp_list=None):
    if not emp_list:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

print(add_employee.__defaults__)
add_employee('Corey')
print(add_employee.__defaults__)
add_employee('John')
print(add_employee.__defaults__)

print(add_employee_fixed.__defaults__)
add_employee_fixed('Corey')
print(add_employee_fixed.__defaults__)
add_employee_fixed('John')
print(add_employee_fixed.__defaults__)

import time
from datetime import datetime

def display_time(time_to_print=datetime.now()):
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

def display_time_fixed(time_to_print=None):
    if not time_to_print:
        time_to_print = datetime.now()
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

print(display_time.__defaults__)
display_time()
time.sleep(1)    
print(display_time.__defaults__)
display_time()
time.sleep(1)    
print(display_time.__defaults__)
display_time()

print(display_time_fixed.__defaults__)
display_time_fixed()
time.sleep(1)    
print(display_time_fixed.__defaults__)
display_time_fixed()
time.sleep(1)    
print(display_time_fixed.__defaults__)
display_time_fixed()
