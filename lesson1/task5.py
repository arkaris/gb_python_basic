begin, end = map((lambda s: ord(s[0])), input("Введите через один пробел два английских символа: ").split(" "))

# ord("A") == 65
# ord("Z") == 90
# ord("a") == 97
# ord("z") == 122

if not (65 <= begin <= 90 or 97 <= begin <= 122) or not (65 <= end <= 90 or 97 <= end <= 122):
	print("Не тот символ")
	exit()

if 97 <= begin <= 122:
	begin -= 32

if 97 <= end <= 122:
	end -= 32

begin -= 64
end -= 64

print(f"Первая буква стоит в алфавитена {begin} позиции")
print(f"Вторая буква стоит в алфавитена {end} позиции")

if begin > end:
	begin, end = end, begin

delta = end - begin - 1
if delta == -1:
	delta = 0

print(f"Между ними {delta} букв")