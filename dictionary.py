person={
    "name":"Fahad",
    "age":21,
    "is_valid_for vot":True
}
print(person)
print(person.get("name"))
person["email"]="fahadkk833@gmail.com"
print(person)
print(person.pop("email"))  #remove entire key and return
print(person)
print(person.keys())

person.update({"age":22})  #update the key value....
print(person.get("age"))

person={
    "name":"Fahad",
    "age":21,
    "city":"karachi"
}
for key in person.keys():
    print(key)
print("====")
for key in person.values():
    print(key)
print("====")
for key,value in person.items():
    print("Keys:",key)
    print("value:",value)

#nested dictionary...
student={
    "name":"Fahad",
    "grades":{
        "English":"A+",
        "Math":"B+"
    }
}
print(student)
#commonly used in api responmses
response={
    "status":"Succeed",
    "data":{
        "id":1,
        "product_name":"Mouse",
        "price":"Rs:700"
    }
}
print(response)

#simple contact book
contact = {
    "name": "Fahad",
    "phone": "0309-3334567",
    
    "address": {
        "city": "Karachi",
        "country": "Pakistan"
    }
}

print("--- Contact Card ---")
print("Name:", contact["name"])
print("Phone:", contact["phone"])
print("Email:", contact.get("email", "No email provided"))  #this will simply show error measge but did not crash the program
# print("Email:", contact["email"])   #this will give error and crash the programe
print("City:", contact["address"]["city"])

contact["email"]="fahad@gmail.com"
contact["nickname"] = "Fadii"

print("\n--- Updated Contact ---")
for key, value in contact.items():
    print(key, ":", value)