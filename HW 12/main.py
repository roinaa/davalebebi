# 1 დავალება

import csv

def collect_users_to_csv(count):
    with open("users.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["ID", "first_name", "last_name", "age"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, count + 1):
            print(f"\nმომხმარებელი #{i}")
            first_name = input("შეიყვანე სახელი:").strip()
            last_name = input("შეიყვანე გვარი:").strip()
            while True:
                try:
                    age = int(input("შეიყვანე ასაკი: ").strip())
                    break
                except ValueError:
                    print("შეიყვანე მხოლოდ რიცხვი")
            writer.writerow({
                "ID": i,
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            })
while True:
    try:
        user_count = int(input("რამდენი მომხმარებლის შეყვანა გსურს?:"))
        break
    except ValueError:
        print("გთხოვ შეიყვანე მხოლოდ მთელი რიცხვი")
collect_users_to_csv(user_count)


# 2 დავალება

def split_students_by_grade():
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        passed = []
        failed = []
        for row in reader:
            try:
                grade = int(row["Grade"])
                if grade >= 50:
                    passed.append(row)
                else:
                    failed.append(row)
            except (ValueError, KeyError):
                continue 
    with open("failed_students.csv", "w", newline="", encoding="utf-8") as fail_file:
        writer = csv.DictWriter(fail_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(failed)
    with open("passed_students.csv", "w", newline="", encoding="utf-8") as pass_file:
        writer = csv.DictWriter(pass_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(passed)
split_students_by_grade()
