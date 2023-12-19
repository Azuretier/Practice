import random


def random_number(str):
    num = random.randrange(1,4)
    print(f"{str}: {num}")
    return num

def random_char():
    char = random.choice(["a","b","c"])
    print(f"char: {char}")
    return char

x = random_number("x")
y = random_number("y")
z = random_number("z")

if x == 1 or y == 1 or z == 1:
    print("Clear condition 1")

# x == 3 もしくは y == 3 かつ z == 2
if x == 3 or y == 3 and z == 2:
    print("Clear condition 2")

# x == 13 かつ z == 2 はなどxかyに"3"が含まれていればTrueになるわけではない
if 3 in [x,y] and z == 2:
    print("Clear condition 3")

char = random_char()

if char in ["aaa","bbb","ccc"]:
    print("Clear condition 4")

if char in "asset":
    print("Clear condition 5")

if char in ["a","b"]:
    print("Clear condition 6")

if any(word in "heyyy" for word in ["hello", "hey", "hi"]):
    print("Clear condition 7")