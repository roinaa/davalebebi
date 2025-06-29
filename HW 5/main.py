# 1 დავალება
numbers = [7, 6, 16, 3, 11]
sum_ = 0

for num in numbers:
    sum_ += num

average = sum_ / len(numbers)

print("ჯამი:", sum_)
print("საშუალო:", average)


# 2 დავალება
data = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
unique = []

for item in data:
    if item not in unique:
        unique.append(item)

print("უნიკალური სია:", unique)

# 3 დავალება
import random

numbers = [random.randint(-50, 50) for _ in range(20)]

even_numbers = [num for num in numbers if num % 2 == 0]

print("ყველა რიცხვი:", numbers)
print("მხოლოდ ლუწები:", even_numbers)


