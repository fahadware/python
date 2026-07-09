# #basic funtion defination
# def func_name():
   #here code which will run

# #defination with parameters
# def func_name(paramter1,parameter2):

def add(para):
    result=para*2
    return print(result)


add(4)

def greet(name="Guest"):  #function defination
    print("Hello Mr",name)
greet()        #funtion calling without argument..
greet("fahad")    #funtion calling with argument..

def describe_person(name,age,cast):
    return print("Name:",name,"\n","Age:",age,"\n","Cast:",cast)
    
describe_person(name="Fahad",cast="khokhar",age=21)  #explcict argument calling...order does'nt matter

def add(a,b):
    result=a+b
    print(result)
add(1,2)


def power(base,exponent=2):
    return base**exponent
print(power(5))


#funtion calling other function...
def square(x):
    return x*x
def sum_of_square(a,b):
    return square(a)+square(b)
print(sum_of_square(2,2))

#returning multiple value using tuple unpacking....
def min_max(numbers):
    return min(numbers),max(numbers)
lowest,highest=min_max([2,4,9,1,10,0])
print("lowest:",lowest)
print("higest:",highest)

#*arg---accept any number of arguments..
def addition(*numbers):
    tottal=0
    for num in numbers:
        tottal+=num
    return tottal
print(addition(1,2,3))
print(addition(1,2,3,6,7,8,9,10))


# (**kwargs) — accepting any number of keyword arguments

def profile(**details):
    for key,values in details.items():
        print(key,":",values)

profile(name="fahad",age=21)

def preprocess_data(raw_data):
      cleaned = raw_data.lower().strip()
      return cleaned


print(preprocess_data("My naMe is FahAd"))

#simple calcultor using python....
import time 
def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
     if b == 0:
      return "Cannot divide by zero"
     return a / b
def power(base,exponent):
    return base**exponent
def display(result):
    if isinstance(result, float) and result.is_integer():
        print("Result is:", int(result))
    else:
        print("Result is:", result)
choice=0
while True:
  print("\tBasic Calculator\t")
  print("Select Operation")
  print("1:Addtion\n2:Subtraction\n3:Multiplication\n4:Division\n5:Power\n6:Exist")
  choice=int(input("Enter You Choice:"))
  if choice==1:
    num1=float(input("Enter 1st Number:"))
    num2=float(input("Enter second Number:"))
    display(add(num1, num2))
  elif choice==2:
    num1=float(input("Enter 1st Number:"))
    num2=float(input("Enter second Number:"))
    display(subtraction(num1,num2))
  elif choice==3:
    num1=float(input("Enter 1st Number:"))
    num2=float(input("Enter second Number:"))
    display(multiplication(num1,num2))
  elif choice==4:
    num1=float(input("Enter 1st Number:"))
    num2=float(input("Enter second Number:"))
    display(division(num1,num2))
  elif choice==5:
    num1=float(input("Enter Base:"))
    num2=float(input("Enter Power:"))
    display(power(num1,num2))
  elif choice==6:
      print("Existing.....")
      time.sleep(2)
      break
      
  else:
    print("Plz enter correct Choice...")


