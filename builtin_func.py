print("Python builtin function....")
#string method
#you can use . to call method
#syntex
#string.method()

#first are case conversion
name="fahad ali"
print(name.lower())
print(name.upper())
print(name.capitalize()) #convert 1st letter of string into capital..
print(name.title())      #convert 1st letter of each word..

#cleaning
word="hello world"
print(word.strip())
print(word.lstrip())
print(word.rstrip())

user_input = "   FAHAD.ALI@EMAIL.COM   "
cleaned_email = user_input.strip().lower()
print(cleaned_email)
#searching
print(word.find("l"))
print(word.count("l"))
print(word.startswith("h"))
print(word.isdecimal())
#split and join
print(word.split("-"))
print(word.join("-"))

#replace
newword="cat"
print(newword.replace("c","b"))
#IN FUNTION....
email = "fAHAD.ALI@example.com"
if "@" in email:
    print("Valid email format")
else:
    print("Invalid email")

    #LETS BUILD SIMPLE data CLEANER....

raw_data=input("Enter some sentence of data:")
email=input("Enter an email of source:")
if "@" and email.lower()==True in email:
    print("Email is valid")
else:
    print("Enter Valid email plz...")

cleaned_data=raw_data.strip().lower()
word_count=len(cleaned_data.split())
upercase_version=cleaned_data.upper()
find_word=cleaned_data.find("f")

print("----Analysis---------")
print("Entered text is : ",raw_data)
print()
print("Cleaned Data  : ",cleaned_data)
print("Uppercase version:", upercase_version)
print("Mentions How many words:", find_word)