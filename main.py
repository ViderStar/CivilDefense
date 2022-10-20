n = int(input())
a = list(map(int, input().split()))
count = []
for i in range(n):
    id_tuple = (a[i], i)
    count.append(id_tuple)
m = int(input())
bomb = []
b = list(map(int, input().split()))
for i in range(m):
    id_tuple = (b[i], i)
    bomb.append(id_tuple)
count.sort()
bomb.sort()
res = []
a = 0
for i in range(len(count)):
    for j in range(a, len(bomb)):
        if j + 1 == len(bomb):
            id_tuple = (count[i][1], bomb[j][1])
            res.append(id_tuple)
            a = j
            break
        if abs(count[i][0] - bomb[j][0]) <= abs(count[i][0] - bomb[j + 1][0]):
            id_tuple = (count[i][1], bomb[j][1])
            res.append(id_tuple)
            a = j
            break
res.sort()
for i in range(n):
    print(res[i][1] + 1, end=' ')
# Тест 1
# Входные данные:
# 4
# 1 2 6 10
# 2
# 7 3
# Вывод программы:
# 2 2 1 1
# Тест 2
# Входные данные:
# 1
# 1
# 1
# 2
# Вывод программы:
# 1
# Тест 3
# Входные данные:
# 10
# 79 64 13 8 38 29 58 20 56 17
# 10
# 53 19 20 85 82 39 58 46 51 69
# Вывод программы:
# 5 10 2 2 6 3 7 3 7 2