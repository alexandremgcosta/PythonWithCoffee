import file_operations

file_operations.save_to_file('Testeee', './6. Files/teste_data.txt')

print(f'Lido do file teste_data.txt: {file_operations.read_file('./6. Files/teste_data.txt')}')