# 1) Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.

a = float(input('Введите исходное число: '))
d = float(input('Введите "точность" вывода: '))
count = 0
if d == 1:
    print(int(a))
else:
    while d != 1:
        d *= 10
        count += 1
    print(round(a, count))


# 2) Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

n = int(input())
res_list = []
for i in range(2, n + 1):
    if n % i == 0:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            res_list.append(i)
print(res_list)

# 3) Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

# user_list = list(map(int, input().split()))
user_list = [1, 5, 6, 8, 1, 5, 6, 3]
res = []

for i in user_list:
    if user_list.count(i) == 1:
        res.append(i)

print(f'Исходный массив: {user_list}')
print(f'Уникальные элементы: {res}')