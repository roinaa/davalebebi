import csv
import random
from faker import Faker
fake = Faker()
with open("persons.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["ID", "first_name", "last_name", "age"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, 51):
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(20, 80)

        writer.writerow({
            "ID": i,
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        })