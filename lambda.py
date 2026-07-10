print("Lambda functions....")
#ordinary function
def square(x):
    return x*x
number=int(input("Enter Number to take square:"))
print("Square is :",square(number))

#with Lambda function
#syntex:
# lambda argument:expression
square=lambda x:x*x
print(square(3))
 
add=lambda a,b:a+b
print(add(2,3))

greet=lambda : "Hello"
print(greet())

