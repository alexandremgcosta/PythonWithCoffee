"""

friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
    print("This runs too.")
else:
    print("Hello, stranger!")

print("Isto já não faz parte do if!")


name = input("Enter yout name: ")
if name:
    print("We know your name.")

"""

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")