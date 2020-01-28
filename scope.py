"""
LEGB
Local, Enclosing, Global, Built-in
"""

x = "global x"
print(x)


def test_local_x():
    x = "local x"
    print("test_local_x =", x)


def test_global_x():

    global x  # create global x if it does not exist in global scope
    x = "global x2"
    print("test_global_x =", x)


def test_global_x2():
    print("test_global_x2", x)


def test_global_z():

    global z  # create global x if it does not exist in global scope
    z = "global z"
    print("test_global_z", z)


test_local_x()
print(x)

test_global_x()
print(x)

test_global_x2()

test_global_z()
print(z)

import builtins

print(dir(builtins))

m = min([5, 1, 4, 2, 3])
print(m)


def min():
    pass


# m = min([5, 1, 4, 2, 3]) # local min() override builtin min(...), will throw TypeError


def outer():

    x = "outer x"

    def inner():
        x = "inner x"
        print("inner =", x)

    def inner2():
        print("inner2 = ", x)

    def inner3():
        nonlocal x
        x = "inner3 x"
        print("inner3 =", x)

    def inner4():
        global x
        x = "inner4 x"
        print("inner4 =", x)

    inner()
    print(x)
    inner2()
    print(x)
    inner3()
    print(x)
    inner4()
    print(x)


outer()

print(x)

