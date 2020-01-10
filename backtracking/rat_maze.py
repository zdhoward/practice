"""
0 = possible pathway
1 = wall
2 = rat's path
"""
board = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main():
    if solve(board, 0, 0, 0):
        print("Solvable")
        [print(row) for row in board]
    else:
        print("Not Solvable")


def solve(board, new_x, new_y, pos):
    if isAllowed(new_x, new_y):
        old_val = board[new_x][new_y]
        board[new_x][new_y] = 2
        pos += 1
        # print("Pos: ", pos, " | x: ", new_x, " | y: ", new_y)
        if isCompleted():
            return True
        for x, y in moves:
            if solve(board, new_x + x, new_y + y, pos):
                return True
        # print("Backtracking")
        board[new_x][new_y] = old_val
    return False


def isAllowed(x, y):
    if x >= 0 and x < 5 and y >= 0 and y < 5 and board[x][y] == 0:
        return True
    return False


def isCompleted():
    if board[4][4] == 2:
        return True
    return False


if __name__ == "__main__":
    main()
