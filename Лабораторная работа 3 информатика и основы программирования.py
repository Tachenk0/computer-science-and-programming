print('задание 1')
a = input("Введите имя")
b = int(input("Введите возраст"))
for _ in range(10):
    print('Меня зовут', a,'и мне', b,'лет')
print('задание 2')
n = int(input('n = '))

for i in range(1, 11):
    print(f'{n}*{i} = {n * i}')
print('задание 3')
for c in range (1,101,3):
    print(c)
print('задание 4')
num = int(input('Введите число: '))
f = num
for i in range(1, num):
    f = f * i
print(f)
print('задание 5')
i = 20
while i > 0:
    i-=1
    print(i)
print('задание 6')

fibon = int(input("Введите число:"))
f1 = f2 = 1
i=0
while i<fibon:
    f1, f2 = f2, f1+f2
    print(f2, end=" ")
    i +=1
print(' ')     
print('задание 7')   
l="привет"
i=1
for a in range(0, len(l)):
    print(l[i], i, sep="", end="")
print('задание 8')
def main():
    while True:
        try:
            num1 = float(input('Введите первое число : '))
            num2 = float(input('Введите второе число : '))
            sum = num1 + num2

            print(f'Вы ввели: {num1} и {num2}')
            print(f'сумма: {sum}')
        
        except ValueError:
            print('Неверный ввод. Пожалуйста, введите числовые значения.')
        break

if __name__ == '__main__':
    main()
