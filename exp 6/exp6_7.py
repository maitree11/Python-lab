# a) keyword argument
def student(name, age):
    print("Name: ", name)
    print("Age: ", age)
    print("\n")

student(age=19, name="Maitree")

# b) default argument
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Maitree")
print("\n")

# c) variable length argument
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(10,20,30))

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name="Maitree", age = 19)