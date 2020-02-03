import itertools

counter = itertools.count()

for num in counter:
    if num < 20:
        print(num)
    else:
        break

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

data = [100,200,300,400]

daily_data = list(zip(itertools.count(), data))
print(daily_data)

counter = itertools.count(start=5, step=5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.count(start=5, step=-2.5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

cycler = itertools.cycle([1,2,3])

print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))

toggle = itertools.cycle(('On','Off'))

print(next(toggle))
print(next(toggle))
print(next(toggle))
print(next(toggle))
print(next(toggle))
print(next(toggle))
print(next(toggle))

repeater = itertools.repeat(2)

print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))

repeater = itertools.repeat(6, times=3)

for i in repeater:
    print(i)

squares = list(map(pow, range(10), itertools.repeat(2)))
print(squares)

cubes = list(map(pow, range(10), itertools.repeat(3)))
print(cubes)

squares = list(itertools.starmap(pow, [(0,2), (1,2), (2,2)]))
print(squares)

# combination - order does not matter
# permutation - order does matter
# no repeats in both 

letters = ['a', 'b', 'c', 'd']

result = itertools.combinations(letters, 2)
for item in result:
    print(item)

print()    

result = itertools.permutations(letters, 2)
for item in result:
    print(item)    

print()    

numbers = [0,1,2,3]

# repeats allowed
result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)    

print()    

result = itertools.combinations_with_replacement(numbers, 4)
for item in result:
    print(item)    

names = ['Corey','Nicole']

# chain

combined = letters + numbers + names
for item in combined:
    print(item)    

combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)    

# slice

result = itertools.islice(range(10), 5)
for item in result:
    print(item)    

result = itertools.islice(range(10), 1, 5, 2) # start, end, step
for item in result:
    print(item)    

with open('test.txt', 'r') as f:
    three_lines = itertools.islice(f, 3)
    for line in three_lines:
        print(line,end='') 

# compress

selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)
for item in result:
    print(item)    

print()

result = filter(lambda x: x < 2, numbers)
for item in result:
    print(item)    

print()

result = itertools.filterfalse(lambda x: x < 2, numbers)
for item in result:
    print(item)    

print()

# drop while - drop all variables until the first item that satisfy the filter condition, 
# after that it drops the filters and returns the remaining values

numbers2 = [0,1,2,3,2,1,0]
result = itertools.dropwhile(lambda x: x < 2, numbers2)
for item in result:
    print(item)    

print()

# take while is the opposite of drop while
result = itertools.takewhile(lambda x: x < 2, numbers2)
for item in result:
    print(item)    

print()

# accumulate 

# cumulative sum
result = itertools.accumulate(numbers)
for item in result:
    print(item)    

print()

# cumulative multiples
import operator

number3 = [1,2,3,2,1,0]
result = itertools.accumulate(number3, operator.mul)
for item in result:
    print(item)    

# group by

def get_state(person):
    return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
]

sorted_people = sorted(people, key=get_state)

# group by can only handle sorted iterable
person_group = itertools.groupby(sorted_people, get_state)
for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()

# duplicate

# note that sorted_people cannot be used after this call
copy1, copy2 = itertools.tee(sorted_people)

for people in copy1:
    print(people['state'])

print()

for people in copy2:
    print(people['state'])   

print()

for people in sorted_people:
    print(people['state'])   
