from random import randint

winConditions = {
    1 : [(0, 0), (0, 1), (0, 2)],
    2 : [(1, 0), (1, 1), (1, 2)],
    3 : [(2, 0), (2, 1), (2, 2)],
    4 : [(0, 0), (1, 0), (2, 0)],
    5 : [(0, 1), (1, 1), (2, 1)],
    6 : [(0, 2), (1, 2), (2, 2)],
    7 : [(0, 0), (1, 1), (2, 2)],
    8 : [(0, 2), (1, 1), (2, 0)]
}


def checkEnd(winConditions, lastPlayed, symbol):
    for i in winConditions:
        for j in range(len(winConditions[i])):
            if winConditions[i][j] == lastPlayed:
                winConditions[i][j] = symbol
                
    for i in winConditions:
        if winConditions[i] == [symbol, symbol, symbol]:
            print(f'Fim de jogo: {symbol} vence.')
            return True, winConditions
    else:
        return False, winConditions 
        

gameEnded = False
while gameEnded != True:
    gameEnded, b = checkEnd(winConditions, (randint(0, 2), randint(0, 2)), 'X')
    print(gameEnded, b)
