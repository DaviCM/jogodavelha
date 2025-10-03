from random import randint
from time import sleep
from os import system

def continuar(message, cls=True):
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

            return intNum - 1
        
        except ValueError:
            continuar('Valor inválido. Por favor, tente novamente.', cls=False)
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
                continuar('Você irá iniciar o jogo.')
                CPU = 'O'
                playerFirst = True
                break
            case 'O':
                continuar('Você será o segundo a jogar.')
                CPU = 'X'
                playerFirst = False
                break
            case _:
                continuar('Opção inválida. Por favor, tente novamente.')
                continue

    return player, CPU, playerFirst


def getPlayerMove(played):
    while True:
        playerCol = getInt('\n''Insira a coluna da casa que deseja jogar: ')
        playerRow = getInt('Insira a linha da casa que deseja jogar: ')

        if (playerRow, playerCol) in played:
            continuar('Você tentou jogar em uma casa já preenchida. tente novamente.', cls=False)
            continue
        else:
            return playerRow, playerCol


def getCPUMove(played):
    while True:
        CPURow = randint(0, 2)
        CPUCol = randint(0, 2)

        if (CPURow, CPUCol) in played:
            continue
        else:
            return CPURow, CPUCol


def checkEnd(table):
    ...


def game():
    player, CPU, playerFirst = getGameOrder()
    table = [[' ' for cols in range(3)] for rows in range(3)]
    played = []

    while True:
        if playerFirst == True:
            while True:
                printGame(table)

                playerRow, playerCol = getPlayerMove(played)
                table[playerRow][playerCol] = player
                played.append((playerRow, playerCol))

                printGame(table)
                sleep(1)
                system('cls')

                CPURow, CPUCol = getCPUMove(played)
                table[CPURow][CPUCol] = CPU
                played.append((CPURow, CPUCol))

                printGame(table)
                sleep(3)
                system('cls')
                continue

        else:
            while True:
                printGame(table)

                CPURow, CPUCol = getCPUMove(played)
                table[CPURow][CPUCol] = CPU
                played.append((CPURow, CPUCol))

                printGame(table)
                sleep(1)
                system('cls')

                playerRow, playerCol = getPlayerMove(played)
                table[playerRow][playerCol] = player
                played.append((playerRow, playerCol))

                printGame(table)
                sleep(3)
                system('cls')
                continue


def main():
    system('cls')
    print('Bem vindo ao jogo da velha! \n')

    while True:
        opt = (input('Deseja iniciar o jogo? (s/n): ').lower()).strip()

        match opt:
            case 's':
                game()
            case 'n':
                system('cls')
                print('Adeus.')
                break
            case _:
                continuar('Opção inválida. Por favor, tente novamente.')
                continue


main()
