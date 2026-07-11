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

students=[("Ali",85),("Fahad",65),("Hammad",78)]

sorted_std=sorted(students, key=lambda students :students[1])

print(sorted_std)

numbers=[1,2,3,4,5,6,8,9,10,11,12]

even=list(filter(lambda x:x%2==0,numbers))
print(even)

#map function
numbers=[1,2,3,4,5]
square=list(map(lambda x:x*x,numbers))  #map will apply lamda fucntion to all numbers each time
print(square)

