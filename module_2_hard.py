def generate_password(n):
    password = ""
    pairs = []

    for i in range(1, 21):
        for j in range(i + 1, 21):
            total = i + j
            if n % total == 0:
                pairs.append((i, j))
    for (i, j) in pairs:
        password += f"{i}{j}"

    return password

import random

random_number = random.randint(3, 20)
print(f"Случайное число: {random_number}")
result_password = generate_password(random_number)
print(f"Пароль: {result_password}")

