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
