def average(seq):
    return sum(seq) / len(seq)

# IGUAIS

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for stu in students:
    name = stu["name"]
    grades = stu["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total' or 'top': ")

    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == "top":
        print(top(grades))