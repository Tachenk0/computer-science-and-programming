import random

print('задание 1')
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(num)):
    if num[i] == 3:
        num[i] = 30
        break 
print(num)


print('задание 2')
num1 = [1, 2, 3, 4, 5]
sqr = [ x**2 for x in num1]
print(sqr)


print('задание 3')
num2 = [14, 12, 2, 8, 5, 11]
max_num2 = max(num2)
len_list = len(num2)
result = max_num2 / len_list
print("Наибольшее число:", max_num2)
print("Длина списка:", len_list)
print("Результат деления:", result)


print('задание 4')
tuple_elem= (3, 1, 4, 2, )
if all(isinstance(x1, (int, float)) for x1 in tuple_elem):
 sort_tuple = tuple(sorted(tuple_elem))
 print("Отсортированный кортеж:", sort_tuple)
else:
    print("Кортеж остаётся неизменным:", tuple_elem)


print('задание 5')
prod = {
    'яблоки': 50,
    'бананы': 30,
    'апельсины': 40,
    'груши': 60,
    'киви': 70
}
max_prod = max(prod, key=prod.get)
max_price = prod[max_prod]

min_prod = min(prod, key=prod.get)
min_price = prod[min_prod]

print("Товар с максимальной ценой:", max_prod, "с ценой:", max_price)
print("Товар с минимальной ценой:", min_prod, "с ценой:", min_price)


print('задание 6')
elemen = ['apple', 'cherry', 'date','cat']
result_dict = {elemen: elemen for elemen in elemen}
print(result_dict)


print('задание 7')
translations = {
    'яблоко': 'apple',
    'кот': 'cat',
    'вишня': 'cherry',
    'груша': 'pear',
    'киви': 'kiwi'
}

rus_word = input("Введите русское слово для перевода на английский: ")

eng_translation = translations.get(rus_word)

if eng_translation:
    print(f"Перевод '{rus_word}' на английский: {eng_translation}")
else:
    print(f"Перевод для слова '{rus_word}' не найден.")

print('задание 8')
import random

def get_winner(user_choice, computer_choice):
    
    rules = {
        'камень': ['ножницы', 'ящерица'],
        'ножницы': ['бумага', 'ящерица'],
        'бумага': ['камень', 'спок'],
        'ящерица': ['спок', 'бумага'],
        'спок': ['ножницы', 'камень']
    }
    
    if user_choice == computer_choice:
        return "Ничья!"
    elif computer_choice in rules[user_choice]:
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def main():
    options = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']
    
   
    user_choice = input("Введите камень, ножницы, бумагу, ящерицу или спок: ").lower()
    
    if user_choice not in options:
        print("Некорректный ввод. Пожалуйста, выберите один из вариантов.")
        return
    
   
    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")
    
  
    result = get_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()

