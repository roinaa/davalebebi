# 1 დავალება

def save_names_to_file():
    with open("names.txt", "w", encoding="utf-8") as file:
        count = 1
        while True:
            first_name = input("Enter your first name: ").strip()
            if first_name.lower() == "stop":
                break
            last_name = input("Enter your last name: ").strip()
            file.write(f"{count}. {first_name} {last_name}\n")
            count += 1
save_names_to_file()


# 2 დავალება

def split_people_by_age():
    with open("persons.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    younger = []  
    older = []    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) < 3:
            continue  
        try:
            age = int(parts[1].strip())
        except ValueError:
            continue 
        if age < 50:
            younger.append(line.strip())
        else:
            older.append(line.strip())
    with open("under50.txt", "w", encoding="utf-8") as u_file:
        for person in younger:
            u_file.write(person + "\n")
    with open("over50.txt", "w", encoding="utf-8") as o_file:
        for person in older:
            o_file.write(person + "\n")
split_people_by_age()