str=input("Введи строку:")
print("Длина строки = ",len(str))
glasn=0
soglasn=0
a = "аоуыеёиэяю"
b = "!,.?1234567890' '#№&+=/*-_@^%\""
for i in str:
        if i in a:
             glasn+=1
        elif i in b:
             continue
        else:
              soglasn+=1
print("Гласных букв = ",glasn)
print("Согласных букв = ",soglasn)
