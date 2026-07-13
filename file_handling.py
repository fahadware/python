#open file and write an statment by "with" statment
with open("My_file.txt","w") as myfile: #w->write
    myfile.write("Hello from fahad")

with open("My_file.txt","r") as myfile:  #r->read(file myst be exist)
    content=myfile.read()
    print(content)

with open("My_file.txt","r") as myfile:
    for lines in myfile:
        print(lines)

with open("My_file.txt","a") as myfile:
    myfile.write("\nI am computer science student")
#after appending text....

with open("My_file.txt","r") as myfile:  #r->read(file myst be exist)
    content=myfile.read()
    print(content)

with open("My_file.txt", "r") as file:
     content = file.read()
     file.close()   # you must remember to do this manually!
     print(content)

lines_to_write=["Fahad\n","Hammad\n","Shahzaib\n"]
with open("Names.txt","w") as newfile:
    newfile.writelines(lines_to_write)  #write =lines is used fro writing multiple lines at once

with open("Names.txt","r") as myfile:
    content=myfile.read()
    print(content)

#word count in file
with open("Names.txt","r") as myfile:
    content=myfile.read()
    word_count=len(content.split())
    print(content)
    print(word_count)

#file handling using exceptional handling
try:
    with open("Mynotes.txt","r") as myfile:
       contnet=myfile.read()
       print(content)
except FileNotFoundError as f:
    print("the file does not exist")

import os 
if os.path.exists("Mynotes.txt"):
    with open("Mynotes.txt","r") as f:
        print(f.read())
else:
    print("File not found")

