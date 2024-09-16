age = 34
age_as_str = str(age)
print("You are " + age_as_str)


#Formata a string de forma a não ter de usar uma variavel auxiliar para converter o integer
print(f"You are {age}")

name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)

#Limitação: Se agora mudar o nome da variavel name e chamar greeting, mantem o nome Jose.
name = "Bob"
print(greeting)

# Outra forma de formatar a string:
print("--")
name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)