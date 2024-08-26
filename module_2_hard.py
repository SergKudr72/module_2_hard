n = int(input('Введите число от 3 до 20: '))
pairs = []

for i in range(1, n):
    for j in range(1, (i+1)):
        if n % (i+j) == 0 and (i, j) not in pairs and i != j:
            pairs.append((j, i))

print(n, '-', pairs)
