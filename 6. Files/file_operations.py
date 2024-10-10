def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(f'{content}')
        
def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()