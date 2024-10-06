import grades_services as services
import random
import math

grades = {
    'math': 89,
    'english': 92,
    'bio': 60
}

total = services.calculate_grades(grades)
print(total)

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(nums))

print(random.randint(1, 999))


print(math.sqrt(4))