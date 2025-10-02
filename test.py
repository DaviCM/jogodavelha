table = [[' ' for cols in range(3)] for rows in range(3)]

playerRow = int(input('\n''Insira a linha da casa que deseja jogar: '))
playerCol = int(input('Insira a coluna da casa que deseja jogar: '))
table[playerRow][playerCol] = 'X'

print(table)