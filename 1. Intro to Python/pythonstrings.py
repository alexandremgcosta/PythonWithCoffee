my_string = "Hello, world!"
print(my_string)

string_with_quotes = "Hello, it's me."

another_with_quotes = 'He said "You are amazing!" yesterday.'

multiline = """Hello, world.

My name is Alexandre.


Welcome to my program.
"""

print(multiline)


name = "Jose"
greeting = "Hello, "+name
print(greeting)

# Não é possivel juntar um integer com uma string. Temos de converter o integer

age = 34

age_as_str = str(age)
print("You are " + age_as_str)