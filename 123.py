from random import randint
n = int(input("Количество строк:"))
m = int(input("Количество столбцов:"))
b = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        b[i][j]=randint(10,99)
for i in range(n):
    print(" ".join(map(str,b[i])))
min = b[0][0]
str_min=0
stb_min=0
for i in range(n):
    for j in range(m):
        if b[i][j]<min:
            min = b[i][j]
            str_min = i
            stb_min = j
print('Минимальное значение равно ',min, 'адрес:',str_min,',',stb_min)
