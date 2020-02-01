import math
import datetime

for n in range(1,11):
    print(f'The value is {n:02}')

print(f'PI is {math.pi}')
print(f'PI is {math.pi:.4f}')

bday = datetime.datetime(2020, 1, 29)

print(f'bday is {bday:%B %d, %Y}')
