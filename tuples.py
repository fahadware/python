print("Tuples....")
names=("Fahad","Hammad","Shahzaib")
for i in names:
    print(i)

print(names[0])  #Accessing items

coordinates = (10, 20)

print(coordinates[0])    # 10
print(coordinates[-1])   # 20

coordinates[0] = 99   #  TypeError! because tuples are unchangable...


std_info=("Fahad","21","CS","3.1")
name,age,department,cgpa=std_info  #Tuple unpacking
#Important: if a tuple contains a mutable object (like a list) inside it, that inner list can still be changed — only the tuple's own structure 
# (what's at each position) is locked:
print(name)
print(age)
print(department)
print(cgpa)

#checking tuples...
not_a_tuple=(5)
tuple=(5,)
print(type(not_a_tuple))
print(type(tuple))

#modifying tuple givebttype error because tuples are not changable...
point = (10, 20)
point[0] = 99

scores=(100,90,80)
print(len(scores))
print(scores.count(80))
print(scores.index(90))

#nested tuple..
student=("Fahad",(100,90,20))
print(student[0])
print(student[1])
print(student[1][0]) #it gives second element of nested tuple

student=("Fahad",23,"computer science",3.1)
name,roll_no,department,gpa=student
print('====student detail==========')
print("Name:",name)
print("roll no:",roll_no)
print("department:",department)
print("gpa:",gpa)

print("Tottal fields in record:",len(student))
print("is 'computer scient' is in record : ","computer science"in student)
