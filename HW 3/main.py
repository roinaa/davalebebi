# 1 დავალება

print("დავალება 1 - BMI-ის გამოთვლა")

weight = float(input("შეიყვანე წონა (კგ): "))
height = float(input("შეიყვანე სიმაღლე (მ): "))

bmi = weight / (height ** 2)
print("შენი BMI არის:", round(bmi, 2))

if bmi < 19:
    print("შენ ხარ underweight")
elif 19 <= bmi <= 25:
    print("შენი წონა ნორმაშია (normalweight)")
else:
    print("შენ ხარ overweight")

print("\n")


# 2 დავალება

print("დავალება 2 - ფაქტორიალის გამოთვლა")

num = int(input("შეიყვანე რიცხვი ფაქტორიალისთვის: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}-ის ფაქტორიალი არის: {factorial}")
print("\n")


# 3 დავალება

print("დავალება 3 - გამრავლების ტაბულა")

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
print("\n")


# 4 დავალება

print("დავალება 4 - გადახდის აპარატი")

total = 50
paid = 0
valid_notes = [5, 10, 20]

print("გადასახდელი თანხა: 50 ლარი")

while paid < total:
    try:
        note = int(input("შეიტანე კუპიურა (5, 10 ან 20 ლარი): "))
    except ValueError:
        print("გთხოვ შეიყვანე რიცხვი")
        continue

    if note not in valid_notes:
        print("არასწორი კუპიურაა. სცადე ხელახლა.")
    else:
        paid += note
        remaining = total - paid
        if remaining > 0:
            print(f"დარჩენილი გადასახდელი თანხა: {remaining} ლარი")

change = paid - total
print(f"გადახდა დასრულებულია. თქვენი ხურდა არის: {change} ლარი")
