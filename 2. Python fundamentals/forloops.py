friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)


elements = [0,1,2,3,4,5,6,7,8,9]

for _ in elements:
    print("Hello, world!")

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")