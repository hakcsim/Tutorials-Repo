# Duck typing and Easier to ask Forgivenness then Permission (EAFP)

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print('I am quacking like a duck!')

    def fly(self):
        print('I am flapping my arms!')

def quack_and_fly(thing):
    # NOT Duck type (Non-Pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This thing has to be a Duck!')

    print()

def quack_and_fly_1(thing):
    # Duck type (Pythonic)
    thing.quack()
    thing.fly()

    print()

def quack_and_fly_2(thing):
    # LBYL Look Before You Leap (Non Pythonic)

    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

    print()

def quack_and_fly_3(thing):
    # EAFP Easier to ask Forgivenness then Permission (Pythonic)

    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)    

    print()


d = Duck()
p = Person()

quack_and_fly(d)
quack_and_fly(p)

quack_and_fly_1(d)
quack_and_fly_1(p)

quack_and_fly_2(d)
quack_and_fly_2(p)

quack_and_fly_3(d)
quack_and_fly_3(p)


person = {'name': 'Jesse', 'age' : 23, 'job' : 'Programmer'}

# LBYL (Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))

# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))
except KeyError as e:
    print('Missing {} keys'.format(e))

person = {'name': 'Jesse', 'age' : 23}

# LBYL (Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))

# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))
except KeyError as e:
    print('Missing {} keys'.format(e))

my_list = [1,2,3,4,5]

# LBYL (Non-Pythonic)
if len(my_list) > 5:
    print(my_list[5])
else:
    print('That index does not exist')

# EAFP (Pythonic)
try:
    print(my_list[5])
except IndexError as e:
    print('That index does not exist: {}'.format(e))

import os

my_file = 'test.txt'

# Race condition
if os.access(my_file, os.R_OK):
    with open(my_file, 'r') as f:
        print(f.read())
else:
    print('File cannot be accessed') 

# No race condition
try:
    f = open(my_file, 'r')
except IOError as e:
    print('File cannot be accessed')
else:
    with f:
        print(f.read())


