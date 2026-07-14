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