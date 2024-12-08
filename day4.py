import sys


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def dfs(board, word, x, y, direction, rows, cols):
    # Direction vectors for 8 possible directions
    directions = {
        "right": (0, 1),  # (x, y+1)
        "left": (0, -1),  # (x, y-1)
        "down": (1, 0),  # (x+1, y)
        "up": (-1, 0),  # (x-1, y)
        "down-right": (1, 1),  # (x+1, y+1)
        "down-left": (1, -1),  # (x+1, y-1)
        "up-right": (-1, 1),  # (x-1, y+1)
        "up-left": (-1, -1),  # (x-1, y-1)
    }

    dx, dy = directions[direction]

    for i in range(1, len(word)):
        x += dx
        y += dy

        # Check if we are out of bounds
        if not is_valid(x, y, rows, cols) or board[x][y] != word[i]:
            return False

    return True


def find_xmas(board):
    word = "XMAS"
    rows = len(board)
    cols = len(board[0])
    count = 0

    # Iterate over every cell in the grid
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:  # Start DFS if the first letter matches
                # Try each direction
                for direction in [
                    "right",
                    "left",
                    "down",
                    "up",
                    "down-right",
                    "down-left",
                    "up-right",
                    "up-left",
                ]:
                    if dfs(board, word, i, j, direction, rows, cols):
                        count += 1

    return count


def solve():
    pass


def parse_input_to_matrix(input_data):
    # Split the input data by newline and remove any surrounding whitespace
    rows = input_data.strip().splitlines()

    # Convert each row (string) into a list of characters
    matrix = [list(row) for row in rows]

    return matrix


if __name__ == "__main__":
    matrix = parse_input_to_matrix(sys.stdin.read().strip())
    print(find_xmas(matrix))
