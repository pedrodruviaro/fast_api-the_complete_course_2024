# sets
my_set = {1, 2, 3, 4, 5, 1, 2}

for x in my_set:
    print(x)

my_set.discard(3)
print(my_set)

# tuples
my_tuple = (4, 5, 6, 7)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])

# my_tuple[2] = 1 -> error (not support assign)


# Exercise
zoo = ['monkey', 'snake', 'elephant', 'duck', 'rat', 'wolf', 'panda']
removedFromThirdPosition = zoo.pop(3)
zoo.append('chicken')
zoo.pop(0)

for animal in zoo:
    print(animal)

firstThreeAnimals = zoo[0:3]