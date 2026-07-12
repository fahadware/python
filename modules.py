
#built -in modules
import math
sqaure=math.sqrt(16)
print(sqaure)

#importing as alies
import math as mt
sqaure=mt.sqrt(16)
print(sqaure)
print(mt.factorial(2))

import random 
print(random.randint(1,10))   #generet random number from 1-10
print(random.choice(["a","b","c"]))  #randomly pick one from this list
import os

print(os.getcwd())   # prints your current working directory

#1 ye file bnayi calculator ka name sa
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

#dusri file ma uper walai method import kiya 
import calculator
print(calculator.add(5,3))
print(calculator.subtract(2,1))


