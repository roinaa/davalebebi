# დავალება 1

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

while True:
    name_input = input("შეიყვანე სახელი (ან შეიყვანე 'stop' გასაჩერებლად): ").strip()
    if name_input.lower() == "stop":
        break

    found_name = [p for p in persons if p[0].lower() == name_input.lower()]
    if not found_name:
        print("ეს სახელი სიაში არ მოიძებნა.")
        continue

    surname_input = input("შეიყვანე გვარი: ").strip()
    found_full = [p for p in found_name if p[1].lower() == surname_input.lower()]

    if found_full:
        print("ასაკი არის:", found_full[0][2])
    else:
        print("ეს გვარი ამ სახელთან ერთად სიაში არ მოიძებნა.")


# დავალება 2

word1 = input("შეიყვანე პირველი სიტყვა: ").strip()
word2 = input("შეიყვანე მეორე სიტყვა: ").strip()

set1 = set(word1)
set2 = set(word2)

print("საერთო სიმბოლოები:", set1 & set2)
print("განსხვავებული სიმბოლოები:", set1 ^ set2)
print("გაერთიანებული სიმბოლოები:", set1 | set2)


# დავალება 3

sentence = input("შეიყვანე წინადადება: ")

cleaned = sentence.replace(" ", "")
result = tuple(cleaned)

print("ტაპლი:", result)

