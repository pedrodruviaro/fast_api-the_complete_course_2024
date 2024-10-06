# Functions

def print_my_name(firstname, lastname, msg="Gogogo"):
    fullname = f"{firstname} {lastname}"
    print(f"Hello, {fullname}! {msg}")

print_my_name(firstname="John", lastname="Doe", msg="Nice!")
print_my_name("Mark", "Ruffalo")


def multiply (a, b):
    return a * b

solution = multiply(2, 89)
print(solution)


def create_user (firstname, lastname, age):
    user_dict = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return user_dict

new_user = create_user(firstname="John", lastname="Macklane", age=50)
print(new_user)

