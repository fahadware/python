#type conversion...
print("Type conversion")
age = 25
#print("My age is " + age)----->Give type error

print("My age is " + str(age))

print(type(age))

age_text = "25"
age_number = int(age_text)     # converts str "25" to int 25

price = 19
price_float = float(price)     # converts int 19 to float 19.0

score = 95
score_text = str(score)        # converts int 95 to str "95"

flag = bool(1)                 # converts int 1 to bool True

## converts str "25" to int 25
price_str="25"

price_float=float(price_str)

print(price_float)
print(type(price_float))

item_name = "Coffee"
price = 4.5          # float
quantity = 3          # int

total = price * quantity
print("Item: " + item_name)
print("Total: $" +  str(total))