students = [
    {"name": "ali", "scores": [12, 15, 17], "is_active": True},
    {"name": "sara", "scores": [10, 13, 19], "is_active": False},
]

print(students)

while True:
    for student in students:
        print(
            f"name : {student['name']} , scores : {student['scores']} , is_active : {student['is_active']}"
        )
    name = input("enter student name: ")
    scores = []
    while True:
        user_input = input("enter score (or 'done') :")
        if user_input == "done":
            break
        scores.append(int(user_input))

    new_student = {"name": name, "scores": scores, "is_active": True}
    students.append(new_student)
    break
print("GPA Calculation :")
for student in students:
    total = 0
    for score in student["scores"]:
        total = total + score

    average = total / len(student["scores"])
    print(f"{student['name']} average: {round(average, 2)}")  
