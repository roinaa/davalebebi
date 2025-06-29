import math
# pirveli davaleba

a = int(input("შეიყვანეთ პირველი კათეტის სიგრძე (მთელი დადებითი რიცხვი): "))
b = int(input("შეიყვანეთ მეორე კათეტის სიგრძე (მთელი დადებითი რიცხვი): "))

hypotenuse = math.sqrt(a**2 + b**2)

area = (a * b) / 2

print("ჰიპოთენუზის სიგრძე არის:", round(hypotenuse, 2))
print("სამკუთხედის ფართობი არის:", round(area, 2))


# meore davaleba
total_seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} წამი არის {hours} საათი, {minutes} წუთი, {seconds} წამი")