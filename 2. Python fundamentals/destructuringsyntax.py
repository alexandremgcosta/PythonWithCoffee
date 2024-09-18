# O Python permite:

currencies = 0.8, 1.2
usd, eur = currencies
# Por exemplo, tradicionalmente teriamos de fazer da seguinte forma:

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

for friend in friends:
    print(friend)

# Mas com o Python é possivel fazer da seguinte forma:

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

for name, age in friends:   #Ele entende que em cada tuplo vai colocar a string no name e o integer no age
    print(name, age)