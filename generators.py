def square_numbers(nums):
    for num in nums:
        yield num * num

nums = [1,2,3,4,5]

sq_gen = square_numbers(nums)

while True:
    try:
        print(next(sq_gen))
    except StopIteration:
        print()
        break

sq_gen = square_numbers(nums)

for sq in sq_gen:
    print(sq)

sq_values = [x * x for x in nums]

print(sq_values)

sq_gen = (x * x for x in nums)  # generator too

for sq in sq_gen:
    print(sq)

import memory_profiler
import time
import random
import timeit

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []

    for i in range(num_people):
        person = { 'id': i, 
                   'name' : random.choice(names), 
                   'major' : random.choice(majors) }
        result.append(person)

    return result      

def people_generator(num_people):

    for i in range(num_people):
        yield { 'id': i, 
                'name' : random.choice(names), 
                'major' : random.choice(majors) }        

print(f'Memory (Before): {memory_profiler.memory_usage()} Mb')

start_time = time.process_time()
people = people_list(1000000)
end_time = time.process_time()

print(f'Memory (After): {memory_profiler.memory_usage()} Mb')
print(f'Took {end_time - start_time} seconds')


print(f'Memory (Before): {memory_profiler.memory_usage()} Mb')

start_time = time.process_time()
people = people_generator(1000000)
end_time = time.process_time()

print(f'Memory (After): {memory_profiler.memory_usage()} Mb')
print(f'Took {end_time - start_time} seconds')

