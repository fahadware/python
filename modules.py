
#built -in modules
import math
sqaure=math.sqrt(16)
print(sqaure)

#importing as alies
import math as mt
sqaure=mt.sqrt(16)
print(sqaure)

#1 ye file bnayi calculator ka name sa
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

#dusri file ma uper walai method import kiya 
import calculator
print(calculator.add(5,3))
print(calculator.subtract(2,1))