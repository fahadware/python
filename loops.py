#for loop condition....
for i in range(10):
 print(i)

#different ranges of for loop...
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5 (start, stop)
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (start, stop, step)
    print(i)

#break and continue statement....
for i in range(0,10,2):
 if i==4:
    break  #this will stop when 4 arrive...
 print(i)

for i in range(0,10,2):
 if i==4:
    continue  #this will skip 4 and continue the programe...
 print(i)


 count=0
collection=["iphone12","Mouse","Keyboard","Monitor","Laptop"]
for i in collection:
 count+=1
 print("Item no",count,":",i)

#while loop

count=1
while count<=5:
  print(count)
  count+=1

  contact={
    "name":"Fahad",
    "Contact":"03093212224",
    "email":"fahad@gmail.com"
  }
for key,value in contact.items():
  print(key,":",value)


count = 0
password = ""
while password != "fahad123":
    if count == 0:
        password = input("Enter Password to access File: ")
    else:
        password = input("Plz Enter Correct Password: ")
    count += 1
print("Access Granted!")


#simple analyzer...

numbers=[12,7,19,25,4,8,9]
tottal=0
even_count=0
largest=numbers[0]
for num in numbers:
   tottal+=num
   if num%2==0:
       even_count+=1

   if num>largest:
      largest=num

average=tottal/len(numbers)

print("Total:",tottal)
print("Evencount:",even_count)
print("Largest Number:",largest)
print("Average:",average)



