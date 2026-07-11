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

even=list(filter(lambda x:x%2==0,numbers))  #filter() keeps only the items where the lambda returns True..
print(even)

#map function
numbers=[1,2,3,4,5]
square=list(map(lambda x:x*x,numbers))  #map will apply lamda fucntion to all numbers each time
print(square)


# Forgetting key= when using lambda with sorted()/max()/min()
students = [("Ali", 85), ("Sara", 92)]
#    sorted_students = sorted(students, lambda s: s[1])   # ❌ TypeError — missing "key="
sorted_students = sorted(students, key=lambda s: s[1])   # ✅ correct

numbers=[20,10,30,100,35,15]
maximum=max(numbers,key=lambda x:x)
print(maximum)

#task..
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300}
]

sorted_by_price = sorted(products, key=lambda p: p["price"])
sorted_by_name = sorted(products, key=lambda p: p["name"])
expensive_items = list(filter(lambda p: p["price"] > 100, products))
discounted_prices = list(map(lambda p: p["price"] * 0.9, products))

print("Sorted by price:", sorted_by_price)
print("Sorted by name:", sorted_by_name)
print("Expensive items (>100):", expensive_items)
print("Discounted prices (10% off):", discounted_prices)