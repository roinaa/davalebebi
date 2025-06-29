# 1 დავალება

def sum_numbers(times=5):
    total = 0
    for _ in range(times):
        while True:
            try:
                number = float(input("შეიყვანე რიცხვი: "))
                break
            except ValueError:
                print("გთხოვ შეიყვანე მხოლოდ რიცხვი")
        total += number
    return total
while True:
    user_input = input("რამდენი რიცხვის დაჯამება გსურს? (თუ დატოვებ ცარიელს ავტომატურად 5 რიცხვის დაჯამებას შეძლებ): ").strip()

    if user_input == "":
        count = 5
        break
    try:
        count = int(user_input)
        break
    except ValueError:
        print("გთხოვ შეიყვანე მხოლოდ მთელი რიცხვი")
result = sum_numbers(count)
print("რიცხვების ჯამი არის:", result)


# 2 დავალება

def luwi_da_kenti_ricxvebis_garcheva(*args):
  luwebi = []
  kentebi = []

  for ricxvi in args:
    if isinstance(ricxvi, int): 
      if ricxvi % 2 == 0:
        luwebi.append(ricxvi)
      else:
        kentebi.append(ricxvi)
        
  return luwebi, kentebi

user_input = input("შეიყვანე რიცხვები გამოტოვებით :")
ricxvebis_teqsturi_sia = user_input.split()
ricxvebi = []
for item in ricxvebis_teqsturi_sia:
  try:
    ricxvi = int(item)
    ricxvebi.append(ricxvi)
  except ValueError:
    print(f"'{item}' არ არის რიცხვი.")
if ricxvebi:
  luwi_ricxvebi, kenti_ricxvebi = luwi_da_kenti_ricxvebis_garcheva(*ricxvebi)
  print("-" * 20) 
  print(f"ლუწი რიცხვები: {luwi_ricxvebi}")
  print(f"კენტი რიცხვები: {kenti_ricxvebi}")
else:
  print("თქვენ არ შეგიყვანიათ რიცხვები.")


# 3 დავალება

import re

def count_word_frequency_from_user_input():
  sentence = input("გთხოვთ, შეიყვანოთ წინადადება: ")
  lower_case_sentence = sentence.lower()
  cleaned_sentence = re.sub(r'[^a-z\s]', '', lower_case_sentence)
  words = cleaned_sentence.split()
  word_counts = {}

  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
  return word_counts
frequency_dictionary = count_word_frequency_from_user_input()

print("\nდათვლილი სიტყვები")
print(frequency_dictionary)