print('задание 1')
def converter(time, f, t):
     total = 0
     if time > 0:
         if f == 'h':
             if t == 'h': total = time
             if t == 'm': total = time * 60
             if t == 's': total = time * 3600
         if f == 'm':
             if t == 'h': total = time/60
             if t == 'm': total = time
             if t == 's': total = time*60
         if f == 's':
             if t == 'h': total = time/3600
             if t == 'm': total = time/60
             if t == 's': total = time

     message = str(total) +''+ t
     return message

time,f,t = input('Введите время: '), input('С чего конвертировать (h,m,s): '), input('Во что конвертировать (h,m,s): ')
print(converter(int(time),f,t))

print('задание 2')
def f(a,n):
     procnew = 0
     if a < 30000: print('Минимальная сумма - 30000')
     else:
        proc = 0.3 * (a/10000)
        if proc >= 5:proc = 5

        if n <= 3: procnew = a * (1 + (proc + 3)/100)**(int(n))
        if n > 3 and n <= 6: procnew = (a * (1 + (proc + 3)/100)**3) * (1 + (proc + 5)/100)**(int(n)-3)
        if n > 6: procnew = ((a * (1 + (proc + 3)/100)**3) * (1 + (proc + 5)/100)**3) * (1 + (proc + 2)/100)**(int(n)-6)

        return procnew - a
    
a,n = float(input('Введите сумму: ')), float(input('На сколько лет?: '))
print(f(a,n))

print('задание 3')
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes_in_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        return 'Начало и конец диапазона должны быть целыми числами.'
    if start > end:
        return 'Начало диапазона не может быть больше конца диапазона.'
    if start < 1 or end < 1:
        return 'Диапазон должен начинаться с 1 или больше.'

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
print('введите начало диапозона')
start_range = int(input())
print('введите конец диапозона')
end_range = int(input())
primes = find_primes_in_range(start_range, end_range)
print('Простые числа в диапазоне от', start_range, 'до', end_range, ':', primes)
print('Задание 4')
def input_matrix(size):
   
    matrix = []
    print(f'Введите {size} строк(и) матрицы, разделяя элементы пробелами:')
    for _ in range(size):
        row = list(map(int, input().strip().split()))
        if len(row) != size:
            raise ValueError(f'Каждая строка должна содержать {size} элементов.')
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    
    size = len(matrix1)
    result = []
    for i in range(size):
        result_row = []
        for j in range(size):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(result_row)
    return result

def print_matrix(matrix):
    
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    try:
       
        size = int(input('Введите размер матриц (больше 1): '))
        if size < 2:
            raise ValueError('Размер матриц должен быть больше 1.')

        
        print('Матрица 1:')
        matrix1 = input_matrix(size)
        print('Матрица 2:')
        matrix2 = input_matrix(size)

        
        result_matrix = add_matrices(matrix1, matrix2)

       
        print('Результат сложения матриц:')
        print_matrix(result_matrix)

    except ValueError as e:
        print('Ошибка:', e)


if __name__ == '__main__':
    main()
print('задание 5')
def is_palindrome(s):

    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

def main():
    
    user_input = input('Введите строку: ')
    
    if is_palindrome(user_input):
        print('Да')
    else:
        print('Нет')


if __name__ == '__main__':
    main()
