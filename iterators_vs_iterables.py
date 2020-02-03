# iterable - something that can be looped over, e.g. list, tuples, dict, file etc
# __iter__() dunder method implemented
# must return an iterator from its __iter__ method
# and an iterator must define a __next__ method

nums = (1,2,3)

for num in nums:
    print(num)

print(dir(nums))

# iter() call the __iter__() method in the background
# next() call the __next__() method in the background

# i_nums_0 and i_nums are the same
i_nums_0 = nums.__iter__
i_nums = iter(nums)

print(i_nums)
print(dir(i_nums))

# list is a iterable but NOT an iterator
# iterator has a state where it knows where it is during iteration and it also know how to fetch its next value 
# __next__ dunder method implemement

try:
    print(next(nums))
except TypeError:
    print('list is not an iterator')    

# for loop actually uses the iterator 
# stops when StopIteration raised
while (True):
    try:
        print(next(i_nums))
    except StopIteration:
        break

print('='*50)

# both iterator and iterable
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # return iterator (__next__) 
    def __iter__(self):
        return self 

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        else:
            current = self.value
            self.value += 1
            return current

nums = MyRange(1, 10)

# iterable
for num in nums:
    print(num)

print()

# cannot call next or iter again on nums because loop has exhausted

# for num in nums:
#     print(num)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# generators are iterators as well but __iter__ and __next__ are created automatically

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

# continue from above
for num in nums:
    print(num)

def my_range_forever(start):
    current = start
    while True:
        yield current
        current += 1

nums = my_range_forever(1)

for num in nums:
    if num == 20:
        break
    print(num)

class Sentence:
    def __init__(self, sentence):
        self.words = sentence.split(' ')
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.words):
            result = self.words[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)       

def get_word(sentence):
    words = sentence.split(' ')
    index = 0
    while index < len(words):
        yield words[index]
        index += 1

for word in get_word('This is a test'):
    print(word)       
