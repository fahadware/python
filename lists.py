print("Topic : :Lists")


# Ordered — items keep the position you placed them in (like strings, indexing starts at 0).
# Mutable — unlike strings, you can change a list after creating it: add, remove, or modify items in place.
# Allows duplicates — [1, 1, 2, 2] is a perfectly valid list.
# Can hold mixed types — ["Ali", 25, True, 3.5] is valid 

Names=["Fahad","Hammad","Ali"]
print(Names[2])
student_detail=["Fahad","Ali","Computer science",3.5,True,21]
print("Name : ",student_detail[1])  #accessing element of list
print(student_detail)    
student_detail[1]="Khokhar"  #changing element at specific index...
print(student_detail)

fruits=["Apple","Banana","Gauva"]
print(fruits)
fruits.append("Grapes")
print(fruits)
fruits.remove("Apple")
print(fruits)

numbers=[10,12,13,14]
print("Curret List : ",numbers)
numbers.reverse()  #revers the list
print("Reverse : " ,numbers)
remove_item=numbers.pop(0)   #remove by index
print("Removed Item : ",remove_item)
print(numbers)
numbers.sort()
print("Sorted Numbers : ",numbers)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  #checking that is this element present...
print("mango" in fruits)

for fruits in fruits:
    print(fruits)  #looping through the list...


# This is how you'd represent something like a grid or table — very common in data analysis and AI/ML 
# (e.g., representing images or datasets).
matrix=[[1, 2],[3,6],[0,1]]
print(matrix)
print("Gride 0: ",matrix[0])

#simple To - do list...
tasks=["Clean room","lab tasks","project submission"]
print("======Current Task=========")
for i in tasks:
    print(i)

newTask=tasks.append("DB Assignment Submission")
print("New Task Added: ",newTask)
print("======Current Task=========")
for i in tasks:
    print(i)
remove=tasks.pop(0)
print("One task completed : ",remove)
print("====Updated Tasks====")
for i in tasks:
    print(i)

print("Number of Tottal Tasks : ",len(tasks))