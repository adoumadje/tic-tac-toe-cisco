import random

board = [
    [1, 2, 3],
    [4, 'x', 6],
    [7, 8, 9]
]

def start():
    while True:
        display()
        myPlay()
        if checkWin('O'):
            display()
            print("You won")
            break
        computerPlay()
        if checkWin('X'):
            display()
            print("Computer won")
            break
        if checkDraw():
            display()
            print("You drew")
            break



def myPlay():
    correct = False
    while not correct:
        move = int(input("Enter your move: "))
        for row in board:
            for col in row:
                if col == move:
                    correct = True
                    board[(col - 1) // 3][(col - 1) % 3] = 'O'
                    break
            if correct:
                break
        if not correct:
            print("Wrong input!!! Try again...")

def computerPlay():
    plays = []
    for row in board:
        for col in row:
            if isinstance(col, int):
                plays.append(col)
    i = random.randint(0, len(plays) - 1)
    col = plays[i]
    board[(col - 1) // 3][(col - 1) % 3] = 'X'

def checkWin(play):
    n = len(board)

    for row in board:
        win = True
        for col in row:
            if col != play:
                win = False
                break;
        if win:
            return True

    for c in range(n):
        win = True
        for r in range(n):
            if board[r][c] != play:
                win = False
                break
        if win:
            return True

    r, c = 0, 0
    win = True
    while r < n and c < n:
        if board[r][c] != play:
            win = False
            break
        r += 1
        c += 1
    if win:
        return True

    r, c = 0, n-1
    win = True
    while r < n and c >= 0:
        if board[r][c] != play:
            win = False
            break
        r += 1
        c -= 1
    return win

def checkDraw():
    for row in board:
        for col in row:
            if isinstance(col, int):
                return False
    return True

def display():
    top = ('+' + '-' * 7) * 3 + '+'
    empty_mid = ('|' + ' ' * 7) * 3 + '|'
    for row in board:
        print(top)
        print(empty_mid)
        for col in row:
            print('|' + ' ' * 3 + str(col) + ' ' * 3, end='')
        print('|')
        print(empty_mid)
    print(top)

if __name__ == '__main__':
    start()
