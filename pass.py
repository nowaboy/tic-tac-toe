import random
import string

length = int(input("Длина пароля: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Случайный пароль:", password)
