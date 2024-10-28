print('Задание 1')
t = (int(input('Введите температуру: ')))
if (t > 20):
 print('Кондиционер выключается')
else:
 print('Кондиционер включается')
print('Задание 2')
a = input()
if a == '12' or a == '1' or a == '2':
    print('Зима')
elif a == '3' or a == '4' or a == '5': 
    print('Весна')
elif a == '6' or a == '7' or a == '8':  
    print('Лето')
elif a == '9' or a == '10' or a == '11':  
    print('Осень')
else:  
    print('Номер месяца введён неверно')
print('Задание 3')
while True:
    print("Введите возраст")
    print("Если программа выводит ошибку, то введено не число")
    years = int(input())
    if years not in range(1,23):
        print("Число не в диапазоне 1-22")
        continue
    if years >= 2:
        year1 = 10.5 * 2
        year2 = 4 * (years - 2)
        humanyears = year1 + year2
    else:
        humanyears = 10.5
    print(humanyears)
print('Задание 4')
while True:
    print("Введите число")
    num = str(input())
    sumd = 0
    for i in num:
        sumd += int(i)
    if int(num[-1]) % 2 == 0 and sumd % 3 == 0:
        print("Число делится на 6")
    else:
        print("Число не делится на 6")
print('Задание 5')
