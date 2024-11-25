print('задание 1')
tasks = [('Проверить почту', 3), ('Написать отчёт', 1), ('Позвонить клиенту', 2)]
sorted_tasks = sorted(tasks, key=lambda task: task[1])
print(sorted_tasks)


print('задание 2')
purchases = [
    {'item': 'Laptop', 'price': 1000, 'quantity': 2},
    {'item': 'Mouse', 'price': 25, 'quantity': 5},
    {'item': 'Keyboard', 'price': 45, 'quantity': 3}
    ]
total_costs = list(map(lambda purchase: purchase['price'] * purchase['quantity'], purchases))
print('Общая стоимость каждой покупки:', total_costs)
most_expensive_purchase = max(purchases, key=lambda purchase: purchase['price'] * purchase['quantity'])
print('Самая дорогая покупка:', most_expensive_purchase)


print('задание 3')
clients = [
    {'name': 'Alice', 'income': 50000},
    {'name': 'Bob', 'income': 120000},
    {'name': 'Charlie', 'income': 70000}
]
clients_with_category = list(map(lambda client: {
    **client,  
    'category': (
        'High' if client['income'] > 100000 else
        'Medium' if client['income'] >= 50000 else
        'Low'
    )}, clients))
print(clients_with_category)


print('задание 4')
flights = [
    {'flight': 'A1', 'departure': 9, 'arrival': 12},
    {'flight': 'B2', 'departure': 14, 'arrival': 18},
    {'flight': 'C3', 'departure': 6, 'arrival': 8}
]
flights_before_noon = list(filter(lambda flight: flight['arrival'] < 12, flights))
print(flights_before_noon)


print('задание 5')
import re

messages = [
    {'user': 'Исследователь А', 'message': 'Отчёт готов. Ссылка: http://foundation.org'},
    {'user': 'Доктор Б', 'message': 'Документы можно найти здесь: https://classified.com'},
    {'user': 'Охранник В', 'message': 'Нет аномальной активности за смену.'},
    {'user': 'Агент Г', 'message': 'Срочно изучите материалы по объекту 173 на http://statue-database.net'},
    {'user': 'Д-р Кляйн', 'message': 'Обновлённый протокол эксперимента доступен: https://safezone.scp'},
    {'user': 'Сотрудник Д', 'message': 'Просьба ознакомиться с https://docs.anomalies-secure.com перед сменой.'},
    {'user': 'Старший учёный Л', 'message': 'Все записи переданы. Никаких аномалий на объекте 096.'},
    {'user': 'Техник З', 'message': 'Проблема с сервером устранена. Подробнее: http://fix-report.internal'}
]
filtered_messages = list(filter(lambda msg: 'http://' in msg['message'] or 'https://' in msg['message'], messages))
for msg in filtered_messages:
    msg['message'] = re.sub(r'https?://[^\s]+', '[ДАННЫЕ УДАЛЕНЫ]', msg['message'])
print(filtered_messages)

