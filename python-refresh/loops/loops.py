my_list = [1, 2, 3, 4, 5]
sum = 0

for item in my_list:
    sum += item

print(sum)

for i in range(90, 99):
    pass

num = 10
while num >= 0:
    if num == 0:
        break
    num -= 1

# Exercise
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for item in my_list:
    if item == "Monday":
        continue

    times_to_print = 3
    while times_to_print > 0:
        times_to_print -= 1
        print(item)

