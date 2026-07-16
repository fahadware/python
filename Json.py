#serialization (Json to pyhton object like dict) using load
import json 

data='{"name":"Fahad","Age":21}'

y=json.loads(data)

print(y["name"])
print(y["Age"])
#serilization (dic to json text) using dump

import json 
data={
    "name":"fahad",
    "Age":21,
    "DOB":"29-12-2004",
    "is_student":True
}
print(data)
json_string=json.dumps(data)
print(json_string)

#lets write data dirctly to json file
with open("data.json","w") as j_file:
    json.dump(data,j_file)

import json
with open("data.json","r") as file:
    content=json.load(file)
    print(content)

#simple contact book
import json
def save_contact(contact):
    with open("contacts.json","w") as file:
        json.dump(contact,file,indent=4)
def load_contact():
    try:
        with open('contact.json',"r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
        return []
        
contacts=load_contact()
contacts.append({"name": "Fahad", "phone": "0309-1234567"})
contacts.append({"name": "Hammad", "phone": "0311-9876543"})
save_contact(contacts)
print("----Saved contacts------")
for contact in load_contact():
    print(f"{contact['name']}: {contact['phone']}")