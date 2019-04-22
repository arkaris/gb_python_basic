# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

from hashlib import sha256

# my_str = input("Введите строку: ")
my_str = "olala"

substrings = {my_str[i:j] for i in range(len(my_str)) for j in range(i+1, len(my_str)+1)}

hashes = set(map(lambda s: sha256(s.encode("utf-8")).hexdigest(), substrings))

print(f"Получено {len(substrings)} подстрок и {len(hashes)} хешей")