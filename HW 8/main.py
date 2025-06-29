# 1 დავალება
def count_upper_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    upper_text = text.upper()
    return f"{count} დიდი ასო იყო ტექსტში", upper_text

txt = input("შეიყვანე ტექსტი: ")
result = count_upper_letters(txt)
print(result[0])
print("Uppercase:", result[1])


#  2 დავალება
def camel_to_snake(text):
    result = ""
    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result

user_input = input("შეიყვანე camel Case ცვლადი: ")
converted = camel_to_snake(user_input)

print("snake case ფორმატში:", converted)
