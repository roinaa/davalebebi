import math
from concurrent.futures import ThreadPoolExecutor

def is_prime(n):
    if n <= 1:
        return f"{n} არ არის მარტივი"
    if n == 2:
        return f"{n} არის მარტივი"
    if n % 2 == 0:
        return f"{n} არ არის მარტივი"
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return f"{n} არ არის მარტივი"
    return f"{n} არის მარტივი"
num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]
with ThreadPoolExecutor() as executor:
    results = list(executor.map(is_prime, num_list))
for res in results:
    print(res)
