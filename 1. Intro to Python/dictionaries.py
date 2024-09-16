
# GUARDA keys e values 
# Dicionario mantem a ordem em que foram adicionados

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

#Adicionar key ao dicionario
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25
print(friend_ages)


friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "RAdam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

print(friends[0]["name"])


# Data to Dictionaries

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 11)]
friend_ages = dict(friends)
print(friend_ages)