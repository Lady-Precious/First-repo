print ('hello world this is me practicing git and github')
print('yippeee')
 
# TUESDAY 19TH JAN 2021
# FUNCTIONS

def max(x, y):
    if x >=y:
        return x
    else:
        return y

print(max(4, 7))
z  = max (8, 5)
print (z)

def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

#Import modules

import random
for i in range(5):
    value = random.randint(1, 6)
    print(value)

from math import pi
print(pi)

from math import pi, sqrt
from math import sqrt as square_root
print (square_root(100))

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(4)) 

quote = "This python tutorial video is very fast"
#print("%s %s %s" % ('I like the quiet and serenity', quote))

print("i don't like", end="")
print(" newlines")
print ("hi, thanks Jerry for helping me out")