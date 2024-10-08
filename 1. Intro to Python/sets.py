
# SETS não tem ordem e não contem elementos duplicados

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")

print(art_friends)

art_friends.add("Jen")

print(art_friends)

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

science_but_not_science = science_friends.difference(art_friends)
print(science_but_not_science)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)


art_and_science = art_friends.intersection(science_friends)
print(art_and_science)


all_friends = art_friends.union(science_friends)
print(all_friends)