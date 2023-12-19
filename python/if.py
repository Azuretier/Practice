import random


def random_number(str):
    num = random.randrange(1,4)
    print(f"{str}: {num}")
    return num

x = random_number("x")
y = random_number("y")
z = random_number("z")

if x == 1 or y == 1 or z == 1:
    print("Clear condition 1")

# x == 3 もしくは y == 3 かつ z == 2
if x == 3 or y == 3 and z == 2:
    print("Clear condition 2")

if 3 in [x,y] and z == 2:
    print("Clear condition 3")
