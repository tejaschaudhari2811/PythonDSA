class InvalidInt(ValueError):
    pass


age = input("Please enter your age: ")
try:
    age = int(age)
except InvalidInt:
    raise InvalidInt("please enter a valid number")