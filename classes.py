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

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first = None
        self.last = None

    # apply_raise1 and apply_raise are the same
    # class variable can only be accessed via
    # the class or instance. 

    def apply_raise1(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def apply_raise(self):
        # self.raise_amount is the same as Employee.raise_amount
        # if no new raise_amount is created for an instance when
        # user explicity assign a value to self.raise_amount  

        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount  

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static class method has no class or instance 
    # added to class for logical purpose only
    @staticmethod
    def is_work_day(day):
        return day.weekday() == 5 or day.weekday() == 6

    # special (Magic / Dunder) methods

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    # will use __repr__ in print() if __str__ is not provided
    def __str__(self):
        return f'{self.fullname}, {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)      

class Developer(Employee):

    # override base class Employee raise_amount
    # meaning that Employee and Develop raise_amount
    # are not the same
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # or Employee.__init__(self, first, last, pay)
        # need this for multiple inheritances
        self.prog_lang = prog_lang

class Manager(Employee):

    # override base class Employee raise_amount
    # meaning that Employee and Develop raise_amount
    # are not the same
    raise_amount = 1.1

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # or Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname = 'Hak Sim'

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname)

print(emp_1.pay)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.__dict__)

emp_2.raise_amount = 1.05  # this create a new raise_amount in emp_1 ! This may be useful if we want an instance to have different raise amount
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

Employee.raise_amount = 1.06
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(Employee.num_of_emps)

Employee.set_raise_amt(1.07)
print(emp_1.raise_amount)
print(emp_2.raise_amount)  # this is stuck at 1.05
print(Employee.raise_amount)

emp_2.set_raise_amt(1.08)
print(emp_1.raise_amount)
print(emp_2.raise_amount)  # this is stuck at 1.05
print(Employee.raise_amount)

emp_str_3 = 'John-Doe-70000'

emp_3 = Employee.from_string(emp_str_3)

import datetime

print(Employee.is_work_day(datetime.datetime(2020, 1, 30)))
print(Employee.is_work_day(datetime.datetime(2020, 2, 1)))

print(help(Developer))

dev_1 = Developer('Corey', 'Schafer', 10000, 'Python')
dev_2 = Developer('Test', 'Employee', 10000, 'Java')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# check if an object is an instance of a class
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))

print(mgr_1)
print(mgr_1.__repr__())
print(mgr_1.__str__())


print(1+2)
print(int.__add__(1, 2))
print(str.__add__('A', 'B'))

print(mgr_1 + dev_1)

print(len('test'))
print('test'.__len__())

print(len(mgr_1))

del emp_1.fullname

