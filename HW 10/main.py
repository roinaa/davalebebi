# 1 დავალება

data = [(1, 3), (4, 2), (2, 5)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)


# 2 დავალება

def divide_numbers():
    try:
        a = int(input("შეიყვანე პირველი რიცხვი: "))
        b = int(input("შეიყვანე მეორე რიცხვი: "))
        result = a / b
        return result

    except ValueError:
        print("გთხოვ შეიყვანე მხოლოდ რიცხვები")

    except ZeroDivisionError:
        print("ნულზე გაყოფა არ შეიძლება")

print("შედეგი:", divide_numbers())


# 3 დავალება

from functools import reduce
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

# 1. filter() 
cheap_products = list(filter(lambda product: product["price"] < 100, products))
print("პროდუქტები რომელთა ფასიც ნაკლებია 100-ზე:")
for product in cheap_products:
    print(product)

# 2. map()
names_and_prices = list(map(lambda p: f"{p['name']}: {p['price']}", products))
print("\nყველა პროდუქტის სახელი და ფასი:")
for info in names_and_prices:
    print(info)

# 3. sorted() 
sorted_products = sorted(products, key=lambda p: p["price"])
print("\nპროდუქტები დალაგებულია ფასის მიხედვით:")
for product in sorted_products:
    print(product)

# 4. reduce() 
total_price = reduce(lambda acc, p: acc + p["price"], products, 0)
print("\nყველა პროდუქტის ფასების ჯამი:", total_price)


# 4 დავალება

def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)
number = int(input("შეიყვანე მთელი რიცხვი: "))
if number >= 1:
    result = recursive_sum(number)
    print(f"1-დან {number}-ის ჩათვლით რიცხვების ჯამი არის: {result}")
else:
    print("გთხოვ შეიყვანე მთელი დადებითი რიცხვი")
