def divide(x, y):
    if y == 0:
        return print("You tried to divide by zero!")
    else:
        return x / y

divide(10, 0)


# o " y=3 " serve de default parameter

def add(x, y=3):
    total = x+y
    return total

print(add(5))


# Argumento especial

print(1, 3, 2, 4, 5, sep=" - ")



# O PYTHON DEFINE O y = default_y
default_y = 3

def add(x, y= default_y):
    total = x + y
    print(total)

add(2)
# MESMO QUE DEPOIS SE ATRIBUA UM NOVO VALOR
# O PYTHON JÁ DEU ASSIGN À VARIAVEL 
default_y = 4
add(2)