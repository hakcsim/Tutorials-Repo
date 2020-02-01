from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

print(Color._fields)

color = Color(55,155,255)

print(color.red, color[2])
print(color.green, color[1])
print(color.blue, color[0])

color2 = Color(red=50,green=100,blue=200)

print(color2.red, color2[2])
print(color2.green, color2[1])
print(color2.blue, color2[0])

# throw AttributeError - namedtuple is immutable
color.red = 99