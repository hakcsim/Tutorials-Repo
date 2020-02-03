s0 = set()

for i in range(10):
    s0.add(i)
    s0.add(i)

print(s0)

s1 = set([*range(1,6)])
print(s1)

s1.update([6,7,8])
print(s1)

s2 = {7,8,9}
s1.update([6,7,8], s2)
print(s1)

s1.remove(5)
print(s1)

try:
    s1.remove(10)
    print(s1)
except KeyError:
    print('set remove throw KeyError if item does not exist in set')

# set discard does not throw KeyError if item does noit exist in set
s1.discard(6)
s1.discard(6)
print(s1)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}

s4 = s1.intersection(s2)
print(s4)

s4 = s1.intersection(s2, s3)
print(s4)

s4 = s1.difference(s2)
print(s4)

s4 = s2.difference(s1)
print(s4)

s4 = s2.difference(s1, s3)
print(s4)

# number unique in s1 and s2
s4 = s1.symmetric_difference(s2)
print(s4)

l1 = [1,2,3,1,2,3]

l2 = set(l1)
l2 = list(l2)
print(l2)

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

# can use list in set functions
print(set(gym_members).intersection(developers))
print(set(employees).difference(gym_members, developers))

# set is more efficient for membership test
# O(n) for list
# O(1) for set
if 'Corey' in developers:
    print('Found!')

