my_file = open('./6. Files/data.txt', 'r')   #abrir ficheiro, 'r' modo read

file_content = my_file.read()

my_file.close() # Indica ao sistema operativo que o file foi fechado

print(file_content)

name = input("Enter your name: ")
my_file_writing = open('./6. Files/data.txt', 'w')

'''
Na linha de código a baixo o meu primeiro pensamento foi escrever
my_file_writing.write(name) mas porque é que não o devo fazer??
Nesse caso a variavel é escrita diretamente no ficheiro e isso só funcionará
se a variavel for uma string, pois o método write() espera que seja uma string.

my_file_writing.write(f'{name}') será a forma correta, convertendo o valor de
name para uma string antes de escrevê-lo no file.

'''
my_file_writing.write(f'{name}') 

my_file_writing.close()


