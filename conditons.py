print("if else statments...")

correct_username="admin123"
correct_password="root123"

user_name=input("Enter UserName:")

password=input("Enter Password:")

if user_name!=correct_username and password!=correct_password:
    print("Wrong username And password")
elif user_name!=correct_username and password==correct_password:
    print=("enter correct username plz")
elif user_name==correct_username and password!=correct_password:
    print("enter correct password plz")
else:
    print("Succesfully Login...")
    