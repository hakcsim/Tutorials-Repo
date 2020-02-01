import logging
import requests

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('./test_files/employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# do not need this anymore
# logging.basicConfig(filename='./test_files/employee.log', level=logging.INFO, 
#                     format='%(levelname)s:%(name)s:%(message)s')

class Employee:

    # class variable - shared between instances
    raise_amount = 1.05

    num_of_emps = 0

    def __init__(self, first, last, pay):

        # instance variables - unique to each instance

        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

        logger.info(f'Created employee: {self.first} {self.last}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'    


if __name__ == '__main__':
    emp_1 = Employee('Hak', 'Sim', 10000000)
    emp_2 = Employee('Corey', 'Schafer', 10000000)
