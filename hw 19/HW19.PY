import json
import random
from faker import Faker

fake = Faker()
students = []

for _ in range(100):
    student = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

active_students = [student for student in loaded_students if student["is_active"]]

with open("active_students.json", "w", encoding="utf-8") as file:
    json.dump(active_students, file, ensure_ascii=False, indent=4)
