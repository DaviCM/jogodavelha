table = [['' for cols in range(3)] for rows in range(3)]
c = 1

for i in range(len(table)):
    for j in range(len(table[i])):
        table[i][j] = c
        c += 1

print(table)