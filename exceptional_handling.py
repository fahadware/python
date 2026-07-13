while True:
    try:
        number=input("Enter Number:")
        num=int(number)
        break
    except:
        print("Thats not Valid number plz enter valid number:")

print("Thanks for entering valid number")
# full structed syntex
# try:
#     # risky code
# except SomeError:
#     # handle error
# else:
#     # runs ONLY if no error occurred
# finally:
#     # ALWAYS runs, error or not

try:
    number = int("abc")
except ValueError:
    print("That's not a valid number!")
#error when divided by zero
try:
    number=10/0
except ZeroDivisionError as z:
    print("Error:",z)

#kye not found error when accessing
    person = {"name": "Ali"}
try:
    print(person["age"])
except KeyError as k:
    print("That key doesn't exist!")

#lets try another example
def safdivide(a,b):
    try:
        result=a/b
    except ZeroDivisionError as z:
        print("Error:",z)
        return None
    except TypeError:
        print("Both value should be numbers")
        return None
    else:
        return result
print(safdivide(10,2))
print(safdivide(10,0))
print(safdivide(10,"a"))


while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number, try again.")

print("Your age is:", age)

#manually raising error
def set_age(age):
    if age<0:
        raise ValueError("Age can not be negative")
    return age
try:
    set_age(-5)
except ValueError as e:
    print("Caught Error:",e)

#Basic calculator example to avoid input error using try,except,raise
def safe_calculator():
    try:
        num1=float(input("Enter First number"))
        num2=float(input("Enter second number"))
        operation=input("Enter operation(+,-,*,/)")
        if operation=="+":
            result=num1+num2
        elif operation=="-":
            result=num1-num2
        elif operation=="*":
            result=num1*num2
        elif operation=="/":
            result=num1/num2
        else:
            raise ValueError("Invalid Operation symbol")
    except ValueError as e:
        print("Error:",e)
    except TypeError as t:
        print("Typeerror:",e)

    except ZeroDivisionError as z:
        print("Error:",z)
    else:
        print("Result is:",result)
safe_calculator()

#usage in api request
# try:
#       response = requests.get(url, timeout=5)
#   except requests.exceptions.Timeout:
#       print("Request timed out, retrying...")
#in file operation

try:
    with open("data.csv") as f:
        data=f.read()
except FileNotFoundError as f:
    print("Error:",f)