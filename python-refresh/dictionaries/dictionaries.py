# Dictionaries

user = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 28
}

print(user['firstName'])
print(user.get('lastName'))

user['maried'] = True
print(user)
print(len(user))

user.pop('age')
print(user)

# user.clear()
# print(user)

# del user

for x, y in user.items(): 
    print(x)
    print(y)

user2 = user.copy()
user2.pop("maried")

print(user)
print(user2)

# Exercice
print("----- EXERCISE -----")

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for key, value in my_vehicle.items():
    print(f"key -> {key}")
    print(f"value -> {value}")

vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
vehicle2.pop("mileage")
print(vehicle2)

for key in vehicle2:
    print(key)