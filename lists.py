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
numbers.reverse()  #revers the list
print(numbers)
remove_item=numbers.pop(0)   #remove by index
print("Removed Item : ",remove_item)
print(numbers)