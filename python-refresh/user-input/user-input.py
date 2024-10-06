# firstname = input('Enter your firstname: ')
# days = input("How many days before your birthday? ")
# print(firstname)
# print(360 - int(days))

days_unit_birthday = int(input("How many days until your birthday? "))
weeks_until_birthday = round((days_unit_birthday / 7), 2)
print(f'{weeks_until_birthday} weeks until your birthday!')