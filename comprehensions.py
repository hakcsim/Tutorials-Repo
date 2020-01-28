nums = [*range(1, 11)]

print(nums)

l0 = [n for n in nums]
print(l0)

l1 = [n * n for n in nums]
print(l1)

l2 = map(lambda n: n * n, nums)  # l2 is a function not a list
print([*l2])

l3 = [n for n in nums if n % 2 == 0]
print(l3)

l4 = filter(lambda n: n % 2 == 0, nums)
print([*l4])

ll3 = [n if n % 2 == 0 else -1 for n in nums]
print(ll3)

l5 = [(x, y) for x in "abcd" for y in range(4)]
print(l5)

l6 = [(x, y) for y in range(4) for x in "abcd"]
print(l6)

print(l5 == l6)

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverin", "Deadpool"]

d0 = {name: hero for name, hero in zip(names, heros)}
print(d0)

d1 = {name: hero for name, hero in zip(names, heros) if hero != "Spiderman"}
print(d1)

data = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

s0 = {*data}
print(s0)

s1 = {n for n in data}
print(s1)


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)


for n in my_gen:
    print(n, end=",")

