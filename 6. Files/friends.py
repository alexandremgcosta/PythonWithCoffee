friends = input(
    'Enter three friend names, separated by commas (no spaces, please): ').split(',')
    
file = open('./6. Files/people.txt', 'r')
file_content = [line.strip() for line in file.readlines()]
file.close()

friends_set = set(friends)
people_set = set(file_content)

nearby_friends = friends_set.intersection(people_set)

file = open('./6. Files/nearby_friends.txt', 'w')

for f in nearby_friends:
    file.write(f+'\n')
    
file.close()