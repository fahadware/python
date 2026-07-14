#Technical definition: A class is a blueprint/template for creating objects, 
# defining the attributes (data) and methods (functions) that its objects will have.
#  An object (also called an instance) is a specific, concrete realization of that class, 
# created via a process called instantiation.


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hi , Im ",self.name," and I am ",self.age," Year Old")

person1=person("Fahad",21)  #Creating (instantiating) objects from the class:
person2=person("Hammad",14)

#accesing objects:
print("Name:",person1.name)
print("Age:",person1.age)

person1.greet()
person2.greet()

#inhertence 
#inherit from person
class student(person):
    def __init__(self, name, age,school):
        super().__init__(name, age)
        self.school=school
    def study(self):
        print(self.name," is studied in ",self.school)

object = student("Fahad", 21, "HARMAIN")
object.study()
object.greet()

#simple class with attribute
class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
my_animal=Animal("Dog","German Shephard")
print(my_animal.name)
print(my_animal.breed)

#now with method
class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def animal_sound(self):
        print(self.name,"Says wooo")
    
my_animal=Animal("Dog","German Shephard")
print(my_animal.name)
print(my_animal.breed)
my_animal.animal_sound()

#modifing clas attribute
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}'s new balance: {self.balance}")

account = BankAccount("Ali", 1000)
account.deposit(500)

#inheritence
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"Is eating")
class Dog(Animal):
    def bark(self):
        print(self.name,"Says wooo!")

mydog=Dog("puppy")
mydog.eat()
mydog.bark()
        
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")   # reuse Animal's setup logic

my_dog = Dog("Puppy")
my_dog.make_sound()

#Polymorphism — same method name, different behavior
class cat:
    def speak(self):
        print("Meow")
class dog:
    def speak(self):
        print("wooo")
Animals=[cat(),dog()]
for animals in Animals:
    animals.speak()
        
#encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # single underscore = "internal use" convention->private

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

account = BankAccount("Ali", 1000)
account.withdraw(200)