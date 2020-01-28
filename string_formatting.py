person = {"name": "Jenn", "age": 23}

print("My name is {} and I am {} years old".format(person["name"], person["age"]))
print("My name is {0} and I am {1} years old".format(person["name"], person["age"]))
print("My name is {0[name]} and I am {0[age]} years old".format(person))
print("My name is {name} and I am {age} years old".format(**person))
print("My name is {name} and I am {age} years old".format(name="Jenn", age="23"))

l = ["Jenn", "23"]
print("My name is {0[0]} and I am {0[1]} years old".format(l))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Jack", "33")

print("My name is {0.name} and I am {0.age} years old".format(p1))

i = 9
print("The value is {:03}".format(i))

import math

print("The value is {:.3f}".format(math.pi))
print("The value is {:,}".format(1000 ** 2))
print("The value is {:,.2f}".format(1000 ** 2))

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

print("Date is {}".format(my_date))
print("Date is {:%B %d, %Y}".format(my_date))

print(
    "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.".format(my_date)
)

