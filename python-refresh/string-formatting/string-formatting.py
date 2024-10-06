firstname = 'John'
lastname = 'Doe'
fullname = f'{lastname} {lastname}'
print(fullname)

phrase = 'Hi, {} {}'
formated = phrase.format(firstname, lastname)
print(formated)