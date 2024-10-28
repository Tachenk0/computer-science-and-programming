import re
while True:
    containsUpper = 0
    containsLower = 0
    containsNumbers = 0
    containsSpecialSym = 0
    print("Введите пароль")
    password = str(input())
    for i in password:
        if re.search(r'[A-Z]',i):
            containsUpper = 1
    for i in password:
        if re.search(r'[a-z]', i):
            containsLower = 1
    for i in password:
        if re.search(r'[0-9]', i):
            containsNumbers = 1
    for i in password:
        if re.search(r'[^A-Za-z0-9А-Яа-я]', i):
            containsSpecialSym = 1
    if not(containsUpper and containsLower and containsNumbers and containsSpecialSym and len(password) >= 8):
        if containsUpper == 0:
            print("В пароле нет заглавных букв")
        if containsLower == 0:
            print("В пароле нет строчных букв")
        if containsNumbers == 0:
            print("В пароле нет цифр")
        if containsSpecialSym == 0:
            print("В пароле нет спецсимволов")
        if len(password) < 8:
            print("Пароль недостаточно длинный")
    else:
        break
