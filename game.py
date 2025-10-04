from random import randint
from time import sleep
from os import system

def proceed(message, cls=True):
    system('cls') if cls == True else ...
    print(message)
    sleep(1)
    system('cls') if cls == True else ...


def getInt(message):
    while True:
        try:
            intNum = int(input(message).strip())
            if (intNum < 1) or (intNum > 3):
                raise ValueError

            # Index da tupla sempre será -1, pois inicia no 0
            return intNum - 1
        
        except ValueError:
            proceed('Valor inválido. Por favor, tente novamente.', cls=False)
            continue


def printGame(matrix):
    c = 1
    system('cls')
    print('    1    2    3')

    for row in matrix:
        print(f'{c} {row}')
        c += 1


def getGameOrder():
    while True:
        player = (input('Escolha o símbolo que deseja jogar (X/O): ').upper()).strip()

        match player:
            case 'X':
                proceed('Você irá iniciar o jogo.')
                CPU = 'O'
                playerFirst = True
                break
            case 'O':
                proceed('Você será o segundo a jogar.')
                CPU = 'X'
                playerFirst = False
                break
            case _:
                proceed('Opção inválida. Por favor, tente novamente.')
                continue

    return player, CPU, playerFirst


def played(winConditions, lastPlayed):
    for i in winConditions:
        if lastPlayed in winConditions[i]:
            return False
        # 8 é a última condição de vitória
        elif i == 8 and lastPlayed not in winConditions[i]:
            return True
        else:
            continue
    

def checkEnd(winConditions, lastPlayed, symbol):
    for i in winConditions:
        for j in range(len(winConditions[i])):
            if winConditions[i][j] == lastPlayed:
                winConditions[i][j] = symbol
                
    for i in winConditions:
        if winConditions[i] == [symbol, symbol, symbol]:
            print(f'Fim de jogo: {symbol} vence. \n')
            return True, winConditions
    else:
        return False, winConditions # Else fora do for, senão sairia imediatamente


def getPlayerMove(winConditions):
    while True:
        playerCol = getInt('\n''Insira a coluna da casa que deseja jogar: ')
        playerRow = getInt('Insira a linha da casa que deseja jogar: ')

        if played(winConditions, (playerRow, playerCol)) == True:
            proceed('Você tentou jogar em uma casa já preenchida. tente novamente.', cls=False)
            continue
        else:
            return playerRow, playerCol


def getCPUMove(winConditions):
    while True:
        # 0, 1 e 2 são as possibilidades de valor da tupla
        CPURow = randint(0, 2)
        CPUCol = randint(0, 2)

        if played(winConditions, (CPURow, CPUCol)) == True:
            continue
        else:
            return CPURow, CPUCol

                
def game():
    player, CPU, playerFirst = getGameOrder()
    table = [[' ' for cols in range(3)] for rows in range(3)] # 3 linhas e 3 colunas
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

    while True:
        if playerFirst == True:
            system('cls')
            printGame(table)
            
            playerRow, playerCol = getPlayerMove(winConditions)
            table[playerRow][playerCol] = player
            
            printGame(table)
            gameEnded, winConditions = checkEnd(winConditions, (playerRow, playerCol), player)
            if gameEnded == True:
                break
            sleep(1)
            system('cls')
            
            CPURow, CPUCol = getCPUMove(winConditions)
            table[CPURow][CPUCol] = CPU
            
            printGame(table)
            gameEnded, winConditions = checkEnd(winConditions, (CPURow, CPUCol), CPU)
            if gameEnded == True:
                break
            sleep(3)
            continue

        else:
            printGame(table)
            sleep(1)
            system('cls')
            
            CPURow, CPUCol = getCPUMove(winConditions)
            table[CPURow][CPUCol] = CPU
            
            gameEnded, winConditions = checkEnd(winConditions, (CPURow, CPUCol), CPU)
            if gameEnded == True:
                break
            
            printGame(table)
            
            playerRow, playerCol = getPlayerMove(winConditions)
            table[playerRow][playerCol] = player
            
            printGame(table)
            gameEnded, winConditions = checkEnd(winConditions, (playerRow, playerCol), player)
            if gameEnded == True:
                break
            sleep(3)
            continue
    
    while True:
        opt = (input('Deseja jogar novamente? (s/n): ').lower()).strip()
    
        match opt:
            case 's':
                return False
            case 'n':
                system('cls')
                print('Adeus.')
                return True
            case _:
                proceed('Opção inválida. Por favor, tente novamente.')
                continue


def main():
    quitGame = False

    while quitGame != True:
        system('cls')
        print('Bem vindo ao jogo da velha! \n')
        opt = (input('Deseja iniciar o jogo? (s/n): ').lower()).strip()

        match opt:
            case 's':
                quitGame = game()
            case 'n':
                system('cls')
                print('Adeus.')
                quitGame = True
            case _:
                proceed('Opção inválida. Por favor, tente novamente.')
                continue


main()
