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
