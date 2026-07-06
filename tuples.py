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
print(name)
print(age)
print(department)
print(cgpa)