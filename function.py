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