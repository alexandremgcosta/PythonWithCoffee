my_name = "Jose"
your_name = input("Enter your name: ")
print(f"Hello {your_name}. My name is {my_name}.")

print(" ")
print("--")
print(" ")

age = input("Enter your age: ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months.")

print(" ")
print("--")
print(" ")

# Outra forma de o fazer:

age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} months.")