#Напишите программу, которая запрашивает у пользователя строку и выводит ее длину,
# количество гласных и солганных символов. (Строки вводятся на русском)
n=str(input("Введите строку:"))
print(n)
length = len(n)
print(f"Длина строки: {length}")
vowels = "аеёиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"
vowel_count = 0
consonant_count = 0
for char in n.lower():
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print(f"Количество гласных: {vowel_count}")
print(f"Количество согласных: {consonant_count}")
