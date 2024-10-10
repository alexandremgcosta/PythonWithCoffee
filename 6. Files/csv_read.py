file = open('./6. Files/csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    p = line.split(',')
    
    print(f'{p[0].title()} is {p[1]}, studying {p[2].capitalize()} at {p[3].title()}')
    
    
sample_csv_value = ','.join(['Rolf','25', 'MIT','Computer Science'])
print(sample_csv_value)