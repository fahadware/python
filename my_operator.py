print("Operators...")
num=10+2
print(num)
num=10-2
print(num)
num=10/2
print(num)
num=10//2  #cut division
print(num)
num=10*2  
print(num)
num=10**2   #exponent
print(num)

#comapision operator.... return true/fals

age=18
valid=age>18
print(valid)
age=18
valid=age<18
print(valid)
age=18
valid=age!=18
print(valid)
age=18
valid=age==18
print(valid)
age=18
valid=age>=18
print(valid)
age=18
valid=age<=18
print(valid)

#logical operato;
age=18
isvalid=age>18 and age<18
print(isvalid)

print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)

number=7
if number%2==0:
 print("Even")
else:
 print("Odd")
 
#example...........
marks=float(input("Enter Your Marks"))
passed=marks>=40
Distinction=marks>=85

print("Passed:", passed)
print("Distinction:", Distinction)

percentage_needed=100-marks
 
print("Marks needed to score full : ",percentage_needed)
