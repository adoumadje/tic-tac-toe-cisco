board = [
    [1, 2, 3],
    [4, 'x', 6],
    [7, 8, 9]
]

def start():
    while True:
        display()
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
