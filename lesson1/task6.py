char_number = int( input("Введите номер символа английского алфавита: ") )

if not (1 <= char_number <= 26):
	print("Нет такой буквы")
	exit()

print("Это буква ", chr(char_number + 64))