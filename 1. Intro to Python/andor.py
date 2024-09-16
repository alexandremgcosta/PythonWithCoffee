age = 25

result = age > 18 and age < 65
print(result)




default_age = 30
age = 0
user_age = age or default_age
print(user_age)



default_greeting = "there"
name = input("Enter your name: (optional) ")

user_name = name or default_greeting
print(f"Hello, {user_name}!")