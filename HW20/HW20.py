import json
import os

def add_persons(n):
    if not os.path.exists("persons.json"):
        with open("persons.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    with open("persons.json", "r", encoding="utf-8") as f:
        try:
            persons = json.load(f)
        except json.JSONDecodeError:
            persons = []
    last_id = persons[-1]["id"] if persons else 0
    for _ in range(n):
        name = input("შეიყვანეთ სახელი: ")
        while True:
            try:
                age = int(input("შეიყვანე ასაკი: "))
                break
            except ValueError:
                print("შეიყვანე მხოლოდ რიცხვი.")
        person = {
            "id": last_id + 1,
            "name": name,
            "age": age
        }
        persons.append(person)
        last_id += 1
    with open("persons.json", "w", encoding="utf-8") as f:
        json.dump(persons, f, ensure_ascii=False, indent=4)
    print(f"{n} პერსონა წარმატებით დაემატა ფაილში.")
if __name__ == "__main__":
    while True:
        try:
            count = int(input("რამდენი პერსონის დამატება გსურთ?: "))
            break
        except ValueError:
            print("გთხოვთ, შეიყვანეთ მხოლოდ რიცხვი.")