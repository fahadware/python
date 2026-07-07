print("sets....")

name={"Fahad","hammad","shahzaib"}
print(name)
name={"Fahad","Fahad","Hammad"}  #Remove automaticaly
print(name)
record={"Fahad","Hammad"}
print(record)
record.add("shahzaib")
print(record)
record.remove("shahzaib")  #remove element error if not found
print(record)
record.discard("Fahad")

fruits = {"apple", "banana", "cherry"}  
print("apple" in fruits)       #checking membership
print("mango" in fruits)

list_of_numbers=[1,1,2,3,4,4,5,6,7,7,8,9,10,10,11]

unique_numbers=set(list_of_numbers)  #extracting unique from list through sets...
print(unique_numbers)
list=list(set(list_of_numbers))  #convert back into list removing dupliacte
print(list)
#Taking union
morning_customer={"Ali","Fahad","Kashif"}
evening_customer={"Ali","hammad","Kahsif"}
all_customer=morning_customer|evening_customer  #taking union....
print("All customers:",all_customer)    
#Taking intersection...
morning_customer={"Ali","Fahad","Kashif"}
evening_customer={"Ali","Fahad","Kahsif"}
both=morning_customer&evening_customer   #this giving customer that visited both time by taking intersection
print("Customer Visited in both shifted:",both)    

#difference(Give 1st set element that are not in 2nd set)
morning_customer={"Ali","Fahad","Kashif"}
evening_customer={"Ali","hammad","Kahsif"}
only_morning=morning_customer-evening_customer  
print("Customer Visited in Morning:",only_morning)  


monday_visitors = ["Ali", "Sara", "fahad", "Ali", "Zain"]
tuesday_visitors = ["shahzaib", "ali", "Zain", "Zain"]

monday_set = set(monday_visitors)
tuesday_set = set(tuesday_visitors)

print("Unique Monday visitors:", monday_set)
print("Unique Tuesday visitors:", tuesday_set)

all_visitors = monday_set | tuesday_set
returning_visitors = monday_set & tuesday_set
monday_only = monday_set - tuesday_set

print("\nAll unique visitors across both days:", all_visitors)
print("Visitors who came both days:", returning_visitors)
print("Visitors who ONLY came Monday:", monday_only)