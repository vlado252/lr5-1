# Запрашиваем ввод строки у пользователя
str = input("Введи строку:")

# Выводим длину введенной строки
print("Длина строки = ", len(str))

# Инициализируем счетчики для гласных и согласных букв
glasn = 0
soglasn = 0

# Определяем строки с гласными буквами и символами, которые нужно игнорировать
a = "аоуыеёиэяю"
b = "!,.?1234567890' '#№&+=/*-_@^%\""

# Проходим по каждому символу в введенной строке
for i in str:
    # Если символ является гласной буквой, увеличиваем счетчик гласных
    if i in a:
        glasn += 1
    # Если символ находится в списке игнорируемых символов, пропускаем его
    elif i in b:
        continue
    # В противном случае, увеличиваем счетчик согласных букв
    else:
        soglasn += 1

# Выводим количество гласных букв
print("Гласных букв = ", glasn)

# Выводим количество согласных букв
print("Согласных букв = ", soglasn)