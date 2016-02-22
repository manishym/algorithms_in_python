#/usr/bin/env python


board = []
size = 8


def danger(row, col):
    for i, j in board:
        if i == row: return True 
        if j == col: return True 
        if abs(i - row) == abs(j - col): return True 

    return False


def queens(row):
    if(row > size):
        print board
    else:
        for col in range(1, size + 1):
            if not danger(row, col):
                board.append((row, col))
                queens(row+1)
                board.remove((row, col))

def main():
    queens(1)


if __name__ == "__main__":
    main()
