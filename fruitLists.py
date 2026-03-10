#Change List Items
fruits = ["Banana", "Guavas", "Apples", "Oranges"]
fruits[1] = "Mangoes"
print(fruits)

#Change second and third value by replacing with one value
fruits[1:3] = ["Watermelon"]
print(fruits)

#insert() at specific index
fruits.insert(2, "Passion")
print(fruits)

#add list items
fruits.append("BlackCurrent")
print(fruits)

#Length
print(len(fruits))

#Items Present 
if "Banana" in fruits:
    print("Yes, 'Banana' is on the list")

#Join Lists extend()
cars = ["Volvo", "BMW", "Demio"]
fruits.extend(cars)
print(fruits)

#Loop Through A List
for x in fruits:
    print(x)
    
for i in range(len(fruits)):
    print(fruits[i])
