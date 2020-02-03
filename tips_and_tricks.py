condition = False

x = 1 if condition else 0
print(x)

print('='*50)

num1 = 10_000_000_000
num2 = 10_000_000

print(f'{(num1 + num2):,}')

print('='*50)

names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names, start=1):
    print(index, name)

print('='*50)

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heros = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heros, universes):
    print(f'{name} is actually {hero} from {universe}')

print('='*50)

a, _ = (1, 2)

print(a)

a, b, *_ = (1, 2, 3, 4, 5)
a, b, *c = (1, 2, 3, 4, 5)

print(a, b, c, sep='\n')

a, b, *_, d = (1, 2, 3, 4, 5)
a, b, *c, d = (1, 2, 3, 4, 5)

print(a, b, c, d, sep='\n')

print('='*50)

class Person:
    pass

person = Person()

first_key = 'first'haklsim
first_val = 'Corey'

setattr(person, first_key, first_val)

print(person.first)

print(getattr(person, first_key))

print('='*50)

from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print(f'{username} : {password}')

print('='*50)

