li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)

print(s_li)

print(li)

li.sort()

print(li)

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

r_li = sorted(li, reverse=True)
print(r_li)

ti = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_t = sorted(ti)
print(s_t)

di = {"name": "Corey", "job": "programming", "age": 23, "os": "Mac"}
s_di = sorted(di)
print(s_di)

lx = [-6, -5, -4, 1, 2, 3]
s_lx = sorted(lx)
print(s_lx)

# absolute value sort
s_lx = sorted(lx, key=abs)
print(s_lx)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.age}, ${self.salary}"


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 90000)
e3 = Employee("John", 43, 80000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.salary


s_employees = sorted(employees, key=e_sort)
print(s_employees)

r_employees = sorted(employees, key=e_sort, reverse=True)
print(r_employees)


s_lambda_employees = sorted(employees, key=lambda e: e.name)
print(s_lambda_employees)

from operator import attrgetter

s_attrgetter_employees = sorted(employees, key=attrgetter("age"))
print(s_attrgetter_employees)

